from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random, json

author = 'Your name here'

doc = """
hometime app
"""


class Constants(BaseConstants):
    name_in_url = 'pal_hometime'
    players_per_group = None
    num_rounds = 1000

    with open('wordlist.json') as json_file:
        data = json.load(json_file)
        
    pairs=dict([(x[0][0],x[1][0]) for x in data])
    
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

    pair_choice=models.CharField(
        choices=list(Constants.pairs.values())
    )
