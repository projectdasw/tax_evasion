from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'before_experiment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    session = subsession.session
    template = dict(
        retry_delay=1.0, puzzle_delay=0, attempts_per_puzzle=1, attempts_per_puzzle_pilot=10, max_math=None,
    )
    session.params = {}
    for param in template:
        session.params[param] = session.config.get(param, template[param])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# FUNCTIONS
# PAGES
class InfoPage(Page):
    timeout_seconds = 20


page_sequence = [InfoPage]
