import time
import csv
import random

from otree import settings
from otree.api import *

from .image_utils import encode_image

doc = """
Real-effort tasks. The different tasks are available in task_matrix.py, task_transcription.py, etc.
You can delete the ones you don't need. 
"""


def get_task_module(player):
    """
    This function is only needed for demo mode, to demonstrate all the different versions.
    You can simplify it if you want.
    """
    from . import task_math

    session = player.session
    task = session.config.get("task")
    if task == "math":
        return task_math
    # default
    return task_math


class Constants(BaseConstants):
    name_in_url = "tax_nt"
    players_per_group = 4
    num_rounds = 30

    instructions_template = __name__ + "/instructions.html"
    captcha_length = 3


class Subsession(BaseSubsession):
    def creating_session(self):
        for group in self.get_groups():
            group.set_group_bagipajak()


def creating_session(subsession: Subsession):
    session = subsession.session
    template = dict(
        retry_delay=1.0, puzzle_delay=0, attempts_per_puzzle=1, attempts_per_puzzle_pilot=10, max_iterations=None,
        max_math=None
    )
    session.params = {}
    for param in template:
        session.params[param] = session.config.get(param, template[param])

    subsession.group_randomly()
    audit_event = open(__name__ + '/parameter/audit_event.csv', encoding='utf-8-sig')
    lower_return = open(__name__ + '/parameter/lower_return.csv', encoding='utf-8-sig')
    middle_return = open(__name__ + '/parameter/middle_return.csv', encoding='utf-8-sig')
    higher_return = open(__name__ + '/parameter/higher_return.csv', encoding='utf-8-sig')

    audit = list(csv.DictReader(audit_event))
    lowertax = list(csv.DictReader(lower_return))
    middletax = list(csv.DictReader(middle_return))
    highertax = list(csv.DictReader(higher_return))
    random.shuffle(audit)
    random.shuffle(lowertax)
    random.shuffle(middletax)
    random.shuffle(highertax)

    groups = subsession.get_groups()
    for i in range(len(groups)):
        lowertax_cols = lowertax[i]
        middletax_cols = middletax[i]
        highertax_cols = highertax[i]
        player = groups[i]
        if player.round_number <= 10:
            player.return_tax = float(lowertax_cols['97'])
        elif player.round_number <= 20:
            player.return_tax = float(middletax_cols['110'])
        elif player.round_number <= 30:
            player.return_tax = float(highertax_cols['105'])

    players = subsession.get_players()
    for i in range(len(players)):
        audit_cols = audit[i]
        player = players[i]
        player.audit = bool(int(audit_cols['1']))


class Group(BaseGroup):
    return_tax = models.FloatField()
    totalpajak = models.FloatField(min=0, max=1)
    bagipajak = models.FloatField(min=0, max=1)

    def set_group_bagipajak(self):
        self.group_bagipajak = self.bagipajak


class Player(BasePlayer):
    iteration = models.IntegerField(initial=0)
    num_trials = models.IntegerField(initial=0)
    num_correct = models.IntegerField(initial=0)
    num_failed = models.IntegerField(initial=0)
    pendapatan = models.FloatField(min=0, max=1, initial=0)
    laporpendapatan = models.FloatField(label="Masukkan Pendapatan Anda", initial=0)
    bebanpajak = models.FloatField(min=0, max=1, initial=0)
    audit = models.BooleanField()
    denda = models.FloatField(min=0, max=1, initial=0)

# puzzle-specific stuff


class Puzzle(ExtraModel):
    """A model to keep record of all generated puzzles"""

    player = models.Link(Player)
    iteration = models.IntegerField(initial=0)
    attempts = models.IntegerField(initial=0)
    timestamp = models.FloatField(initial=0)
    # can be either simple text, or a json-encoded definition of the puzzle, etc.
    text = models.LongStringField()
    # solution may be the same as text, if it's simply a transcription task
    solution = models.LongStringField()
    response = models.LongStringField()
    response_timestamp = models.FloatField()
    is_correct = models.BooleanField()


