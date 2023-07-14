from os import environ
import sys

DEBUG = False

SESSION_CONFIGS = [
    dict(
        name="task_math1",
        display_name="Eksperimen Perilaku Perpajakan Sesi 1 - No Treatment",
        num_demo_participants=4,
        app_sequence=["instruction_experiment1", "task_math_practice", "tax_compliance_practice1", "BeforeExperiment",
                      "task_math", "tax_compliance1", "pay_random_round", "payment_info"],
        task='math',
        attempts_per_puzzle=1,
    ),

    dict(
        name="task_math2",
        display_name="Eksperimen Perilaku Perpajakan Sesi 2 - Corruption Treatment",
        num_demo_participants=8,
        app_sequence=["instruction_experiment2", "task_math_practice", "tax_compliance_practice2", "BeforeExperiment",
                      "task_math", "tax_compliance2", "pay_random_round", "payment_info"],
        task='math',
        attempts_per_puzzle=1,
    ),

    dict(
        name="task_math3",
        display_name="Eksperimen Perilaku Perpajakan Sesi 3 - Prefilled Form Treatments",
        num_demo_participants=8,
        app_sequence=["instruction_experiment3", "task_math_practice", "tax_compliance_practice3", "BeforeExperiment",
                      "task_math", "tax_compliance3", "pay_random_round", "payment_info"],
        task='math',
        attempts_per_puzzle=1,
    ),

    dict(
        name="task_math4",
        display_name="Eksperimen Perilaku Perpajakan Sesi 4 - Prefilled Form + Corruption Treatment",
        num_demo_participants=8,
        app_sequence=["instruction_experiment4", "task_math_practice", "tax_compliance_practice4", "BeforeExperiment",
                      "task_math", "tax_compliance4", "pay_random_round", "payment_info"],
        task='math',
        attempts_per_puzzle=1,
    )
]
# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1, participation_fee=1.00, doc=""
)

PARTICIPANT_FIELDS = ['is_dropout',
                      'total_payoff',
                      'payment',
                      'participant_fee',
                      'finalpayment',
                      'selected_round']
SESSION_FIELDS = ['params']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = "en"

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = ""
USE_POINTS = True

ADMIN_USERNAME = "admin"
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get("OTREE_ADMIN_PASSWORD")

DEMO_PAGE_TITLE = "Eksperimen Perilaku Perpajakan"
DEMO_PAGE_INTRO_HTML = """
Selamat Datang di Eksperimen kami. Eksperimen ini diperuntukan penelitian tentang Perilaku Perpajakan.
"""

SECRET_KEY = "2015765205890"

# adjustments for testing
# generating session configs for all varieties of features
if sys.argv[1] == 'test':
    MAX_ITERATIONS = 5
    FREEZE_TIME = 0.1
    TRIAL_PAUSE = 0.2
    TRIAL_TIMEOUT = 0.3

    for task in ['task_math']:
        SESSION_CONFIGS.extend(
            [
                dict(
                    name=f"testing_{task}_defaults",
                    num_demo_participants=1,
                    app_sequence=['task_math'],
                    puzzle_delay=TRIAL_PAUSE,
                    retry_delay=FREEZE_TIME,
                ),
                dict(
                    name=f"testing_{task}_retrying",
                    num_demo_participants=1,
                    app_sequence=['task_math'],
                    puzzle_delay=TRIAL_PAUSE,
                    retry_delay=FREEZE_TIME,
                    attempts_per_puzzle=5,
                ),
                dict(
                    name=f"testing_{task}_limited",
                    num_demo_participants=1,
                    app_sequence=['task_math'],
                    puzzle_delay=TRIAL_PAUSE,
                    retry_delay=FREEZE_TIME,
                    max_iterations=MAX_ITERATIONS,
                )
            ]
        )
