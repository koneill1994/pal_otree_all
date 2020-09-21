from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import time

class MyPage(Page):
    pass
 
class FinalExamWaitPage(Page):
    def is_displayed(self):
        return self.round_number == 1

 
class exam_start_page(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        # user has 5 minutes to complete as many pages as possible
        self.participant.vars['expiry'] = time.time() + Constants.exam_timer
        if ("points_cumulative" in self.participant.vars) and ('correct_cumulative' in self.participant.vars):
            self.player.points_cumulative=self.participant.vars['points_cumulative']
        self.participant.vars['correct_cumulative']=0
        
class exam_1(Page):
    form_model='player'
    form_fields=['pair_choice','response_time']
    
    timer_text = 'Time remaining to finish the exam'

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()
    def is_displayed(self):
        return self.get_timeout_seconds() > 3
    def vars_for_template(self):
        return dict(
            presented_word=Constants.words[self.round_number-1]
        )
    def before_next_page(self):
        self.player.get_pair()
        self.player.SetPoints()

class Debrief(Page):

    def vars_for_template(self):
        return dict(
            correct=self.participant.vars['correct_cumulative'],
            points_exam=self.participant.vars['correct_cumulative']*Constants.final_exam_accuracy_points,
            points_total=self.participant.vars['points_cumulative']
        )
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    FinalExamWaitPage,
    exam_start_page,
    exam_1,
    Debrief
    ]
