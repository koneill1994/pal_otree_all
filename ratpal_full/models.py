from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random, json

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'ratpal_full'
    players_per_group = None
    
    
    home_timer=30 # in minutes
    
    max_rounds=100 # should be an arbitrarily large number, theoretical end of ht
    st_rounds=20 # number of words shown to players in schooltime
    pair_rounds=6 # number of times players go through ht/st paired tasks
    
    num_rounds = pair_rounds*2*max_rounds
    

    def is_hometime(self,round_n):
        if round_n%(2*self.max_rounds)<self.max_rounds:
            return True
        return False
        
    def is_schooltime(self,round_n):
        if round_n%(2*self.max_rounds)>=self.max_rounds and round_n%(2*self.max_rounds)<self.st_rounds:
            return True
        return False
        
    def is_hometime_start(self,round_n):
        if round_n%(2*self.max_rounds)==1:
            return True
        return False
    
    
    with open('wordlist.json') as json_file:
        data = json.load(json_file)
        
    pairs=dict([(x[0][0],x[1][0]) for x in data])
    
    words=list(pairs.keys())
    random.shuffle(words)
    
    condition=random.randint(0,2)
    



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    condition=models.IntegerField(initial=Constants.condition)



class Player(BasePlayer):
    
    task=models.CharField()
    
    presented_word=models.CharField()
    correct_match=models.CharField()

    def get_pair(self):
        word=Constants.words[self.round_number]
        self.presented_word=word
        self.correct_match=Constants.pairs[word]

    pair_choice=models.CharField()
    
    player_choice_final=models.CharField()
    
    hovercount=models.IntegerField(default=0)
    hovertime=models.IntegerField(default=0)
    
    hover_json=models.StringField(blank=True)
    
    # i don't like hardcoding it like this
    # but unless you want to interpret a json string
    # in the analysis, this is the cleanest way
    hovercount1=models.IntegerField(default=0)
    hovertime1=models.IntegerField(default=0)
    hovercount2=models.IntegerField(default=0)
    hovertime2=models.IntegerField(default=0)
    hovercount3=models.IntegerField(default=0)
    hovertime3=models.IntegerField(default=0)
    hovercount4=models.IntegerField(default=0)
    hovertime4=models.IntegerField(default=0)

    hover_json1=models.StringField(blank=True)
    hover_json2=models.StringField(blank=True)
    hover_json3=models.StringField(blank=True)
    hover_json4=models.StringField(blank=True)

    homechoose_json=models.CharField()
    
    def evaluate_choice(self):
        return(self.pair_choice==Group.correct_match)
   


