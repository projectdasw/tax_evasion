from otree.api import *
import random


doc = """
Select a random round for payment
"""


class C(BaseConstants):
    NAME_IN_URL = 'pay_random_apps2'
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
            'corruption1', 'corruption2', 'corruption3', 'corruption4', 'corruption5', 'corruption6',
            'corruption7', 'corruption8', 'corruption9', 'corruption10', 'corruption11', 'corruption12',
            'corruption13', 'corruption14', 'corruption15', 'corruption16', 'corruption17', 'corruption18',
            'corruption19', 'corruption20', 'corruption21', 'corruption22', 'corruption23', 'corruption24',
            'corruption25', 'corruption26', 'corruption27', 'corruption28', 'corruption29', 'corruption30',
        ]

        random_apps = random.choice(apps)
        player.name_apps = random_apps

        if player.name_apps == 'corruption1':
            player.round = 1
            player.potential_payoff = float(participant.pay_treatment1)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption2':
            player.round = 2
            player.potential_payoff = float(participant.pay_treatment2)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption3':
            player.round = 3
            player.potential_payoff = float(participant.pay_treatment3)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption4':
            player.round = 4
            player.potential_payoff = float(participant.pay_treatment4)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption5':
            player.round = 5
            player.potential_payoff = float(participant.pay_treatment5)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption6':
            player.round = 6
            player.potential_payoff = float(participant.pay_treatment6)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption7':
            player.round = 7
            player.potential_payoff = float(participant.pay_treatment7)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption8':
            player.round = 8
            player.potential_payoff = float(participant.pay_treatment8)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption9':
            player.round = 9
            player.potential_payoff = float(participant.pay_treatment9)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption10':
            player.round = 10
            player.potential_payoff = float(participant.pay_treatment10)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption11':
            player.round = 11
            player.potential_payoff = float(participant.pay_treatment11)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption12':
            player.round = 12
            player.potential_payoff = float(participant.pay_treatment12)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption13':
            player.round = 13
            player.potential_payoff = float(participant.pay_treatment13)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption14':
            player.round = 14
            player.potential_payoff = float(participant.pay_treatment14)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption15':
            player.round = 15
            player.potential_payoff = float(participant.pay_treatment15)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption16':
            player.round = 16
            player.potential_payoff = float(participant.pay_treatment16)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption17':
            player.round = 17
            player.potential_payoff = float(participant.pay_treatment17)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption18':
            player.round = 18
            player.potential_payoff = float(participant.pay_treatment18)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption19':
            player.round = 19
            player.potential_payoff = float(participant.pay_treatment19)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption20':
            player.round = 20
            player.potential_payoff = float(participant.pay_treatment20)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption21':
            player.round = 21
            player.potential_payoff = float(participant.pay_treatment21)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption23':
            player.round = 23
            player.potential_payoff = float(participant.pay_treatment23)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption24':
            player.round = 24
            player.potential_payoff = float(participant.pay_treatment24)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption25':
            player.round = 25
            player.potential_payoff = float(participant.pay_treatment25)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption26':
            player.round = 26
            player.potential_payoff = float(participant.pay_treatment26)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption27':
            player.round = 27
            player.potential_payoff = float(participant.pay_treatment27)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption28':
            player.round = 28
            player.potential_payoff = float(participant.pay_treatment28)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption29':
            player.round = 29
            player.potential_payoff = float(participant.pay_treatment29)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'corruption30':
            player.round = 30
            player.potential_payoff = float(participant.pay_treatment30)
            player.payoff = player.potential_payoff * 100 + 10000


class Results(Page):
    pass


page_sequence = [WaitAllPlayer, MyPage, Results]
