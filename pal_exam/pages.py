from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass
    
    
class SchoolTimeWaitPage(Page): 
    def before_next_page(self):
        self.player.get_pair()
        
class exam_1(Page):
    form_model='player'
    form_fields=['pair_choice','response_time']



page_sequence = [
    SchoolTimeWaitPage,
    exam_1
    ]
