from otree.api import *
import csv


class C(BaseConstants):
    NAME_IN_URL = 'tax_compliance_practice4'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    subsession.group_randomly()

    prefilled_event = open(__name__ + '/parameter/prefilled_form.csv', encoding='utf-8-sig')
    corrupt_event = open(__name__ + '/parameter/ambiguous_corruption_event.csv', encoding='utf-8-sig')
    audit_event = open(__name__ + '/parameter/audit_event.csv', encoding='utf-8-sig')
    returntax = open(__name__ + '/parameter/return_tax.csv', encoding='utf-8-sig')

    prefilledform = list(csv.DictReader(prefilled_event))
    corrupt = list(csv.DictReader(corrupt_event))
    audit = list(csv.DictReader(audit_event))
    returntax = list(csv.DictReader(returntax))

    players = subsession.get_players()
    for i in range(len(players)):
        prefilled_cols = prefilledform[i]
        corrupt_cols = corrupt[i]
        audit_cols = audit[i]
        returntax_cols = returntax[i]
        player = players[i]
        player.prefilled_form = int(prefilled_cols['112'])
        player.corrupt = int(corrupt_cols['77'])
        player.audit = bool(int(audit_cols['1']))
        player.return_tax = int(returntax_cols['97'])


class Group(BaseGroup):
    lat_totalpajak = models.FloatField(min=0, max=1)
    lat_bagipajak = models.FloatField(min=0, max=1)


class Player(BasePlayer):
    lat_pendapatanakhir = models.FloatField(min=0, max=1)
    lat_laporpendapatan = models.FloatField(label="Masukkan Pendapatan Anda")
    lat_bebanpajak = models.FloatField(min=0, max=1)
    audit = models.BooleanField()
    prefilled_form = models.IntegerField()
    corrupt = models.IntegerField()
    return_tax = models.IntegerField()
    denda = models.FloatField(initial=0)


# FUNCTIONS
def set_jumlahpajak(group: Group):
    players = group.get_players()
    total_pajak = [p.lat_bebanpajak for p in players]
    group.lat_totalpajak = sum(total_pajak)
    group.lat_bagipajak = group.lat_totalpajak / C.PLAYERS_PER_GROUP


# PAGES
class WaitPlayer(WaitPage):
    group_by_arrival_time = True


class BeforeTaxPage(Page):
    timeout_seconds = 15

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        player.lat_pendapatanakhir = participant.total_payoff


class TaxPage(Page):
    timeout_seconds = 20

    form_model = 'player'
    form_fields = ['laporpendapatan']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        hitung_pajak = player.lat_laporpendapatan - 200
        pajak500pertama = 500 * 0.05

        if hitung_pajak <= 500:
            player.lat_bebanpajak = hitung_pajak * 0.05
        if 500 < hitung_pajak <= 1000:
            player.lat_bebanpajak = pajak500pertama + ((hitung_pajak - 500) * 0.15)
        if hitung_pajak > 1000:
            player.lat_bebanpajak = pajak500pertama + ((hitung_pajak - 500) * 0.15) + \
                                    (((hitung_pajak - 500) - 500) * 0.25)


class TotalPajak(WaitPage):
    after_all_players_arrive = set_jumlahpajak


class PooledTax(Page):
    timeout_seconds = 10

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        pres_denda = (player.lat_pendapatanakhir - player.lat_laporpendapatan) * 0.5

        if player.audit == 0:
            if pres_denda == 0:
                player.denda = 0

        if player.denda == 0:
            if pres_denda > 0:
                player.denda = pres_denda

        if player.audit == 1:
            if pres_denda == 0:
                player.denda = 0

        if player.audit == 1:
            if pres_denda > 0:
                player.denda = pres_denda

        player.payoff = (player.lat_laporpendapatan - player.lat_bebanpajak) - player.denda


class FinalResults(Page):
    timeout_seconds = 10


page_sequence = [WaitPlayer, TaxPage, TotalPajak, PooledTax, FinalResults]
