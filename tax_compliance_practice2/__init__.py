from otree.api import *
import csv


class C(BaseConstants):
    NAME_IN_URL = 'tax_compliance_practice2'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for group in self.get_groups():
            group.set_group_bagipajak()


def creating_session(subsession):
    subsession.group_randomly()

    corrupt_event = open(__name__ + '/parameter/ambiguous_corruption_event.csv', encoding='utf-8-sig')
    audit_event = open(__name__ + '/parameter/audit_event.csv', encoding='utf-8-sig')
    lower_return = open(__name__ + '/parameter/lower_return.csv', encoding='utf-8-sig')

    corrupt = list(csv.DictReader(corrupt_event))
    audit = list(csv.DictReader(audit_event))
    returntax = list(csv.DictReader(lower_return))

    players = subsession.get_players()
    for i in range(len(players)):
        corrupt_cols = corrupt[i]
        audit_cols = audit[i]
        returntax_cols = returntax[i]
        player = players[i]
        player.corrupt = float(corrupt_cols['77'])
        player.audit = bool(int(audit_cols['1']))
        player.return_tax = float(returntax_cols['98'])


class Group(BaseGroup):
    lat_totalpajak = models.FloatField(min=0, max=1)
    lat_bagipajak = models.FloatField(min=0, max=1)

    def set_group_bagipajak(self):
        self.group_bagipajak = self.lat_bagipajak


class Player(BasePlayer):
    lat_pendapatanakhir = models.FloatField(min=0, max=1, initial=0)
    lat_laporpendapatan = models.FloatField(label="Masukkan Pendapatan Anda", initial=0)
    lat_bebanpajak = models.FloatField(min=0, max=1, initial=0)
    audit = models.BooleanField()
    corrupt = models.FloatField(min=0, max=1, initial=0)
    return_tax = models.IntegerField(min=0, max=1, initial=0)
    korupsi = models.FloatField(min=0, max=1, initial=0)
    sisa_tidak_korupsi = models.FloatField(min=0, max=1, initial=0)
    denda = models.FloatField(min=0, max=1, initial=0)


# FUNCTIONS
def set_jumlahpajak(group: Group):
    players = group.get_players()
    total_pajak = [p.lat_bebanpajak for p in players]
    for player in players:
        player.korupsi = player.lat_bebanpajak * (player.corrupt / 100)
        player.sisa_tidak_korupsi = player.lat_bebanpajak - float(player.korupsi)
        if player.corrupt > 0:
            group.lat_totalpajak = float(sum(total_pajak))
            group.lat_bagipajak = (group.lat_totalpajak * (player.return_tax / 100)) / C.PLAYERS_PER_GROUP


# PAGES
class WaitPlayer(WaitPage):
    wait_for_all_groups = True


class BeforeTaxPage(Page):
    timeout_seconds = 15

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        player.lat_pendapatanakhir = participant.total_payoff


class TaxPage(Page):
    timeout_seconds = 20

    form_model = 'player'
    form_fields = ['lat_laporpendapatan']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        hitung_pajak = player.lat_laporpendapatan - 200

        if player.lat_laporpendapatan <= 99:
            player.lat_pendapatanakhir = 0
            player.lat_laporpendapatan = 0
            player.lat_bebanpajak = 0
            player.korupsi = 0
            player.sisa_tidak_korupsi = 0
            player.denda = 0

        if player.lat_laporpendapatan == 100:
            player.lat_laporpendapatan = 0
            player.lat_bebanpajak = 0

        if hitung_pajak <= 500:
            player.lat_bebanpajak = hitung_pajak * 0.05
            if 500 < hitung_pajak <= 1000:
                player.lat_bebanpajak = ((hitung_pajak - 500) * 0.05) + ((hitung_pajak - 1000) * 0.15)
                if hitung_pajak > 1000:
                    player.lat_bebanpajak = ((hitung_pajak - 500) * 0.05) + ((hitung_pajak - 1000) * 0.15) + \
                                            ((hitung_pajak - 1500) * 0.25)


class TotalPajak(WaitPage):
    after_all_players_arrive = set_jumlahpajak


class PooledTax(Page):
    timeout_seconds = 10

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        hasilbagipajak = player.group.lat_bagipajak
        pres_denda = player.lat_pendapatanakhir * 0.5

        if player.audit == 1:
            if player.lat_laporpendapatan < player.lat_pendapatanakhir:
                player.denda = pres_denda

        if player.audit == 1:
            if player.lat_laporpendapatan == player.lat_pendapatanakhir:
                player.denda = 0

        if player.audit == 0:
            if player.lat_laporpendapatan < player.lat_pendapatanakhir:
                player.denda = pres_denda

        if player.audit == 0:
            if player.lat_laporpendapatan == player.lat_pendapatanakhir:
                player.denda = 0

        player.payoff = (player.lat_pendapatanakhir - player.sisa_tidak_korupsi) + hasilbagipajak - player.denda


class FinalResults(Page):
    timeout_seconds = 10

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        participant.payment = player.payoff * 100
        participant.participant_fee = 10000
        participant.finalpayment = participant.payment + participant.participant_fee


page_sequence = [WaitPlayer, BeforeTaxPage, TaxPage, TotalPajak, PooledTax, FinalResults]
