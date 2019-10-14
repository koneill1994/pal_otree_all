from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'pal_exam'
    players_per_group = None
    num_rounds = 10
    pairs={
        "alpha" : "1",
        "bravo":"2",
        "charlie":"3",
        "delta":"4",
        "echo":"5"
    }
    words=list(pairs.keys())
    random.shuffle(words)
    
class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass



class Player(BasePlayer):

    response_time=models.IntegerField()
    
    presented_word=models.CharField()
    correct_match=models.CharField()

    def get_pair(self):
        word=Constants.words[self.round_number]
        self.presented_word=word
        self.correct_match=Constants.pairs[word]


    pair_choice=models.CharField(
        choices=list(Constants.pairs.values())
    )
    



