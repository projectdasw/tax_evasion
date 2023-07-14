from otree.api import *
import csv


class C(BaseConstants):
    NAME_IN_URL = 'tax_compliance1'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    subsession.group_randomly()

    audit_event = open(__name__ + '/parameter/audit_event.csv', encoding='utf-8-sig')
    returntax = open(__name__ + '/parameter/return_tax.csv', encoding='utf-8-sig')

    audit = list(csv.DictReader(audit_event))
    returntax = list(csv.DictReader(returntax))

    players = subsession.get_players()
    for i in range(len(players)):
        audit_cols = audit[i]
        returntax_cols = returntax[i]
        player = players[i]
        player.audit = bool(int(audit_cols['1']))
        player.return_tax = int(returntax_cols['97'])


class Group(BaseGroup):
    totalpajak = models.FloatField(min=0, max=1)
    bagipajak = models.FloatField(min=0, max=1)


class Player(BasePlayer):
    pendapatanakhir = models.FloatField(min=0, max=1)
    laporpendapatan = models.FloatField(label="Masukkan Pendapatan Anda")
    bebanpajak = models.FloatField(min=0, max=1)
    audit = models.BooleanField()
    return_tax = models.IntegerField()
    denda = models.FloatField(initial=0)


# FUNCTIONS
def set_jumlahpajak(group: Group):
    players = group.get_players()
    total_pajak = [p.bebanpajak for p in players]
    group.totalpajak = sum(total_pajak)
    group.bagipajak = group.totalpajak / C.PLAYERS_PER_GROUP


# PAGES
class WaitPlayer(WaitPage):
    group_by_arrival_time = True


class BeforeTaxPage(Page):
    timeout_seconds = 15

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        player.pendapatanakhir = participant.total_payoff


class TaxPage(Page):
    timeout_seconds = 20

    form_model = 'player'
    form_fields = ['laporpendapatan']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        hitung_pajak = player.laporpendapatan - 200
        pajak500pertama = 500 * 0.05

        if hitung_pajak <= 500:
            player.bebanpajak = hitung_pajak * 0.05
        if 500 < hitung_pajak <= 1000:
            player.bebanpajak = pajak500pertama + ((hitung_pajak - 500) * 0.15)
        if hitung_pajak > 1000:
            player.bebanpajak = pajak500pertama + ((hitung_pajak - 500) * 0.15) + \
                                (((hitung_pajak - 500) - 500) * 0.25)


class TotalPajak(WaitPage):
    after_all_players_arrive = set_jumlahpajak


class PooledTax(Page):
    timeout_seconds = 10

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        pres_denda = (player.pendapatanakhir - player.laporpendapatan) * 0.5

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

        player.payoff = (player.laporpendapatan - player.bebanpajak) - player.denda


class FinalResults(Page):
    timeout_seconds = 10


page_sequence = [WaitPlayer, BeforeTaxPage, TaxPage, TotalPajak, PooledTax, FinalResults]
