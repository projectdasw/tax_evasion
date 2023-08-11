from os import environ

SESSION_CONFIGS = [
    dict(
        display_name='Eksperimen Perilaku Perpajakan Sesi 1 - No Treatment',
        name='tax_nt',
        app_sequence=['nt_instruction', 'tax_nt_practice', 'BeforeExperiment', 'tax_nt', 'nt_pay_random',
                      'questionnaire', 'payment_info'],
        num_demo_participants=60,
    ),

    dict(
        display_name='Eksperimen Perilaku Perpajakan Sesi 2 - Corruption Treatment',
        name='tax_ct',
        app_sequence=['ct_instruction', 'tax_ct_practice', 'BeforeExperiment', 'tax_ct', 'ct_pay_random',
                      'questionnaire', 'payment_info'],
        num_demo_participants=60,
    ),

    dict(
        display_name='Eksperimen Perilaku Perpajakan Sesi 3 - Prefilled Form Treatment',
        name='tax_pft',
        app_sequence=['pft_instruction', 'tax_pft_practice', 'BeforeExperiment', 'tax_pft', 'pft_pay_random',
                      'questionnaire', 'payment_info'],
        num_demo_participants=60,
    ),

    dict(
        display_name='Eksperimen Perilaku Perpajakan Sesi 4 - Prefilled Form + Corruption Treatment',
        name='tax_pfct',
        app_sequence=['pfct_instruction', 'tax_pfct_practice', 'BeforeExperiment', 'tax_pfct', 'pfct_pay_random',
                      'questionnaire', 'payment_info'],
        num_demo_participants=60,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = [
    'selected_round',
    'laporlebih',
    'nt_payment',
    'ct_payment',
    'pft_payment',
    'pfct_payment'
]

SESSION_FIELDS = [
    'params'
]

ROOMS = [
    dict(
        name="tax_nt",
        display_name="Eksperimen Perilaku Perpajakan Sesi 1 - No Treatment",
        participant_label_file='_rooms/participant_labels.txt',
    ),

    dict(
        name="tax_ct",
        display_name="Eksperimen Perilaku Perpajakan Sesi 2 - Corruption Treatment",
        participant_label_file='_rooms/participant_labels.txt',
    ),

    dict(
        name="tax_pft",
        display_name="Eksperimen Perilaku Perpajakan Sesi 3 - Prefilled Form Treatment",
        participant_label_file='_rooms/participant_labels.txt',
    ),

    dict(
        name="tax_pfct",
        display_name="Eksperimen Perilaku Perpajakan Sesi 4 - Prefilled Form + Corruption Treatment",
        participant_label_file='_rooms/participant_labels.txt',
    )
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
DEBUG = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '5660151362368'
