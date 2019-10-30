from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'cr_survey'
    players_per_group = None
    num_rounds = 1
    
    varnames1=["q"+str(x) for x in list(range(0,10))]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    
    def Likert5(q):
      return models.IntegerField(
        verbose_name = q,
        choices=[
          [1,"strongly disagree"],
          [2,"disagree"],
          [3,"neither agree nor disagree"],
          [4,"agree"],
          [5,"strongly agree"]
        ],
        widget=widgets.RadioSelectHorizontal
      )
      
    q0=Likert5("a")
    q1=Likert5("b")
    q2=Likert5("c")
    q3=Likert5("d")
    q4=Likert5("e")
    q5=Likert5("f")
    q6=Likert5("g")
    q7=Likert5("h")
    q8=Likert5("i")
    q9=Likert5("j")
    q10=Likert5("k")
    q11=Likert5("l")
    q12=Likert5("m")
    q13=Likert5("n")
    q14=Likert5("o")
    q15=Likert5("p")
    q16=Likert5("q")
    q17=Likert5("r")
    q18=Likert5("s")
    q19=Likert5("t")
    q20=Likert5("u")
    q21=Likert5("v")
    q22=Likert5("w")
    q23=Likert5("x")
    q24=Likert5("y")
    q25=Likert5("z")

