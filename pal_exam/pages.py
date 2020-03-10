from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import time

class MyPage(Page):
    pass
    
class exam_start_page(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        # user has 5 minutes to complete as many pages as possible
        self.participant.vars['expiry'] = time.time() + Constants.exam_timer
        self.player.get_pair()

        
class exam_1(Page):
    form_model='player'
    form_fields=['pair_choice','response_time']
    
    timer_text = 'Time remaining to finish the exam'

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()
    def is_displayed(self):
        return self.get_timeout_seconds() > 3
    def before_next_page(self):
        self.player.get_pair()





page_sequence = [
    exam_start_page,
    exam_1
    ]
