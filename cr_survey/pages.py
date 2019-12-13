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
  def before_next_page(self):
    self.player.Page_1_cr=self.player.get_CR_Metric()
 
class Page_1(Page):
  form_model='player'
  form_fields=Constants.Page_1
  def vars_for_template(self):
    return(dict(
      qnames=Constants.Page_1,
      cr_score=None
      ))
  def before_next_page(self):
    self.player.Page_1_cr=self.player.get_CR_Metric()
  
class Page_2(Page):
  form_model='player'
  form_fields=Constants.Page_2
  def vars_for_template(self):
    return(dict(
      qnames=Constants.Page_2,
      cr_score=self.player.Page_1_cr
      ))
  def before_next_page(self):
    self.player.Page_2_cr=self.player.get_CR_Metric()
  
class Page_3(Page):
  form_model='player'
  form_fields=Constants.Page_3
  def vars_for_template(self):
    return(dict(
      qnames=Constants.Page_3,
      cr_score=self.player.Page_2_cr
      ))
  def before_next_page(self):
    self.player.Page_3_cr=self.player.get_CR_Metric()
  
class Page_4(Page):
  form_model='player'
  form_fields=Constants.Page_4
  def vars_for_template(self):
    return(dict(
      qnames=Constants.Page_4,
      cr_score=self.player.Page_3_cr
      ))
  def before_next_page(self):
    self.player.Page_4_cr=self.player.get_CR_Metric()
  
class Page_5(Page):
  form_model='player'
  form_fields=Constants.Page_5
  def vars_for_template(self):
    return(dict(
      qnames=Constants.Page_5,
      cr_score=self.player.Page_4_cr
      ))
  def before_next_page(self):
    self.player.Page_5_cr=self.player.get_CR_Metric()
  
class Page_6(Page):
  form_model='player'
  form_fields=Constants.Page_6
  def vars_for_template(self):
    return(dict(
      qnames=Constants.Page_6,
      cr_score=self.player.Page_5_cr
      ))
  def before_next_page(self):
    self.player.Page_6_cr=self.player.get_CR_Metric()
  
class Page_7(Page):
  form_model='player'
  form_fields=Constants.Page_7
  def vars_for_template(self):
    return(dict(
      qnames=Constants.Page_7,
      cr_score=self.player.Page_6_cr
      ))
  def before_next_page(self):
    self.player.Page_7_cr=self.player.get_CR_Metric()
  
class Page_8(Page):
  form_model='player'
  form_fields=Constants.Page_8
  def vars_for_template(self):
    return(dict(
      qnames=Constants.Page_8,
      cr_score=self.player.Page_7_cr
      ))
  def before_next_page(self):
    self.player.Page_8_cr=self.player.get_CR_Metric()
  
class Page_9(Page):
  form_model='player'
  form_fields=Constants.Page_9
  def vars_for_template(self):
    return(dict(
      qnames=Constants.Page_9,
      cr_score=self.player.Page_8_cr
      ))
  def before_next_page(self):
    self.player.Page_9_cr=self.player.get_CR_Metric()
  
class Page_10(Page):
  form_model='player'
  form_fields=Constants.Page_10
  def vars_for_template(self):
    return(dict(
      qnames=Constants.Page_10,
      cr_score=self.player.Page_9_cr
      ))
  def before_next_page(self):
    self.player.Page_10_cr=self.player.get_CR_Metric()
  
class Page_11(Page):
  form_model='player'
  form_fields=Constants.Page_11
  def vars_for_template(self):
    return(dict(
      qnames=Constants.Page_11,
      cr_score=self.player.Page_10_cr
      ))
  def before_next_page(self):
    self.player.Page_11_cr=self.player.get_CR_Metric()
  
class Page_12(Page):
  form_model='player'
  form_fields=Constants.Page_12
  def vars_for_template(self):
    return(dict(
      qnames=Constants.Page_12,
      cr_score=self.player.Page_11_cr
      ))
  def before_next_page(self):
    self.player.Page_12_cr=self.player.get_CR_Metric()
  
class Page_13(Page):
  form_model='player'
  form_fields=Constants.Page_13
  def vars_for_template(self):
    return(dict(
      qnames=Constants.Page_13,
      cr_score=self.player.Page_12_cr
      ))
  def before_next_page(self):
    self.player.Page_13_cr=self.player.get_CR_Metric()
  
class Page_14(Page):
  form_model='player'
  form_fields=Constants.Page_14
  def vars_for_template(self):
    return(dict(
      qnames=Constants.Page_14,
      cr_score=self.player.Page_13_cr
      ))
  def before_next_page(self):
    self.player.Page_14_cr=self.player.get_CR_Metric()
  
class Page_15(Page):
  form_model='player'
  form_fields=Constants.Page_15
  def vars_for_template(self):
    return(dict(
      qnames=Constants.Page_15,
      cr_score=self.player.Page_14_cr
      ))
  def before_next_page(self):
    self.player.Page_15_cr=self.player.get_CR_Metric()
  
class Page_16(Page):
  form_model='player'
  form_fields=Constants.Page_16
  def vars_for_template(self):
    return(dict(
      qnames=Constants.Page_16,
      cr_score=self.player.Page_15_cr
      ))
  def before_next_page(self):
    self.player.Page_16_cr=self.player.get_CR_Metric()
  
  
page_sequence = [
    Page_1,
    Page_2,
    Page_3,
    Page_4,
    Page_5,
    Page_6,
    Page_7,
    Page_8,
    Page_9,
    Page_10,
    Page_11,
    Page_12,
    Page_13,
    Page_14,
    Page_15,
    Page_16,
]

# page_sequence=[q_test_1]