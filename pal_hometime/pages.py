from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time



class StartHometime(Page):
    def is_displayed(self):
        return self.round_number == 1
    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + 60*Constants.home_timer


class Hometime_all(Page):
    form_model='player'
    form_fields=['homechoose_json']
    def before_next_page(self):
        self.player.get_pair()
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()
    def is_displayed(self):
        return self.get_timeout_seconds() > 3

        
class schooltime1(Page):
    form_model='player'
    form_fields=['pair_choice']
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()
    def is_displayed(self):
        return self.get_timeout_seconds() > 3


class Schooltime_feedback_individual(Page):
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()
    def is_displayed(self):
        return self.get_timeout_seconds() > 3






page_sequence = [
    StartHometime,
    Hometime_all,
    schooltime1,
    Schooltime_feedback_individual
]
