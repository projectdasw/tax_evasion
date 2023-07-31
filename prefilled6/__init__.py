from otree.api import *
import csv
import random


class C(BaseConstants):
    NAME_IN_URL = 'prefilled6'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for group in self.get_groups():
            group.set_group_bagipajak()


def creating_session(subsession: Subsession):
    subsession.group_randomly()

    prefilled_event = open(__name__ + '/parameter/prefilled_form.csv', encoding='utf-8-sig')
    audit_event = open(__name__ + '/parameter/audit_event.csv', encoding='utf-8-sig')
    lower_return = open(__name__ + '/parameter/lower_return.csv', encoding='utf-8-sig')

    prefilledform = list(csv.DictReader(prefilled_event))
    audit = list(csv.DictReader(audit_event))
    returntax = list(csv.DictReader(lower_return))
    random.shuffle(returntax)
    random.shuffle(audit)
    random.shuffle(prefilledform)

    groups = subsession.get_groups()
    for i in range(len(groups)):
        returntax_cols = returntax[i]
        player = groups[i]
        player.return_tax = float(returntax_cols['97'])

    players = subsession.get_players()
    for i in range(len(players)):
        prefilled_cols = prefilledform[i]
        audit_cols = audit[i]
        player = players[i]
        player.prefilled_form = float(prefilled_cols['112'])
        player.audit = bool(int(audit_cols['1']))


class Group(BaseGroup):
    return_tax = models.FloatField(min=0, max=0)
    totalpajak = models.FloatField(min=0, max=1)
    bagipajak = models.FloatField(min=0, max=1)

    def set_group_bagipajak(self):
        self.group_bagipajak = self.bagipajak


class Player(BasePlayer):
    pendapatanakhir = models.FloatField(min=0, max=1, initial=0)
    laporpendapatan = models.FloatField(label="Masukkan Pendapatan Anda", initial=0)
    estimasi_pendapatan = models.FloatField(min=0, max=1, initial=0)
    bebanpajak = models.FloatField(min=0, max=1, initial=0)
    audit = models.BooleanField()
    prefilled_form = models.FloatField(min=0, max=0, initial=0)
    denda = models.FloatField(min=0, max=1, initial=0)


# FUNCTIONS
def set_jumlahpajak(group: Group):
    players = group.get_players()
    total_pajak = [p.bebanpajak for p in players]
    if total_pajak == 0:
        total_pajak = 0.0000001
    group.totalpajak = sum(total_pajak)
    group.bagipajak = (group.totalpajak * (group.return_tax / 100)) / C.PLAYERS_PER_GROUP


# PAGES
class WaitPlayer(WaitPage):
    wait_for_all_groups = True


class BeforeTaxPage(Page):
    timeout_seconds = 10

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        player.pendapatanakhir = participant.total_payoff

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.estimasi_pendapatan = player.pendapatanakhir * (player.prefilled_form / 100)


class TaxPage(Page):
    timeout_seconds = 20

    form_model = 'player'
    form_fields = ['laporpendapatan']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        laporpendapatanbersih = player.laporpendapatan - 200
        laporpendapatanlebih = player.laporpendapatan - player.pendapatanakhir

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
        pres_denda = (player.pendapatanakhir - player.laporpendapatan) * 0.5
        laporpendapatanlebih = player.laporpendapatan - player.pendapatanakhir

        if laporpendapatanlebih > 0 and player.audit == 1:
            player.denda = 0
            player.payoff = player.pendapatanakhir - player.bebanpajak + hasilbagipajak
        elif player.audit == 1:
            player.denda = pres_denda
            player.payoff = player.pendapatanakhir - player.denda - player.bebanpajak + hasilbagipajak
        elif laporpendapatanlebih > 0 and player.audit == 0:
            player.denda = 0
            player.payoff = player.pendapatanakhir - player.bebanpajak + hasilbagipajak
        elif player.audit == 0:
            player.payoff = player.pendapatanakhir - player.bebanpajak + hasilbagipajak


class FinalResults(Page):
    timeout_seconds = 10

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        laporpendapatanlebih = player.laporpendapatan - player.pendapatanakhir
        participant.laporlebih = laporpendapatanlebih

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant

        if player.round_number == C.NUM_ROUNDS:
            random_round = random.randint(1, C.NUM_ROUNDS)
            participant.selected_round = random_round
            player_in_selected_round = player.in_round(random_round)
            participant.pay_treatment6 = player_in_selected_round.payoff


page_sequence = [WaitPlayer, BeforeTaxPage, TaxPage, TotalPajak, PooledTax, FinalResults]
