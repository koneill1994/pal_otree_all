from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class q_test_1(Page):

    # varnames=["q"+str(x) for x in list(range(0,10))]
    # varnames=["q0","q1","q2"]

    form_model='player'
    form_fields=Constants.varnames1
    
    def vars_for_template(self):
        return(dict(
            qnames=Constants.varnames1
        ))



class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    q_test_1
]
