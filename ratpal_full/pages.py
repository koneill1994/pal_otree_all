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
    def before_next_page(self):
        self.player.get_pair()
        
class schooltime1(Page):
    form_model='player'
    form_fields=['pair_choice','confidence_first_answer']
    def get_timeout_seconds(self):
        return Constants.school_submit_timer

class schooltime_guesses(Page):
    form_model='player'
    form_fields=['guess1','confidence1',
                'guess2','confidence2',
                'guess3','confidence3']
    def is_displayed(self):
        return self.player.confidence_first_answer<100

class schooltime_non_interactive(Page):
    pass

class ResultsWaitPage(WaitPage):
    pass

class SchooltimeResults(Page):
    form_model='player'
    form_fields=['player_choice_final','player_choice_final_conf','player_choice_json']
    def before_next_page(self):
        self.group.group_answer=self.group.get_group_answer()

class Instructions1(Page):
    def is_displayed(self):
        return self.round_number==1

class Schooltime_feedback_individual(Page):
    pass
    
class Feedback(Page):
    pass

## hometime

class StartHometime(Page):
    def before_next_page(self):
        self.player.Words_JSON()
    def is_displayed(self):
        return Constants.display_hometime(self.round_number)

class Hometime_one_page(Page):
    form_model='player'
    form_fields=['homechoose_json','hometime_study_json']
    def get_timeout_seconds(self):
        return Constants.home_timer
    def is_displayed(self):
        return Constants.display_hometime(self.round_number)


ht_new= [
    StartHometime,
    Hometime_one_page
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
# page_sequence = ht_new

page_sequence = [ID_input,Instructions1]+ht_new + sequence_conditional[0]


