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
    name_in_url = 'pal_exam'
    players_per_group = None
       
       
    num_rounds = 65 # set to same number as number of words
    
    final_exam_accuracy_points=400/num_rounds # points per correct answer

    
    exam_timer = 20*60 # in seconds

    with open('examlist.json') as json_file:
        data = json.load(json_file)
        
    pairs=dict([(x[0],x[1]) for x in data])
    
    words=list(pairs.keys())
    
class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):

    response_time=models.IntegerField()
    
    presented_word=models.CharField()
    correct_match=models.CharField()

    def get_pair(self):
        word=Constants.words[self.round_number-1]
        self.presented_word=word
        self.correct_match=Constants.pairs[word]


    pair_choice=models.CharField()
    
    
    points_cumulative=models.FloatField()

    def SetPoints(self):
        if ("points_cumulative" in self.participant.vars) and ('correct_cumulative' in self.participant.vars):
            self.points_cumulative=self.participant.vars['points_cumulative']
            
            self.participant.vars['correct_cumulative']+=int(self.pair_choice==self.correct_match)
            self.points_cumulative+=Constants.final_exam_accuracy_points*int(self.pair_choice==self.correct_match)
            self.participant.vars['points_cumulative']=self.points_cumulative



