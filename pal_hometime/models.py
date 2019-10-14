from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Your name here'

doc = """
hometime app
"""


class Constants(BaseConstants):
    name_in_url = 'pal_hometime'
    players_per_group = None
    num_rounds = 1000
    pairs={
        "alpha" : "1",
        "bravo":"2",
        "charlie":"3",
        "delta":"4",
        "echo":"5"
    }
    words=list(pairs.keys())
    random.shuffle(words)
    
    home_timer=30 # in minutes





class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    
    homechoose_json=models.CharField()
    
    presented_word=models.CharField()
    correct_match=models.CharField()

    def get_pair(self):
        word=Constants.words[self.round_number]
        self.presented_word=word
        self.correct_match=Constants.pairs[word]

    hometime_choice=models.CharField(
        choices=[
            ["rest","Just rest for the hometime period"],
            ["game","Play a game for the hometime period"],
            ["study","Study the word pairs for the hometime period"]        
        ]
    )

    pair_choice=models.CharField(
        choices=list(Constants.pairs.values())
    )
