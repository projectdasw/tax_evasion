from otree.api import *
import random


doc = """
Select a random round for payment
"""


class C(BaseConstants):
    NAME_IN_URL = 'pay_random_apps3'
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
            'prefilled1', 'prefilled2', 'prefilled3', 'prefilled4', 'prefilled5', 'prefilled6',
            'prefilled7', 'prefilled8', 'prefilled9', 'prefilled10', 'prefilled11', 'prefilled12',
            'prefilled13', 'prefilled14', 'prefilled15', 'prefilled16', 'prefilled17', 'prefilled18',
            'prefilled19', 'prefilled20', 'prefilled21', 'prefilled22', 'prefilled23', 'prefilled24',
            'prefilled25', 'prefilled26', 'prefilled27', 'prefilled28', 'prefilled29', 'prefilled30',
        ]

        random_apps = random.choice(apps)
        player.name_apps = random_apps

        if player.name_apps == 'prefilled1':
            player.round = 1
            player.potential_payoff = float(participant.pay_treatment1)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled2':
            player.round = 2
            player.potential_payoff = float(participant.pay_treatment2)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled3':
            player.round = 3
            player.potential_payoff = float(participant.pay_treatment3)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled4':
            player.round = 4
            player.potential_payoff = float(participant.pay_treatment4)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled5':
            player.round = 5
            player.potential_payoff = float(participant.pay_treatment5)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled6':
            player.round = 6
            player.potential_payoff = float(participant.pay_treatment6)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled7':
            player.round = 7
            player.potential_payoff = float(participant.pay_treatment7)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled8':
            player.round = 8
            player.potential_payoff = float(participant.pay_treatment8)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled9':
            player.round = 9
            player.potential_payoff = float(participant.pay_treatment9)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled10':
            player.round = 10
            player.potential_payoff = float(participant.pay_treatment10)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled11':
            player.round = 11
            player.potential_payoff = float(participant.pay_treatment11)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled12':
            player.round = 12
            player.potential_payoff = float(participant.pay_treatment12)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled13':
            player.round = 13
            player.potential_payoff = float(participant.pay_treatment13)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled14':
            player.round = 14
            player.potential_payoff = float(participant.pay_treatment14)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled15':
            player.round = 15
            player.potential_payoff = float(participant.pay_treatment15)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled16':
            player.round = 16
            player.potential_payoff = float(participant.pay_treatment16)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled17':
            player.round = 17
            player.potential_payoff = float(participant.pay_treatment17)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled18':
            player.round = 18
            player.potential_payoff = float(participant.pay_treatment18)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled19':
            player.round = 19
            player.potential_payoff = float(participant.pay_treatment19)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled20':
            player.round = 20
            player.potential_payoff = float(participant.pay_treatment20)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled21':
            player.round = 21
            player.potential_payoff = float(participant.pay_treatment21)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled23':
            player.round = 23
            player.potential_payoff = float(participant.pay_treatment23)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled24':
            player.round = 24
            player.potential_payoff = float(participant.pay_treatment24)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled25':
            player.round = 25
            player.potential_payoff = float(participant.pay_treatment25)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled26':
            player.round = 26
            player.potential_payoff = float(participant.pay_treatment26)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled27':
            player.round = 27
            player.potential_payoff = float(participant.pay_treatment27)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled28':
            player.round = 28
            player.potential_payoff = float(participant.pay_treatment28)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled29':
            player.round = 29
            player.potential_payoff = float(participant.pay_treatment29)
            player.payoff = player.potential_payoff * 100 + 10000
        elif player.name_apps == 'prefilled30':
            player.round = 30
            player.potential_payoff = float(participant.pay_treatment30)
            player.payoff = player.potential_payoff * 100 + 10000


class Results(Page):
    pass


page_sequence = [WaitAllPlayer, MyPage, Results]
