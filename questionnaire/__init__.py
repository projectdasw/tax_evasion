from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'questionnaire'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Demographics Survey
    usia = models.IntegerField(label="Usia Anda (Tahun):",
                               min=18, max=60)
    gender = models.StringField(widget=widgets.RadioSelect,
                                label="Jenis kelamin:",
                                choices=["Pria", "Wanita"])
    educ = models.StringField(widget=widgets.RadioSelect,
                              label="Tingkat Pendidikan yang sedang atau telah Anda tempuh:",
                              choices=["Diploma 3 (D3)",
                                       "Sarjana/Diploma 4 (S1/D4)",
                                       "Magister (S2)",
                                       "Doktoral (S3)",
                                       ])
    actv = models.StringField(widget=widgets.RadioSelect,
                              label="Aktivitas utama Anda saat ini:",
                              choices=["Sekolah/Kuliah",
                                       "Lulus belum bekerja",
                                       "Bekerja",
                                       ])
    tax = models.StringField(widget=widgets.RadioSelect,
                              label="Apakah Anda sudah pernah membayar pajak penghasilan?",
                              choices=["Sudah",
                                       "Belum",
                                       ])
    studi = models.StringField(widget=widgets.RadioSelect,
                               label="Bidang Studi:",
                               choices=["Biologi",
                                        "Farmasi",
                                        "Kedokteran Hewan",
                                        "Matematika dan Ilmu Pengetahuan Alam"
                                        "Teknik & Rekayasa",
                                        "Teknologi Pertanian",
                                        "Studi Sosial, Politik & Hukum"
                                        "Ilmu Budaya & Agama",
                                        "Politik-Hukum",
                                        "Ekonomi-Bisnis",
                                        "Psikologi",
                                        "Geografi",
                                        "Filsafat",
                                        "Medis, Dental & Keperawatan",
                                        "Kehutanan",
                                        "Pertanian & Peternakan",
                                        "Kesehatan Masyarakat"])
    expenditure = models.StringField(widget=widgets.RadioSelect,
                                     label="Rata-rata pengeluaran Setiap Bulan:",
                                     choices=["Di bawah Rp 500.000",
                                              "Rp 500.001 - Rp 1.000.000",
                                              "Rp 1.000.001 - Rp 1.500.000",
                                              "Rp 1.500.001 - Rp 2.000.000",
                                              "Rp 2.000.001 - Rp 2.500.000",
                                              "Rp 2.500.001 - Rp 5.000.000",
                                              "Di atas Rp 5.000.000", ])
    pay = models.StringField(widget=widgets.RadioSelect,
                                label="Metode Pembayaran Online:",
                                choices=["OVO", "GoPay", "ShopeePay", "Bank BNI" ,"Bank Mandiri"])

    wa = models.StringField(label="No HP Online Payment / No. Rekening:",)
    skala = models.StringField(widget=widgets.RadioSelect,
                             label="Seberapa menarik eksperimen ini bagi Anda:",
                             choices=["Tidak Menarik", "Cukup Menarik", "Biasa Saja", "Menarik", "Sangat Menarik"])


# PAGES
class demographic(Page):
    form_model = 'player'
    form_fields = ['usia', 'gender', 'educ', 'actv', 'tax', 'studi', 'expenditure', 'pay', 'wa', 'skala']


page_sequence = [demographic]
