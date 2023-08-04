from otree.api import *
import random


doc = """
Select a random round for payment
"""


class C(BaseConstants):
    NAME_IN_URL = 'pay_random_apps1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name_apps = models.StringField()
    round = models.IntegerField()
    potential_payoff = models.FloatField(min=0, max=1, initial=0)


# PAGES
class WaitAllPlayer(WaitPage):
    wait_for_all_groups = True


class MyPage(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        random_round = random.randint(1, 30)
        player.round = random_round


class PayRandom(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant

        if player.round == 1:
            player.name_apps = 'no_treatment1'
            player.potential_payoff = float(participant.pay_treatment1)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 2:
            player.name_apps = 'no_treatment2'
            player.potential_payoff = float(participant.pay_treatment2)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 3:
            player.name_apps = 'no_treatment3'
            player.potential_payoff = float(participant.pay_treatment3)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 4:
            player.name_apps = 'no_treatment4'
            player.potential_payoff = float(participant.pay_treatment4)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 5:
            player.name_apps = 'no_treatment5'
            player.potential_payoff = float(participant.pay_treatment5)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 6:
            player.name_apps = 'no_treatment6'
            player.potential_payoff = float(participant.pay_treatment6)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 7:
            player.name_apps = 'no_treatment7'
            player.potential_payoff = float(participant.pay_treatment7)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 8:
            player.name_apps = 'no_treatment8'
            player.potential_payoff = float(participant.pay_treatment8)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 9:
            player.name_apps = 'no_treatment9'
            player.potential_payoff = float(participant.pay_treatment9)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 10:
            player.name_apps = 'no_treatment10'
            player.potential_payoff = float(participant.pay_treatment10)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 11:
            player.name_apps = 'no_treatment11'
            player.potential_payoff = float(participant.pay_treatment11)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 12:
            player.name_apps = 'no_treatment12'
            player.potential_payoff = float(participant.pay_treatment12)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 13:
            player.name_apps = 'no_treatment13'
            player.potential_payoff = float(participant.pay_treatment13)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 14:
            player.name_apps = 'no_treatment14'
            player.potential_payoff = float(participant.pay_treatment14)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 15:
            player.name_apps = 'no_treatment15'
            player.potential_payoff = float(participant.pay_treatment15)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 16:
            player.name_apps = 'no_treatment16'
            player.potential_payoff = float(participant.pay_treatment16)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 17:
            player.name_apps = 'no_treatment17'
            player.potential_payoff = float(participant.pay_treatment17)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 18:
            player.name_apps = 'no_treatment18'
            player.potential_payoff = float(participant.pay_treatment18)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 19:
            player.name_apps = 'no_treatment19'
            player.potential_payoff = float(participant.pay_treatment19)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 20:
            player.name_apps = 'no_treatment20'
            player.potential_payoff = float(participant.pay_treatment20)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 21:
            player.name_apps = 'no_treatment21'
            player.potential_payoff = float(participant.pay_treatment21)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 22:
            player.name_apps = 'no_treatment22'
            player.potential_payoff = float(participant.pay_treatment22)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 23:
            player.name_apps = 'no_treatment23'
            player.potential_payoff = float(participant.pay_treatment23)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 24:
            player.name_apps = 'no_treatment24'
            player.potential_payoff = float(participant.pay_treatment24)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 25:
            player.name_apps = 'no_treatment25'
            player.potential_payoff = float(participant.pay_treatment25)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 26:
            player.name_apps = 'no_treatment26'
            player.potential_payoff = float(participant.pay_treatment26)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 27:
            player.name_apps = 'no_treatment27'
            player.potential_payoff = float(participant.pay_treatment27)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 28:
            player.name_apps = 'no_treatment28'
            player.potential_payoff = float(participant.pay_treatment28)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 29:
            player.name_apps = 'no_treatment29'
            player.potential_payoff = float(participant.pay_treatment29)
            player.payoff = player.potential_payoff * 50 + 10000
        elif player.round == 30:
            player.name_apps = 'no_treatment30'
            player.potential_payoff = float(participant.pay_treatment30)
            player.payoff = player.potential_payoff * 50 + 10000


class Results(Page):
    timeout_seconds = 10


page_sequence = [WaitAllPlayer, MyPage, PayRandom, Results]
