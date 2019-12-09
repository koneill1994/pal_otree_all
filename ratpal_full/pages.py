from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time
    
    
    ## schooltime
    
class ID_input(Page):
    form_model='player'
    form_fields=['PAL_subject_ID','PAL_group_ID']
    def is_displayed(self):
        return (self.round_number==1)
    
class SchoolTimeWaitPage(Page): 
    def is_displayed(self):
        return Constants.is_schooltime(self.round_number)
    def before_next_page(self):
        self.player.get_pair()
        self.player.set_task()
        
class schooltime1(Page):
    form_model='player'
    form_fields=['pair_choice','confidence_first_answer']
    def is_displayed(self):
        return Constants.is_schooltime(self.round_number)

class schooltime_guesses(Page):
    form_model='player'
    form_fields=['guess1','confidence1',
                'guess2','confidence2',
                'guess3','confidence3']
    def is_displayed(self):
        return (Constants.is_schooltime(self.round_number) and self.player.confidence_first_answer <100)


class schooltime_non_interactive(Page):
    def is_displayed(self):
        return Constants.is_schooltime(self.round_number)


class ResultsWaitPage(WaitPage):
    def is_displayed(self):
        return Constants.is_schooltime(self.round_number)


class SchooltimeResults(Page):
    form_model='player'
    form_fields=['player_choice_final',
        'hovercount1','hovertime1','hover_json1','click_json1',
        'hovercount2','hovertime2','hover_json2','click_json2',
        'hovercount3','hovertime3','hover_json3','click_json3',
        'hovercount4','hovertime4','hover_json4','click_json4'
    ]
    def is_displayed(self):
        return Constants.is_schooltime(self.round_number)


class Schooltime_feedback_individual(Page):
    def is_displayed(self):
        return Constants.is_schooltime(self.round_number)

class Feedback(Page):
    def is_displayed(self):
        return Constants.is_schooltime(self.round_number)


## hometime

class StartHometime(Page):
    def is_displayed(self):
        return Constants.is_hometime_start(self.round_number)
    def before_next_page(self):
        self.player.set_task()
        self.participant.vars['hometime_start'] = time.time()
        self.participant.vars['expiry'] = self.participant.vars['hometime_start'] + 60*Constants.home_timer


class Hometime_all(Page):
    form_model='player'
    form_fields=['homechoose_json']
    def before_next_page(self):
        self.player.get_pair()
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()
    def is_displayed(self):
        return (self.get_timeout_seconds() > 3) and Constants.is_hometime(self.round_number)
    def vars_for_template(self):
        return dict(
            hometime_start=self.participant.vars['hometime_start']
        )

        
class schooltime_ht(Page):
    form_model='player'
    form_fields=['pair_choice']
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()
    def is_displayed(self):
        return (self.get_timeout_seconds() > 3) and Constants.is_hometime(self.round_number)


class Schooltime_feedback_individual_ht(Page):
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()
    def is_displayed(self):
        return (self.get_timeout_seconds() > 3) and Constants.is_hometime(self.round_number)






ht_sequence = [
    StartHometime,
    Hometime_all,
    schooltime_ht,
    Schooltime_feedback_individual_ht
]
    
# depending on condition, we'll set page_sequence equal to 
# one of the following
sequence_group = [
    SchoolTimeWaitPage,
    schooltime1,
    schooltime_guesses,
    ResultsWaitPage,
    SchooltimeResults,
    Feedback
]

sequence_individual = [
    SchoolTimeWaitPage,
    schooltime1,
    Schooltime_feedback_individual
]

sequence_non_interactive = [
    SchoolTimeWaitPage,
    schooltime_non_interactive
]
#####
sequence_conditional=[sequence_group,sequence_individual,sequence_non_interactive]

# page_sequence = sequence_conditional[Constants.condition]
page_sequence = sequence_conditional[0]

# page_sequence = [ID_input]+ht_sequence + sequence_conditional[0]


