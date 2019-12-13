from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass
    
    
class SchoolTimeWaitPage(Page): 
    def before_next_page(self):
        self.player.get_pair()
        
class schooltime1(Page):
    form_model='player'
    form_fields=['pair_choice']

class schooltime_non_interactive(Page):
    pass


class ResultsWaitPage(WaitPage):
        pass


class Results(Page):
    def after_all_players_arrive(self):
        pass

class SchooltimeResults(Page):
    form_model='player'
    form_fields=['player_choice_final',
        'hovercount1','hovertime1','hover_json1',
        'hovercount2','hovertime2','hover_json2',
        'hovercount3','hovertime3','hover_json3',
        'hovercount4','hovertime4','hover_json4'
    ]

    pass

class HomeTimeChoose(Page):
    form_model='player'
    form_fields=['hometime_choice']

class HomeTimeRest(Page):
    timeout_seconds = 60

class Feedback(Page):
    pass

class Schooltime_feedback_individual(Page):
    pass

class Solitaire(Page):
    pass
    
class Sudoku(Page):
    pass
    
    
# depending on condition, we'll set page_sequence equal to 
# one of the following
sequence_group = [
    SchoolTimeWaitPage,
    schooltime1,
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


