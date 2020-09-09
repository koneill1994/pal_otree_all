from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time, json
    
    
    ## schooltime
    
class ID_input(Page):
    form_model='player'
    form_fields=['PAL_subject_ID','PAL_group_ID']
    def is_displayed(self):
        return (self.round_number==1)
    
class Demographics(Page):
    form_model='player'
    form_fields=["age","gender","education"]
    def is_displayed(self):
        return (self.round_number==1)
    
class GroupingWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_condition()
    
class SchoolTimeWaitPage(Page): 
    def before_next_page(self):
        self.player.get_pair()
        
        ### rename?
class schooltime1(Page):
    form_model='player'
    form_fields=['pair_choice','confidence_first_answer']
    def get_timeout_seconds(self):
        return Constants.school_submit_timer
    def before_next_page(self):
        self.group.setConfederateAnswers()

class schooltime_guesses(Page):
    form_model='player'
    form_fields=['guess1','confidence1',
                'guess2','confidence2',
                'guess3','confidence3']
    def is_displayed(self):
        return self.player.confidence_first_answer<100
    def get_timeout_seconds(self):
        return Constants.school_guess_timer

class schooltime_non_interactive(Page):
    def is_displayed(self):
        return self.group.condition==2

class ResultsWaitPage(WaitPage):
    def is_displayed(self):
        return self.group.condition==0

class PreResultsPage(Page):
    def is_displayed(self):
        return self.group.condition==0
    def before_next_page(self):
        self.group.group_answer=self.group.get_group_answer()


class SchooltimeResults(Page):
    form_model='player'
    form_fields=['player_choice_final','player_choice_final_conf','player_choice_json']
    def get_timeout_seconds(self):
        return Constants.school_result_timer
    def is_displayed(self):
        return self.group.condition==0
    def before_next_page(self):
        self.player.SetPoints()



class SchooltimeResultsIndividual(Page):
    form_model='player'
    form_fields=['player_choice_final','player_choice_final_conf','player_choice_json']
    def get_timeout_seconds(self):
        return Constants.school_result_timer
    def is_displayed(self):
        return self.group.condition==1
    def before_next_page(self):
        self.player.SetPoints()



class Instructions1(Page):
    def is_displayed(self):
        return self.round_number==1

class Schooltime_feedback_individual(Page):
    def is_displayed(self):
        return self.group.condition==1

    
class Feedback(Page):
    def vars_for_template(self):
        return dict(
            guess1_notblank=self.player.is_not_blank(self.player.guess1),
            is_individual_condition=(self.group.condition==1),
            points_cum=round(self.player.points_cumulative,2),
            accuracy_pt=round(Constants.individual_accuracy_points,2)
        )


# 

## hometime

# remove?
class StartHometime(Page):
    def before_next_page(self):
        self.player.NumWords_JSON()
    def is_displayed(self):
        return Constants.display_hometime(self.round_number)
###

class Hometime_one_page(Page):
    form_model='player'
    form_fields=['homechoose_json','hometime_study_json']
    def get_timeout_seconds(self):
        return Constants.home_timer
    def is_displayed(self):
        return Constants.display_hometime(self.round_number)
    def vars_for_template(self):
        return dict(
            numwords=json.dumps(Constants.numpairs[Constants.get_session_number(self.round_number)]) 
        )
    def before_next_page(self):
        self.player.GetTimeOffTask()
        
# player.get_session_number(self.round_number)


# 0: set as group
# 1: set as individual


ht_new= [
    # StartHometime,
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
    schooltime_guesses,
    SchooltimeResultsIndividual,
    Feedback
]

# this one is not used
sequence_non_interactive = [
    SchoolTimeWaitPage,
    schooltime_non_interactive
]

sequence_all_conditions=[
    SchoolTimeWaitPage,
    schooltime1,
    schooltime_guesses,
    ResultsWaitPage,
    PreResultsPage,
    SchooltimeResults,
    SchooltimeResultsIndividual,
    Feedback
]


#####
# sequence_conditional=sequence_group+sequence_individual # +sequence_non_interactive

# page_sequence = sequence_conditional
# page_sequence = [GroupingWaitPage,Hometime_one_page]
page_sequence = sequence_all_conditions

# full page sequence:
# page_sequence = [ID_input,Demographics,Instructions1,GroupingWaitPage]+ht_new + sequence_all_conditions


