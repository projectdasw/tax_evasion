from otree.api import *
import random


doc = """
Select a random round for payment
"""


class C(BaseConstants):
    NAME_IN_URL = 'nt_pay_random'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    round = models.IntegerField(initial=0)
    potential_payoff = models.FloatField(min=0, max=1, initial=0)


# PAGES
class WaitAllPlayer(WaitPage):
    wait_for_all_groups = True


class MyPage(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        player.potential_payoff = float(participant.nt_payment)
        player.round = int(participant.selected_round)


class PayRandom(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.payoff = (player.potential_payoff * 50) + 10000


class Results(Page):
    timeout_seconds = 10


page_sequence = [WaitAllPlayer, MyPage, PayRandom, Results]
