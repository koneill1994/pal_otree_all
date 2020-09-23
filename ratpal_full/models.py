from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random, json
import pandas as pd
from types import SimpleNamespace

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'ratpal_full'
    players_per_group = None
    
    
    
    
    
    home_timer=4*60 # in seconds
    
    study_timer=10 # in seconds
    
    school_submit_timer = 30 # in seconds
    school_result_timer = 30
    school_guess_timer = 30
    
    schooltime_words=15 # number of words per round in schooltime

    pair_rounds=6 # number of times players go through ht/st paired tasks
    
    num_rounds = pair_rounds*schooltime_words
    
    
    hometime_points=200/6  #points available for each hometime session
    individual_accuracy_points=100/90 # points per correct answer with 15 problems per school session
    group_accuracy_points=300/90 #points per correct answer with 15 problems per school session

    
    
        
    def display_hometime(round_n):
        if (round_n%Constants.schooltime_words)==1:
            return True
        return False
        
    def get_session_number(round_n):
        return int((round_n-1)/Constants.schooltime_words)
    
    # OBSOLETE
    # with open('wordlist.json') as json_file:
        # data = json.load(json_file)
        
    # pairs=dict([(x[0][0],x[1][0]) for x in data])
    # words=list(pairs.keys())
   
   
    with open('wlist.json') as json_file:
        worddata = json.load(json_file)
    
    wordpairs=[]
    
    for session in worddata:
        wordpairs.append([(str(x[0]),str(x[1])) for x in session])

   
    with open('nlist.json') as json_file:
        numdata = json.load(json_file)
    
    numpairs=[]
    
    for session in numdata:
        numpairs.append([(str(x[0]),str(x[1])) for x in session])
   

   
    
    # FOLLOWING IS OBSOLETE
    # make following generalized
    # also its repeating first 5 from first session, pls fix
    # def arrange_words_for_session(session_n):
        # if session_n==0:
            # return ([],Constants.words[0:Constants.schooltime_words])
        # else:
            # return (Constants.arrange_words_for_session(session_n-1)[1][0:5],
                    # Constants.words[
                        # Constants.schooltime_words+(session_n-1)*(Constants.schooltime_words-5):
                            # Constants.schooltime_words+(session_n)*(Constants.schooltime_words-5)
                    # ])
           
    # def get_words_for_session(session_n):
        # out=[]
        # for sublist in Constants.arrange_words_for_session(session_n):
            # for word in sublist:
                # out.append(word)
        # return out

    def get_words_for_session_pregen(session_n):
        return Constants.wordpairs[session_n]
        
        
    # load confederate data 
    # confederate_df=pd.read_csv("confederate_data.csv")
    confederate_df=pd.read_csv("PAL_confederate_test_data.csv")


    # randomly choose three players to be confederates
    confeds=[]
    for i in random.sample(range(0,len(confederate_df["participant.code"])),3):
        confeds.append(confederate_df["participant.code"][i])




class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    
    condition=models.IntegerField(initial=1)
    # group: 0
    # individual: 1
            
    def confederateAnswerLookup(self,df,confeds,i):
        player=Constants.confeds[i]
        id_in_group=[2,3,4][i] # player is id 1, confederates are id's 2,3,4

        row=df[df["participant.code"]==player]
        k="ratpal_full.1.player."

        r2=["pair_choice",
            "confidence_first_answer",
            "guess1",
            "guess2",
            "guess3",
            "confidence1",
            "confidence2",
            "confidence3",
            "player_choice_final",
            "player_choice_final_conf"]

        sel=".".join(["ratpal_full",str(self.round_number),"player"])

        subs=row[[sel+"."+r for r in r2]]
        subs.columns=r2
        d=subs.to_dict("records")[0]
        d["id_in_group"]=id_in_group
        return d

    confederate_answers=models.CharField()
    
    # json.loads(json.dumps(d),object_hook=lambda d: SimpleNamespace(**d))
    
    def setConfederateAnswers(self):
        conf_answers=[]
        for i in [0,1,2]: # index through 3 confederates
            conf_answers.append(
                self.confederateAnswerLookup(Constants.confederate_df, Constants.confeds, i)
            )
        return json.dumps(conf_answers)
    
    def getConfederateObject(self):
        return json.loads(self.confederate_answers,object_hook=lambda d: SimpleNamespace(**d))

    # this won't be called without the waiting page
    def set_condition(self):
        # choose randomly
        # condition=models.IntegerField(initial=Constants.condition)

        # figure out what to do with this

        # choose based on number of players
        if(len(self.get_players())==4):
            self.condition=0 # set as group
        else:
            self.condition=1 #set as individual
        
    
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
        for c in self.getConfederateObject():
            ans_list.append(c.player_choice_final)
            conf_list.append(c.player_choice_final_conf)

        
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
        else:
            # if all different, choose randomly
            return list(ans_dict.keys())[random.randint(0,3)]
            
            
        # else: # all 4 separate answers
            # choose the answer with the highest confidence above the cutoff
            # highest_conf=0
            # ans_high_conf=""
            # for i in range(0,len(conf_list)):
                # if conf_list[i]>highest_conf:
                    # highest_conf=conf_list[i]
                    # ans_high_conf=ans_list[i]
            # if highest_conf>=confidence_cutoff:
                # return ans_high_conf
            # else: # if no answers are high enough confidence, return a failure tag as the group answer
                # return "___FAILURE___" # or return None?
                
                


        
        