def generate_puzzle(player: Player) -> Puzzle:
    """Create new puzzle for a player"""
    task_module = get_task_module(player)
    fields = task_module.generate_puzzle_fields()
    player.iteration += 1
    return Puzzle.create(
        player=player, iteration=player.iteration, timestamp=time.time(), **fields
    )


def get_current_puzzle(player):
    puzzles = Puzzle.filter(player=player, iteration=player.iteration)
    if puzzles:
        [puzzle] = puzzles
        return puzzle


def encode_puzzle(puzzle: Puzzle):
    """Create data describing puzzle to send to client"""
    task_module = get_task_module(puzzle.player)  # noqa
    # generate image for the puzzle
    image = task_module.render_image(puzzle)
    data = encode_image(image)
    return dict(image=data)


def get_progress(player: Player):
    """Return current player progress"""
    return dict(
        num_trials=player.num_trials,
        num_correct=player.num_correct,
        num_incorrect=player.num_failed,
        iteration=player.iteration,
    )


def play_game(player: Player, message: dict):
    """Main game workflow
    Implemented as reactive scheme: receive message from vrowser, react, respond.

    Generic game workflow, from server point of view:
    - receive: {'type': 'load'} -- empty message means page loaded
    - check if it's game start or page refresh midgame
    - respond: {'type': 'status', 'progress': ...}
    - respond: {'type': 'status', 'progress': ..., 'puzzle': data} -- in case of midgame page reload

    - receive: {'type': 'next'} -- request for a next/first puzzle
    - generate new puzzle
    - respond: {'type': 'puzzle', 'puzzle': data}

    - receive: {'type': 'answer', 'answer': ...} -- user answered the puzzle
    - check if the answer is correct
    - respond: {'type': 'feedback', 'is_correct': true|false, 'retries_left': ...} -- feedback to the answer

    If allowed by config `attempts_pre_puzzle`, client can send more 'answer' messages
    When done solving, client should explicitely request next puzzle by sending 'next' message

    Field 'progress' is added to all server responses to indicate it on page.

    To indicate max_iteration exhausted in response to 'next' server returns 'status' message with iterations_left=0
    """
    session = player.session
    my_id = player.id_in_group
    params = session.params
    task_module = get_task_module(player)

    now = time.time()
    # the current puzzle or none
    current = get_current_puzzle(player)

    message_type = message['type']

    # page loaded
    if message_type == 'load':
        p = get_progress(player)
        if current:
            return {
                my_id: dict(type='status', progress=p, puzzle=encode_puzzle(current))
            }
        else:
            return {my_id: dict(type='status', progress=p)}

    if message_type == "cheat" and settings.DEBUG:
        return {my_id: dict(type='solution', solution=current.solution)}

    # client requested new puzzle
    if message_type == "next":
        if current is not None:
            if current.response is None:
                raise RuntimeError("trying to skip over unsolved puzzle")
            if now < current.timestamp + params["puzzle_delay"]:
                raise RuntimeError("retrying too fast")
            if player.num_correct == params['max_math']:
                return {
                    my_id: dict(
                        type='status', progress=get_progress(player), iterations_left=0
                    )
                }
        # generate new puzzle
        z = generate_puzzle(player)
        p = get_progress(player)
        return {my_id: dict(type='puzzle', puzzle=encode_puzzle(z), progress=p)}

    # client gives an answer to current puzzle
    if message_type == "answer":
        if current is None:
            raise RuntimeError("trying to answer no puzzle")

        if current.response is not None:  # it's a retry
            if current.attempts >= params["attempts_per_puzzle"]:
                raise RuntimeError("no more attempts allowed")
            if now < current.response_timestamp + params["retry_delay"]:
                raise RuntimeError("retrying too fast")

            # undo last updation of player progress
            player.num_trials -= 1
            if current.is_correct:
                player.num_correct -= 1
            else:
                player.num_failed -= 1

        # check answer
        answer = message["answer"]

        if answer == "" or answer is None:
            raise ValueError("bogus answer")

        current.response = answer
        current.is_correct = task_module.is_correct(answer, current)
        current.response_timestamp = now
        current.attempts += 1

        # update player progress
        if current.is_correct:
            player.num_correct += 1
        else:
            player.num_failed += 1
        player.num_trials += 1

        retries_left = params["attempts_per_puzzle"] - current.attempts
        p = get_progress(player)
        return {
            my_id: dict(
                type='feedback',
                is_correct=current.is_correct,
                retries_left=retries_left,
                progress=p,
            )
        }

    raise RuntimeError("unrecognized message from client")


