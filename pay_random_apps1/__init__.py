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
    timeout_seconds = 10

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant

        apps = [
            'no_treatment1', 'no_treatment2', 'no_treatment3', 'no_treatment4', 'no_treatment5', 'no_treatment6',
            'no_treatment7', 'no_treatment8', 'no_treatment9', 'no_treatment10', 'no_treatment11', 'no_treatment12',
            'no_treatment13', 'no_treatment14', 'no_treatment15', 'no_treatment16', 'no_treatment17', 'no_treatment18',
            'no_treatment19', 'no_treatment20', 'no_treatment21', 'no_treatment22', 'no_treatment23', 'no_treatment24',
            'no_treatment25', 'no_treatment26', 'no_treatment27', 'no_treatment28', 'no_treatment29', 'no_treatment30',
        ]

        random_apps = random.choice(apps)
        player.name_apps = random_apps

        if player.name_apps == 'no_treatment1':
            player.round = 1
            player.potential_payoff = float(participant.pay_treatment1)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment2':
            player.round = 2
            player.potential_payoff = float(participant.pay_treatment2)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment3':
            player.round = 3
            player.potential_payoff = float(participant.pay_treatment3)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment4':
            player.round = 4
            player.potential_payoff = float(participant.pay_treatment4)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment5':
            player.round = 5
            player.potential_payoff = float(participant.pay_treatment5)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment6':
            player.round = 6
            player.potential_payoff = float(participant.pay_treatment6)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment7':
            player.round = 7
            player.potential_payoff = float(participant.pay_treatment7)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment8':
            player.round = 8
            player.potential_payoff = float(participant.pay_treatment8)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment9':
            player.round = 9
            player.potential_payoff = float(participant.pay_treatment9)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment10':
            player.round = 10
            player.potential_payoff = float(participant.pay_treatment10)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment11':
            player.round = 11
            player.potential_payoff = float(participant.pay_treatment11)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment12':
            player.round = 12
            player.potential_payoff = float(participant.pay_treatment12)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment13':
            player.round = 13
            player.potential_payoff = float(participant.pay_treatment13)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment14':
            player.round = 14
            player.potential_payoff = float(participant.pay_treatment14)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment15':
            player.round = 15
            player.potential_payoff = float(participant.pay_treatment15)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment16':
            player.round = 16
            player.potential_payoff = float(participant.pay_treatment16)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment17':
            player.round = 17
            player.potential_payoff = float(participant.pay_treatment17)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment18':
            player.round = 18
            player.potential_payoff = float(participant.pay_treatment18)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment19':
            player.round = 19
            player.potential_payoff = float(participant.pay_treatment19)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment20':
            player.round = 20
            player.potential_payoff = float(participant.pay_treatment20)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment21':
            player.round = 21
            player.potential_payoff = float(participant.pay_treatment21)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment23':
            player.round = 23
            player.potential_payoff = float(participant.pay_treatment23)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment24':
            player.round = 24
            player.potential_payoff = float(participant.pay_treatment24)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment25':
            player.round = 25
            player.potential_payoff = float(participant.pay_treatment25)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment26':
            player.round = 26
            player.potential_payoff = float(participant.pay_treatment26)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment27':
            player.round = 27
            player.potential_payoff = float(participant.pay_treatment27)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment28':
            player.round = 28
            player.potential_payoff = float(participant.pay_treatment28)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment29':
            player.round = 29
            player.potential_payoff = float(participant.pay_treatment29)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'no_treatment30':
            player.round = 30
            player.potential_payoff = float(participant.pay_treatment30)
            player.payoff = player.potential_payoff * 100 + 10000


class Results(Page):
    pass


page_sequence = [WaitAllPlayer, MyPage, Results]
