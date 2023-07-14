from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'instruction_experiment2'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    session = subsession.session
    template = dict(
        retry_delay=1.0, puzzle_delay=0, attempts_per_puzzle=1, attempts_per_puzzle_pilot=10, max_math=None,
    )
    session.params = {}
    for param in template:
        session.params[param] = session.config.get(param, template[param])


def creating_session(subsession):
    subsession.group_randomly()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# FUNCTIONS
# PAGES
class WelcomePage(Page):
    pass


class InstructionPage1(Page):
    pass


class InstructionPage2(Page):
    pass


class InstructionPage3(Page):
    pass


class InstructionPage4(Page):
    pass


class InfoPage(Page):
    pass


page_sequence = [WelcomePage, InstructionPage1, InstructionPage2, InstructionPage3, InstructionPage4, InfoPage]