# FUNCTIONS
def set_jumlahpajak(group):
    players = group.get_players()
    total_pajak = [p.bebanpajak for p in players]
    group.totalpajak = sum(total_pajak)
    group.bagipajak = (group.totalpajak * (group.return_tax / 100)) / Constants.players_per_group


# PAGES
class WaitPlayer(WaitPage):
    wait_for_all_groups = True


class Game(Page):
    timeout_seconds = 65
    live_method = play_game

    @staticmethod
    def js_vars(player: Player):
        return dict(params=player.session.params)

    @staticmethod
    def vars_for_template(player: Player):
        task_module = get_task_module(player)
        return dict(DEBUG=settings.DEBUG,
                    input_type=task_module.INPUT_TYPE,
                    placeholder=task_module.INPUT_HINT)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if not timeout_happened and not player.session.params['max_iterations']:
            raise RuntimeError("malicious page submission")

        if player.num_correct > 0:
            player.pendapatan += 100 * player.num_correct
        else:
            player.pendapatan += 0


class Results(Page):
    timeout_seconds = 10


class BeforeTaxPage(Page):
    timeout_seconds = 10


class TaxPage(Page):
    timeout_seconds = 20

    form_model = 'player'
    form_fields = ['laporpendapatan']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        laporpendapatanbersih = player.laporpendapatan - 200
        laporpendapatanlebih = player.laporpendapatan - player.pendapatan

        if laporpendapatanlebih > 500:
            player.bebanpajak = 0
        elif 0 < laporpendapatanbersih <= 500:
            player.bebanpajak = laporpendapatanbersih * 0.05
        elif 500 < laporpendapatanbersih <= 1000:
            player.bebanpajak = (500 * 0.05) + ((laporpendapatanbersih - 500) * 0.15)
        elif laporpendapatanbersih > 1000:
            player.bebanpajak = (500 * 0.05) + (500 * 0.15) + ((laporpendapatanbersih - 1000) * 0.25)
        elif laporpendapatanbersih <= 0:
            player.bebanpajak = 0


class TotalPajak(WaitPage):
    after_all_players_arrive = set_jumlahpajak


class PooledTax(Page):
    timeout_seconds = 10

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        hasilbagipajak = player.group.bagipajak
        pres_denda = (player.pendapatan - player.laporpendapatan) * 0.5
        laporpendapatanlebih = player.laporpendapatan - player.pendapatan

        if laporpendapatanlebih > 0 and player.audit == 1:
            player.denda = 0
            player.payoff = player.pendapatan - player.bebanpajak + hasilbagipajak
        elif player.audit == 1:
            player.denda = pres_denda
            player.payoff = player.pendapatan - player.denda - player.bebanpajak + hasilbagipajak
        elif laporpendapatanlebih > 0 and player.audit == 0:
            player.denda = 0
            player.payoff = player.pendapatan - player.bebanpajak + hasilbagipajak
        elif player.audit == 0:
            player.payoff = player.pendapatan - player.bebanpajak + hasilbagipajak


class FinalResults(Page):
    timeout_seconds = 10

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        laporpendapatanlebih = player.laporpendapatan - player.pendapatan
        participant.laporlebih = laporpendapatanlebih

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant

        if player.round_number == Constants.num_rounds:
            random_round = random.randint(1, Constants.num_rounds)
            participant.selected_round = random_round
            player_in_selected_round = player.in_round(random_round)
            participant.nt_payment = player_in_selected_round.payoff


page_sequence = [WaitPlayer, Game, Results, WaitPlayer, BeforeTaxPage, TaxPage, TotalPajak, PooledTax, FinalResults]
