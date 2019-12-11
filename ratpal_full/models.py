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
    
    
    home_timer=1000 # in minutes
    

    schooltime_words=20 # number of words per round in schooltime
    hometime_pages=2
    max_rounds=schooltime_words+hometime_pages 

    pair_rounds=6 # number of times players go through ht/st paired tasks
    
    num_rounds = pair_rounds*max_rounds
    
    
        
    def display_hometime(round_n):
        if (round_n%Constants.max_rounds)<=Constants.hometime_pages:
            return True
        return False
        
    def get_session_number(round_n):
        return int(round_n/Constants.max_rounds)
    
    with open('wordlist.json') as json_file:
        data = json.load(json_file)
        
    pairs=dict([(x[0][0],x[1][0]) for x in data])
    words=list(pairs.keys())
   
    condition=random.randint(0,2)
    
    def arrange_words_for_session(session_n):
        if session_n==0:
            return ([],Constants.words[0:20])
        else:
            return (Constants.arrange_words_for_session(session_n-1)[1][0:5],Constants.words[20+(session_n-1)*15:20+(session_n)*15])
           
    def get_words_for_session(session_n):
        out=[]
        for sublist in Constants.arrange_words_for_session(session_n):
            for word in sublist:
                out.append(word)
        return out



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    condition=models.IntegerField(initial=Constants.condition)
    
    group_answer=models.CharField()
    
    def get_group_answer(self):
        
        # this value determines the minimum confidence value needed
        # to determine a group answer
        # in the case where all 4 players choose different answers
        confidence_cutoff=80
    
        # get lists of answers and confidences
        ans_list=[]
        conf_list=[]
        for p in self.get_players():
            ans_list.append(p.player_choice_final)
            conf_list.append(p.player_choice_final_conf)
        
        # get a dictionary of form {choice: count}
        ans_dict={}
        for ans in ans_list:
            if ans in ans_dict:
                ans_dict[ans]+=1
            else:
                ans_dict[ans]=1

        # determine group answer
        if len(ans_dict)==1: # all chose same answer
            return list(ans_dict.keys())[0] # return that answer
        elif len(ans_dict)==2: # two answers chosen
            m=max(list(ans_dict.values()))
            if m==2: # if 2 and 2, choose randomly
                return list(ans_dict.keys())[random.randint(0,1)]
            else: # if 3 and 1, choose the max
                return max(ans_dict, key=ans_dict.get)
        elif len(ans_dict)==3: # if 2, 1, and 1, choose the max
            return max(ans_dict, key=ans_dict.get)
        else: # all 4 separate answers
            # choose the answer with the highest confidence above the cutoff
            highest_conf=0
            ans_high_conf=""
            for i in range(0,len(conf_list)):
                if conf_list[i]>highest_conf:
                    highest_conf=conf_list[i]
                    ans_high_conf=ans_list[i]
            if highest_conf>=confidence_cutoff:
                return ans_high_conf
            else: # if no answers are high enough confidence, return a failure tag as the group answer
                return "___FAILURE___" # or return None?
                
                


        
        

class Player(BasePlayer):
    
    def UpdateWords(self):
        return(Constants.get_words_for_session(Constants.get_session_number(self.round_number)))
        # return(Constants.get_words_for_session(0))
    
    words_json=models.CharField()
    
    def Words_JSON(self):
        self.words_json=json.dumps(
            [[word.split("/"),Constants.pairs[word]] for word in self.UpdateWords()]
        )
        
    PAL_subject_ID=models.CharField()
    PAL_group_ID=models.CharField()
    
    task=models.CharField()
    
    presented_word=models.CharField()
    correct_match=models.CharField()
    

    def get_pair(self):
        word=self.UpdateWords()[(self.round_number-1)%Constants.max_rounds]
        self.presented_word=word
        self.correct_match=Constants.pairs[word]

    pair_choice=models.CharField()
    confidence_first_answer=models.IntegerField() # represents percentage
    
    guess1=models.CharField(blank=True)
    guess2=models.CharField(blank=True)
    guess3=models.CharField(blank=True)
    
    confidence1=models.IntegerField(blank=True)
    confidence2=models.IntegerField(blank=True)
    confidence3=models.IntegerField(blank=True)
    
    
    player_choice_final=models.CharField()
    player_choice_final_conf=models.IntegerField()
    
    player_choice_json=models.CharField()
    
    homechoose_json=models.CharField()
    hometime_study_json=models.CharField()
    
    def evaluate_choice(self):
        return(self.pair_choice in Group.correct_match.split("/"))
        
    def get_split_words(self):
        return self.presented_word.split("/")
   


