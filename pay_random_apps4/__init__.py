from otree.api import *
import random


doc = """
Select a random round for payment
"""


class C(BaseConstants):
    NAME_IN_URL = 'pay_random_apps4'
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
            'prefilled_corruption1', 'prefilled_corruption2', 'prefilled_corruption3', 'prefilled_corruption4',
            'prefilled_corruption5', 'prefilled_corruption6', 'prefilled_corruption7', 'prefilled_corruption8',
            'prefilled_corruption9', 'prefilled_corruption10', 'prefilled_corruption11', 'prefilled_corruption12',
            'prefilled_corruption13', 'prefilled_corruption14', 'prefilled_corruption15', 'prefilled_corruption16',
            'prefilled_corruption17', 'prefilled_corruption18', 'prefilled_corruption19', 'prefilled_corruption20',
            'prefilled_corruption21', 'prefilled_corruption22', 'prefilled_corruption23', 'prefilled_corruption24',
            'prefilled_corruption25', 'prefilled_corruption26', 'prefilled_corruption27', 'prefilled_corruption28',
            'prefilled_corruption29', 'prefilled_corruption30',
        ]

        random_apps = random.choice(apps)
        player.name_apps = random_apps

        if player.name_apps == 'prefilled_corruption1':
            player.round = 1
            player.potential_payoff = float(participant.pay_treatment1)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption2':
            player.round = 2
            player.potential_payoff = float(participant.pay_treatment2)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption3':
            player.round = 3
            player.potential_payoff = float(participant.pay_treatment3)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption4':
            player.round = 4
            player.potential_payoff = float(participant.pay_treatment4)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption5':
            player.round = 5
            player.potential_payoff = float(participant.pay_treatment5)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption6':
            player.round = 6
            player.potential_payoff = float(participant.pay_treatment6)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption7':
            player.round = 7
            player.potential_payoff = float(participant.pay_treatment7)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption8':
            player.round = 8
            player.potential_payoff = float(participant.pay_treatment8)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption9':
            player.round = 9
            player.potential_payoff = float(participant.pay_treatment9)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption10':
            player.round = 10
            player.potential_payoff = float(participant.pay_treatment10)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption11':
            player.round = 11
            player.potential_payoff = float(participant.pay_treatment11)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption12':
            player.round = 12
            player.potential_payoff = float(participant.pay_treatment12)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption13':
            player.round = 13
            player.potential_payoff = float(participant.pay_treatment13)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption14':
            player.round = 14
            player.potential_payoff = float(participant.pay_treatment14)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption15':
            player.round = 15
            player.potential_payoff = float(participant.pay_treatment15)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption16':
            player.round = 16
            player.potential_payoff = float(participant.pay_treatment16)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption17':
            player.round = 17
            player.potential_payoff = float(participant.pay_treatment17)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption18':
            player.round = 18
            player.potential_payoff = float(participant.pay_treatment18)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption19':
            player.round = 19
            player.potential_payoff = float(participant.pay_treatment19)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption20':
            player.round = 20
            player.potential_payoff = float(participant.pay_treatment20)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption21':
            player.round = 21
            player.potential_payoff = float(participant.pay_treatment21)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption23':
            player.round = 23
            player.potential_payoff = float(participant.pay_treatment23)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption24':
            player.round = 24
            player.potential_payoff = float(participant.pay_treatment24)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption25':
            player.round = 25
            player.potential_payoff = float(participant.pay_treatment25)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption26':
            player.round = 26
            player.potential_payoff = float(participant.pay_treatment26)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption27':
            player.round = 27
            player.potential_payoff = float(participant.pay_treatment27)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption28':
            player.round = 28
            player.potential_payoff = float(participant.pay_treatment28)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption29':
            player.round = 29
            player.potential_payoff = float(participant.pay_treatment29)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled_corruption30':
            player.round = 30
            player.potential_payoff = float(participant.pay_treatment30)
            player.payoff = player.potential_payoff * 100 + 10000


class Results(Page):
    timeout_seconds = 15


page_sequence = [WaitAllPlayer, MyPage, Results]