class Player(BasePlayer):
    
    # hometime_points=120
    # individual_accuracy_points=1 # points per correct answer
    # group_accuracy_points=3

    points_cumulative=models.FloatField(initial=0)

    time_off_task=models.FloatField()
    
    # [["task",7272],["rest",12842],["task",16125],["rest",20951],["task",24445]]
    # "[[\"task\",7272],[\"rest\",12842],[\"task\",16125],[\"rest\",20951],[\"task\",24445]]"

    def GetTimeOffTask(self):
        # homechoose_json -> time_off_task

        if len(self.homechoose_json)>0:
        
            hometime_list=json.loads(self.homechoose_json)

            # this is the most elegant hack i could think of
            # add in a illusory "task" transition at the end of the task
            # so that we catch the last period before hometime ends
            hometime_list.append(["task",(1000*Constants.home_timer)])

            # we start in "off task" state
            on_task=False
            off_task_sum=0
            start_off_task=0
            for state_change in hometime_list:
                if on_task:
                    if state_change[0]!="task":
                        start_off_task=state_change[1]
                        on_task=False
                else:
                    if state_change[0]=="task":
                        off_task_sum+=state_change[1]-start_off_task
                        on_task=True
                        
            # if hometime_list[-1][0]!="task":
                # off_task_sum+=(1000*Constants.home_timer)-hometime_list[-1][1]
            
            self.time_off_task = off_task_sum
            
        else:
            self.time_off_task=(1000*Constants.home_timer)

                    
    
    def SetPoints(self):
        if(self.round_number>1):
            self.points_cumulative=self.participant.vars['points_cumulative']
        if(Constants.display_hometime(self.round_number)):
            if self.time_off_task==None:
                self.points_cumulative+=Constants.hometime_points
            else:
                self.points_cumulative+=Constants.hometime_points*((self.time_off_task/1000)/Constants.home_timer)
        self.points_cumulative+=Constants.individual_accuracy_points*int(self.player_choice_final==self.correct_match)
        if(self.group.condition==0):
            self.points_cumulative+=Constants.group_accuracy_points*int(self.player_choice_final==self.group.group_answer)
        self.participant.vars['points_cumulative']=self.points_cumulative

    
    # this gives the words for this session
    def UpdateWords(self):
        return(Constants.get_words_for_session_pregen(Constants.get_session_number(self.round_number)))
        #return(Constants.get_words_for_session(Constants.get_session_number(self.round_number)))
        # return(Constants.get_words_for_session(0))
    
    ### remove following?
    words_json=models.CharField()
    
    def Words_JSON(self):
        self.words_json=json.dumps(
            [[word.split("/"),Constants.pairs[word]] for word in self.UpdateWords()]
        )
        
    numwords_json=models.CharField()
        
    def NumWords_JSON(self):
        self.numwords_json=json.dumps(
            [[word,Constants.pairs[word]] for word in self.UpdateWords()]
        )
        
    ###

    ###
        
        
        
    PAL_subject_ID=models.CharField()
    PAL_group_ID=models.CharField()
    
    task=models.CharField()
    
    presented_word=models.CharField()
    correct_match=models.CharField()
    

    def get_pair(self):
        word=self.UpdateWords()[(self.round_number-1)%Constants.schooltime_words]
        self.presented_word=word[0].strip("[]'")
        self.correct_match=word[1].strip("[]'")

        # self.presented_word=word
        # self.correct_match=Constants.pairs[word]

    pair_choice=models.CharField()
    confidence_first_answer=models.IntegerField(initial=0) # represents percentage
    
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
   
    def is_not_blank(self,x):
        if x=="" or x==None:
            return False
        return True
    # questionnaires
    
    age=models.IntegerField(label="Please enter your age",min=18,max=112)
    gender=models.StringField(
        label="Please select the gender you identify as",
        choices=[
            "Male",
            "Female",
            "Non-binary",
            "Prefer not to say"
        ],
        widget=widgets.RadioSelect
    )
    education=models.StringField(
        label="Please select the highest education level you have attained:",
        choices=[
            "high school or below", 
            "1 year of undergraduate college", 
            "2 years of undergraduate college", 
            "3 years of undergraduate college", 
            "4 or more years of undergraduate college", 
            "graduate level college"
        ],
        widget=widgets.RadioSelect
    )

