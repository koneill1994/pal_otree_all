from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class q_test_1(Page):
      form_model='player'
      form_fields=Constants.Page_1
      def vars_for_template(self):
          return(dict(
              qnames=Constants.Page_1
          ))
          
class Page_1(Page):
      form_model='player'
      form_fields=Constants.Page_1
      def vars_for_template(self):
          return(dict(
              qnames=Constants.Page_1
          ))
class Page_2(Page):
      form_model='player'
      form_fields=Constants.Page_2
      def vars_for_template(self):
          return(dict(
              qnames=Constants.Page_2
          ))
class Page_3(Page):
      form_model='player'
      form_fields=Constants.Page_3
      def vars_for_template(self):
          return(dict(
              qnames=Constants.Page_3
          ))
class Page_4(Page):
      form_model='player'
      form_fields=Constants.Page_4
      def vars_for_template(self):
          return(dict(
              qnames=Constants.Page_4
          ))
class Page_5(Page):
      form_model='player'
      form_fields=Constants.Page_5
      def vars_for_template(self):
          return(dict(
              qnames=Constants.Page_5
          ))
class Page_6(Page):
      form_model='player'
      form_fields=Constants.Page_6
      def vars_for_template(self):
          return(dict(
              qnames=Constants.Page_6
          ))
class Page_7(Page):
      form_model='player'
      form_fields=Constants.Page_7
      def vars_for_template(self):
          return(dict(
              qnames=Constants.Page_7
          ))
class Page_8(Page):
      form_model='player'
      form_fields=Constants.Page_8
      def vars_for_template(self):
          return(dict(
              qnames=Constants.Page_8
          ))
class Page_9(Page):
      form_model='player'
      form_fields=Constants.Page_9
      def vars_for_template(self):
          return(dict(
              qnames=Constants.Page_9
          ))
class Page_10(Page):
      form_model='player'
      form_fields=Constants.Page_10
      def vars_for_template(self):
          return(dict(
              qnames=Constants.Page_10
          ))
class Page_11(Page):
      form_model='player'
      form_fields=Constants.Page_11
      def vars_for_template(self):
          return(dict(
              qnames=Constants.Page_11
          ))
class Page_12(Page):
      form_model='player'
      form_fields=Constants.Page_12
      def vars_for_template(self):
          return(dict(
              qnames=Constants.Page_12
          ))
class page_13(Page):
      form_model='player'
      form_fields=Constants.page_13
      def vars_for_template(self):
          return(dict(
              qnames=Constants.page_13
          ))
class Page_14(Page):
      form_model='player'
      form_fields=Constants.Page_14
      def vars_for_template(self):
          return(dict(
              qnames=Constants.Page_14
          ))
class Page_15(Page):
      form_model='player'
      form_fields=Constants.Page_15
      def vars_for_template(self):
          return(dict(
              qnames=Constants.Page_15
          ))
class Page_16(Page):
      form_model='player'
      form_fields=Constants.Page_16
      def vars_for_template(self):
          return(dict(
              qnames=Constants.Page_16
          ))



class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    q_test_1
]

# page_sequence = [
    # Page_1,
    # Page_2,
    # Page_3,
    # Page_4,
    # Page_5,
    # Page_6,
    # Page_7,
    # Page_8,
    # Page_9,
    # Page_10,
    # Page_11,
    # Page_12,
    # page_13,
    # Page_14,
    # Page_15,
    # Page_16
# ]
