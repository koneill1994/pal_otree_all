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

    ### paste constants code below
    infreq_ans=[5,5,5,5,1,1,5,1,1,5,1,1]
    Page_1=["GO_1", "GO_2", "GO_3", "GO_4", "GO_5", "GO_6", "GO_7", "Ant_1a", "GO_8", "GO_9", "GO_10", "GO_11", "Infreq_1", "GO_12", "GO_13", "Page_1_MLS", "Page_1_Pagetime"]
    Page_2=["F_1", "F_2", "F_3", "Ant_2a", "F_4", "F_5", "F_6", "F_7", "Infreq_2", "F_8", "F_9", "F_10", "Page_2_MLS", "Page_2_Pagetime"]
    Page_3=["WE_1", "WE_2", "WE_3", "WE_4", "Syn_1a", "WE_5", "WE_6", "WE_7", "RI_1", "WE_8", "WE_9", "WE_10", "WE_11", "WE_12", "Infreq_3", "WE_13", "WE_14", "Page_3_MLS", "Page_3_Pagetime"]
    Page_4=["WE_15", "WE_16", "Ant_3a", "WE_17", "WE_18", "WE_19", "WE_20", "Syn_2a", "WE_21", "WE_22", "WE_23", "WE_24", "RI_2", "WE_25", "WE_26", "WE_27", "WE_28", "Page_4_MLS", "Page_4_Pagetime"]
    Page_5=["d_1", "Ant_4a", "d_2", "Syn_3a", "d_3", "d_4", "Ant_5a", "d_5", "Infreq_4", "d_6", "d_7", "RI_3", "d_8", "d_9", "Syn_4a", "d_10", "Page_5_MLS", "Page_5_Pagetime"]
    Page_6=["m_1", "m_2", "Infreq_5", "m_3", "m_4", "m_5", "m_6", "Ant_6a", "m_7", "m_8", "m_9", "m_10", "Ant_1b", "m_11", "m_12", "RI_4", "m_13", "m_14", "Page_6_MLS", "Page_6_Pagetime"]
    Page_7=["Ant_7a", "m_15", "m_16", "m_17", "RI_5", "m_18", "m_19", "m_20", "Infreq_6", "m_21", "m_22", "m_23", "m_24", "Ant_8a", "m_25", "m_26", "m_27", "m_28", "Page_7_MLS", "Page_7_Pagetime"]
    Page_8=["RI_6", "N_1", "C_1", "Ant_9a", "O_1", "E_1", "Infreq_7", "N_2", "C_2", "Syn_5a", "C_3", "C_4", "Syn_6a", "N_3", "E_2", "Syn_7a", "A_1", "Page_8_MLS", "Page_8_Pagetime"]
    Page_9=["RI_7", "A_2", "C_5", "Ant_10a", "O_2", "A_3", "Syn_8a", "N_4", "Ant_11a", "O_3", "Infreq_8", "E_3", "Syn_9a", "C_6", "E_4", "Syn_10a", "E_5", "Page_9_MLS", "Page_9_Pagetime"]
    Page_10=["RI_8", "O_4", "Syn_11a", "A_4", "N_5", "Infreq_9", "O_5", "Syn_1b", "N_6", "A_5", "Ant_9b", "E_6", "Syn_5b", "N_7", "C_7", "Syn_6b", "Infreq_10", "Page_10_MLS", "Page_10_Pagetime"]
    Page_11=["N_8", "Ant_2b", "RI_9", "C_8", "Syn_7b", "E_7", "A_6", "Ant_4b", "A_7", "Infreq_11", "E_8", "O_6", "Syn_2b", "O_7", "Ant_10b", "O_8", "Syn_4b", "Page_11_MLS", "Page_11_Pagetime"]
    Page_12=["N_9", "Ant_11b", "A_8", "C_9", "Syn_8b", "O_9", "Ant_8b", "O_10", "RI_10", "N_10", "C_10", "Syn_3b", "E_9", "Ant_5b", "A_9", "A_10", "Syn_9b", "E_10", "Page_12_MLS", "Page_12_Pagetime"]
    Page_13=["IM_1", "IM_2", "IM_3", "Infreq_12", "IM_4", "IM_5", "Ant_6b", "IM_6", "IM_7", "IM_8", "Syn_10b", "IM_9", "IM_10", "IM_11", "Page_13_MLS", "Page_13_Pagetime"]
    Page_14=["IM_12", "Ant_7b", "IM_13", "IM_14", "RI_11", "IM_15", "IM_16", "Syn_11b", "IM_17", "IM_18", "IM_19", "IM_20", "Ant_3b", "IM_21", "Page_14_MLS", "Page_14_Pagetime"]
    Page_15=["RIR_1", "RIR_2", "RIR_3", "RIR_4", "RIR_6", "RIR_5", "RIR_7", "RIR_8", "RIR_9", "RIR_10", "RIR_11", "Page_15_MLS", "Page_15_Pagetime"]
    Page_16=["Age", "Gender", "Page_16_MLS", "Page_16_Pagetime"]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    
    def Likert5(q):
      return models.IntegerField(
        verbose_name = q,
        choices=[
          [1,"Strongly Disagree"],
          [2,"Disagree"],
          [3,"Neither Agree Nor Disagree"],
          [4,"Agree"],
          [5,"Strongly Agree"]
        ],
        widget=widgets.RadioSelectHorizontal
      )

    def Likert7(q):
      return models.IntegerField(
        verbose_name = q,
        choices=[
          [1,"Strongly Disagree"],
          [2,"Moderatly Disagree"],
          [3,"Slightly Disagree"],
          [4,"Neither Diasgree nor Agree"],
          [5,"Slightly Agree"],
          [6,"Moderately Agree"],
          [7,"Strongly Agree"]
        ],
        widget=widgets.RadioSelectHorizontal
      )

    def GoalOrientation(q):
      return models.IntegerField(
        verbose_name = q,
        choices=[
          [1,"Strongly Disagree"],
          [2,"Moderately Disagree"],
          [3,"Slightly Disagree"],
          [4,"Slightly Agree"],
          [5,"Moderately Agree"],
          [6,"Strongly Agree"]
        ],
        widget=widgets.RadioSelectHorizontal
      )

    def Big5(q):
      return models.IntegerField(
        verbose_name = q,
        choices=[
          [1,"Very Innacurate"],
          [2,"Moderately Inaccurate"],
          [3,"Niether Inaccurate nor Accurate"],
          [4,"Moderately Accurate"],
          [5,"Very Accurate"]
        ],
        widget=widgets.RadioSelectHorizontal
      )
      
    def RIR_items(q,responses):
        c=[]
        for r in range(0,len(responses)):
            c.append( [r+1,responses[r]] )
        return models.IntegerField(
            verbose_name=q,
            choices=c,
            widget=widgets.RadioSelectHorizontal        
        )
      
    def div_z(self,a,b):
        if a==0 & b==0:
            return 0
        return a/b

      
    def StringInput(q):
        return models.StringField(
            verbose_name = q,
            blank=True
          )
          
    def IterateMLS(self,var,sum,count):
        if(var!=None):
            return((sum+int(var),count+1))
        return(sum,count)
        
    def IteratePageTime(self,var,n_q,sum,count):
        if(var!=None):
            return((sum+int(float(var)>2*n_q),count+1))
        return(sum,count)
            
    def IterateSyn(self,var1,var2,s,c):
        if var1!=None and var2!=None:
            return((s+int(var1==var2),c+1))
        return((s,c))
        
    def IterateAnt(self,var1,var2,s,c):
        if var1!=None and var2!=None:
            return((s+int(var1!=var2),c+1))
        return((s,c))       
     
    def IterateInfreq(self,var,ans,sum,count):
        if(var!=None):
            return((sum+int(var==ans),count+1))
        return(sum,count)
     
    '''
          
     
    def checkMaxLongString():
        mls_sum=0
        mls_count=0
        (mls_sum,mls_count)=IterateMLS(Page_1_MLS,mls_sum,mls_count)
        return mls_sum/mls_count

        
    def checkPageTime():
        s=0
        c=0
        (s,c)=IteratePageTime(Page_1_Pagetime,len(Constants.Page_1),s,c)
        # calculated as 2*number of questions is the cutoff where more than this time indicates “good quality” and less time is careless.
        return s/c
          
    def checkInfreq():
        infreq_sum=0
        infreq_count=0
        if Infreq_1!=None:
            infreq_count+=1
            infreq_sum+=int(Infreq_1==x) # replace x with whatever the right answer is supposed to be
            # repeat the top 2 lines for each of the infrequency items
        return infreq_sum/infreq_count
            
    def checkSynonym():
        syn_sum=0
        syn_count=0
        if Syn_1a!=None and Syn_1b!=None:
            syn_count+=1
            syn_sum+=int(Syn_1a==Syn_1b)
            # repeat via script for each of the synonyms
        return syn_sum/syn_count

    def checkAntonym():
        ant_sum=0
        ant_count=0
        if Ant_1a!=None and Ant_1b!=None:
            ant_count+=1
            ant_sum+=int(Ant_1a!=Ant_1b)
            # repeat via script for each of the synonyms
        return ant_sum/ant_count
        

        
    def update_cr(cr):
        cr=get_CR_Metric()
        
    Page_1_cr=FloatField()

    RIR_items(q,responses)

    # to get the current value of the careless responding metric
    # take the weighted sum of the component metrics
    
    # we gotta work out the specifics of the algorithm
    '''
      
    current_cr=models.FloatField()
      
    def get_CR_Metric(self):
        weights=[1]*5
        metrics=[
            self.checkMaxLongString(),
            self.checkPageTime(),
            self.checkInfreq(),
            self.checkSynonym(),
            self.checkAntonym()
        ]
        weight_sum=0
        for n in range(0,len(metrics)):
            weight_sum+=metrics[n]*weights[n]
        return weight_sum
      
    ### paste player variables code below
    GO_1=GoalOrientation("I am willing to select a challenging class assignment that I can learn a lot from.")
    GO_2=GoalOrientation("I often look for opportunities to develop new skills and knowledge.")
    GO_3=GoalOrientation("I enjoy challenging and difficult tasks at class where I'll learn new skills.")
    GO_4=GoalOrientation("For me, development of my academic ability is important enough to take risks.")
    GO_5=GoalOrientation("I prefer to work in situations that require a high level of ability and talent.")
    GO_6=GoalOrientation("I'm concerned with showing that I can perform better than my classmates.")
    GO_7=GoalOrientation("I try to figure out what it takes to prove my ability to others in class.")
    Ant_1a=Likert5("I arrive on time to meetings.")
    GO_8=GoalOrientation("I enjoy it when others in class are aware of how well I am doing.")
    GO_9=GoalOrientation("I prefer to work on projects where I can prove my ability to others.")
    GO_10=GoalOrientation("I would avoid taking on a new task if there was a chance I would appear rather incompetent to others.")
    GO_11=GoalOrientation("Avoiding a show of low ability is more important to me than learning a new skill.")
    Infreq_1=Likert5("I look forward to my time off.")
    GO_12=GoalOrientation("I'm concerned about taking on a task in class if my performance would reveal that I had low ability.")
    GO_13=GoalOrientation("I prefer to avoid situations in class where I might perform poorly.")
    F_1=GoalOrientation("Would never take things that aren't mine.")
    F_2=GoalOrientation("Would never cheat on my taxes.")
    F_3=GoalOrientation("Return extra change when a cashier makes a mistake.")
    Ant_2a=Likert5("I believe people lie often.")
    F_4=GoalOrientation("Would feel very badly for a long time if I were to steal from someone.")
    F_5=GoalOrientation("Try to follow the rules.")
    F_6=GoalOrientation("Admire a really clever scam.")
    F_7=GoalOrientation("Cheat to get ahead.")
    Infreq_2=Likert5("I don't like getting speeding tickets.")
    F_8=GoalOrientation("Steal things.")
    F_9=GoalOrientation("Cheat on people who have trusted me.")
    F_10=GoalOrientation("Would not regret my behavior if I were to take advantage of someone impulsively.")
    WE_1=Likert5("It is important to stay busy at work and not waste time. ")
    WE_2=Likert5("I feel content when I have spent the day working. ")
    WE_3=Likert5("One should always take responsibility for one's actions. ")
    WE_4=Likert5("I would prefer a job that allowed me to have more leisure time.")
    Syn_1a=Likert5("I am an active person.")
    WE_5=Likert5("Time should not be wasted, it should be used efficiently. ")
    WE_6=Likert5("I get more fulfillment from items I had to wait for. ")
    WE_7=Likert5("A hard day's work is very fulfilling.")
    RI_1=Likert5("Enjoy listening to classical music.")
    WE_8=Likert5("Things that you have to wait for are the most worthwhile.")
    WE_9=Likert5("Working hard is the key to being successful. ")
    WE_10=Likert5("Self-reliance is the key to being successful. ")
    WE_11=Likert5("If one works hard enough, one is likely to make a good life for oneself.")
    WE_12=Likert5("I constantly look for ways to productively use my time. ")
    Infreq_3=Likert5("I have never felt tired or sleepy in my lifetime. ")
    WE_13=Likert5("One should not pass judgment until one has heard all of the facts.")
    WE_14=Likert5("People would be better off if they depended on themselves")
    WE_15=Likert5("A distant reward is usually more satisfying than an immediate one.")
    WE_16=Likert5("More leisure time is good for people.")
    Ant_3a=Likert5("I don't mind waiting in heavy traffic.")
    WE_17=Likert5("I try to plan out my workday so as not to waste time. ")
    WE_18=Likert5("The world would be a better place if people spent more time relaxing.")
    WE_19=Likert5("I strive to be self-reliant. ")
    WE_20=Likert5("If you work hard you will succeed.")
    Syn_2a=Likert5("It frustrates me when people keep me waiting.")
    WE_21=Likert5("The best things in life are those you have to wait for. ")
    WE_22=Likert5("Anyone who is able and willing to work hard has a good chance of succeeding.")
    WE_23=Likert5("It is important to treat others as you would like to be treated. ")
    WE_24=Likert5("I experience a sense of fulfillment from working.")
    RI_2=Likert5("Would like to go skydiving.")
    WE_25=Likert5("People should have more leisure time to spend in relaxation. ")
    WE_26=Likert5("It is important to control one's destiny by not being dependent on others.")
    WE_27=Likert5("People should be fair in their dealings with others. ")
    WE_28=Likert5("A hard day's work provides a sense of accomplishment.")
    d_1=Likert5("Choose my words with care.")
    Ant_4a=Likert5("I am a forgiving person.")
    d_2=Likert5("Take care of my own affairs.")
    Syn_3a=Likert5("I am a very considerate person.")
    d_3=Likert5("Remain calm under pressure.")
    d_4=Likert5("Easily resist temptations.")
    Ant_5a=Likert5("I exercise on a regular basis.")
    d_5=Likert5("Jump into things without thinking.")
    Infreq_4=Likert5("It feels good to be appreciated.")
    d_6=Likert5("Make rash decisions.")
    d_7=Likert5("Like to act on a whim.")
    RI_3=Likert5("Would be happy spending an afternoon at an art museum.")
    d_8=Likert5("Rush into things.")
    d_9=Likert5("Don't know why I do some of the things I do.")
    Syn_4a=Likert5("I spend most of my time worrying.")
    d_10=Likert5("Act quickly without thinking.")
    m_1=Likert5("I have little confidence in my memory generally")
    m_2=Likert5("I have doubts about my memory.")
    Infreq_5=Likert5("I have never used a computer.")
    m_3=Likert5("I have a poor memory.")
    m_4=Likert5("I am never certain about my memory")
    m_5=Likert5("I never do well at memory tests")
    m_6=Likert5("I often feel that my memory misleads me.")
    Ant_6a=Likert5("I often read books for fun.")
    m_7=Likert5("I have little confidence in my memory for actions")
    m_8=Likert5("I often doubt my memory for having completed tasks.")
    m_9=Likert5("I have little confidence in my ability to remember how I performed on particular tasks")
    m_10=Likert5("I have little confidence in my ability to remember what I did in particular situations.")
    Ant_1b=Likert5("I am often late to my appointments. ")
    m_11=Likert5("My memory can mislead me at times.")
    m_12=Likert5("I have little confidence in my memory for words and names")
    RI_4=Likert5("Believe that I could have a satisfying career working as a librarian.")
    m_13=Likert5("I often doubt my memory for having done things properly.")
    m_14=Likert5("I try so hard to remember things, that I end up forgetting everything")
    Ant_7a=Likert5("Almost nothing embarrasses me.")
    m_15=Likert5("I have difficulty knowing if I have actually done something, or imagined it")
    m_16=Likert5("I have doubts about my decision-making ability.")
    m_17=Likert5("I have little confidence in my decision-making.")
    RI_5=Likert5("Think stamp collecting would be a fun hobby.")
    m_18=Likert5("I don't feel that I make good decisions.")
    m_19=Likert5("I find it difficult to making decisions on the spot")
    m_20=Likert5("I experience many doubts after making a decision.")
    Infreq_6=Likert5("I have never brushed my teeth.")
    m_21=Likert5("I am easily distracted.")
    m_22=Likert5("I have a poor concentration ability.")
    m_23=Likert5("I have difficulty keeping my mind focused on one task until it is completed.")
    m_24=Likert5("My poor concentration interferes with my ability to plan things effectively.")
    Ant_8a=Likert5("I enjoy small talk.")
    m_25=Likert5("I put a lot of pressure on myself to do well on even small tasks.")
    m_26=Likert5("I must perform tasks perfectly")
    m_27=Likert5("I expect myself to be 100% certain about the way I plan things.")
    m_28=Likert5("I expect myself to be 100% certain about my decisions.")
    RI_6=Likert5("Like the taste of Brussels sprouts.")
    N_1=Big5("Rarely get irritated. ")
    C_1=Big5("Get chores done right away. ")
    Ant_9a=Likert5("I like to try new foods.")
    O_1=Big5("Carry the conversation to a higher level. ")
    E_1=Big5("Am the life of the party. ")
    Infreq_7=Likert5("I am using an electronic device currently.")
    N_2=Big5("Panic easily. ")
    C_2=Big5("Find it difficult to get down to work. ")
    Syn_5a=Likert5("I enjoy the company of my friends.")
    C_3=Big5("Carry out my plans. ")
    C_4=Big5("Pay attention to details. ")
    Syn_6a=Likert5("I enjoy relaxing in my free time.")
    N_3=Big5("Often feel blue. ")
    E_2=Big5("Know how to captivate people. ")
    Syn_7a=Likert5("I am a very energetic person.")
    A_1=Big5("Suspect hidden motives in others.")
    RI_7=Likert5("Would be impatient if I had to wait in line at an amusement park.")
    A_2=Big5("Have a sharp tongue. ")
    C_5=Big5("Shirk my duties. ")
    Ant_10a=Likert5("I am interested in politics.")
    O_2=Big5("Avoid philosophical discussions. ")
    A_3=Big5("Make people feel at ease. ")
    Syn_8a=Likert5("I find it easy to open up to my friends.")
    N_4=Big5("Am often down in the dumps. ")
    Ant_11a=Likert5("I am proud of my country.")
    O_3=Big5("Am not interested in abstract ideas. ")
    Infreq_8=Likert5("I have been to every country in the world.")
    E_3=Big5("Don't talk a lot. ")
    Syn_9a=Likert5("Occasionally people annoy me.")
    C_6=Big5("Make plans and stick to them. ")
    E_4=Big5("Have little to say.")
    Syn_10a=Likert5("I am a happy person.")
    E_5=Big5("Keep in the background. ")
    RI_8=Likert5("If my friends dared me to eat a live goldfish, I would probably do it.")
    O_4=Big5("Believe in the importance of art. ")
    Syn_11a=Likert5("I am a lively person.")
    A_4=Big5("Get back at others. ")
    N_5=Big5("Seldom feel blue. ")
    Infreq_9=Likert5("I sleep less than one hour per night.")
    O_5=Big5("Have a vivid imagination ")
    Syn_1b=Likert5("I have an active lifestyle.")
    N_6=Big5("Dislike myself. ")
    A_5=Big5("Insult people. ")
    Ant_9b=Likert5("I avoid unfamiliar foods.")
    E_6=Big5("Am skilled in handling social situations. ")
    Syn_5b=Likert5("I like to spend time with my friends")
    N_7=Big5("Am very pleased with myself. ")
    C_7=Big5("Waste my time.")
    Syn_6b=Likert5("In my time off I like to relax.")
    Infreq_10=Likert5("I would be happy if I won the lottery.")
    N_8=Big5("Am not easily bothered by things. ")
    Ant_2b=Likert5("I think people usually tell the truth.")
    RI_9=Likert5("Have had a recurring dream in which all my teeth have fallen out.")
    C_8=Big5("Do just enough work to get by. ")
    Syn_7b=Likert5("I have a lot of energy.")
    E_7=Big5("Make friends easily. ")
    A_6=Big5("Respect others. ")
    Ant_4b=Likert5("I hold a grudge when people hurt me. ")
    A_7=Big5("Accept people as they are. ")
    Infreq_11=Likert5("I can teleport across time and space.")
    E_8=Big5("Feel comfortable around people. ")
    O_6=Big5("Enjoy hearing new ideas. ")
    Syn_2b=Likert5("It's annoying when people are late.")
    O_7=Big5("Tend to vote for conservative political candidates. ")
    Ant_10b=Likert5("I am not interested in politics.")
    O_8=Big5("Tend to vote for liberal political candidates")
    Syn_4b=Likert5("I worry about things a lot.")
    N_9=Big5("Feel comfortable with myself. ")
    Ant_11b=Likert5("I am not patriotic.")
    A_8=Big5("Believe that others have good intentions. ")
    C_9=Big5("Am always prepared. ")
    Syn_8b=Likert5("It's easy for me to confide in my friends.")
    O_9=Big5("Do not like art. ")
    Ant_8b=Likert5("I dislike small talk.")
    O_10=Big5("Do not enjoy going to art museums. ")
    RI_10=Likert5("Would enjoy living in Alaska during the wintertime.")
    N_10=Big5("Have frequent mood swings. ")
    C_10=Big5("Don't see things through. ")
    Syn_3b=Likert5("I always try to be considerate of other people.")
    E_9=Big5("Would describe my experiences as somewhat dull. ")
    Ant_5b=Likert5("I seldom exercise.")
    A_9=Big5("Have a good word for everyone.")
    A_10=Big5("Cut others to pieces. ")
    Syn_9b=Likert5("Sometimes I find people irritating.")
    E_10=Big5("Don't like to draw attention to myself. ")
    IM_1=Likert7("I enjoy participating in this task very much.")
    IM_2=Likert7("I think I am pretty good at this task.")
    IM_3=Likert7("I put a lot of effort into this task.")
    Infreq_12=Likert5("I enjoy receiving telemarketer's calls.")
    IM_4=Likert7("I do not feel nervous at all while participating on this task.")
    IM_5=Likert7("This task is fun to do.")
    Ant_6b=Likert5("I avoid reading when I can.")
    IM_6=Likert7("I think I do pretty well on this task, compared to other students.")
    IM_7=Likert7("I haven't tried very hard on this task.")
    IM_8=Likert7("I feel very tense while participating on this task.")
    Syn_10b=Likert5("I am usually happy.")
    IM_9=Likert7("I haven't really had a choice about participating on this task. ")
    IM_10=Likert7("I think this task is boring.")
    IM_11=Likert7("I try very hard on this task.")
    IM_12=Likert7("I am very relaxed in performing this task.")
    Ant_7b=Likert5("I am easily embarrassed.")
    IM_13=Likert7("I feel like I have to participate on this task. ")
    IM_14=Likert7("This task does not hold my attention at all. ")
    RI_11=Likert5("Have a fear of spiders.")
    IM_15=Likert7("I would describe this task as very interesting.")
    IM_16=Likert7("I am pretty skilled at performing this task.")
    Syn_11b=Likert5("I tend to be pretty lively.")
    IM_17=Likert7("I haven't put much energy into this task. ")
    IM_18=Likert7("I feel pressured during participation in this task.")
    IM_19=Likert7("I think this task is quite enjoyable.")
    IM_20=Likert7("While participating on this task, I think about how much I enjoy it.")
    Ant_3b=Likert5("I become impatient when waiting in heavy traffic.")
    IM_21=Likert7("I participate in this task because I have no other choice. ")
    Age=StringInput("What year were you born?")
    Gender=StringInput("What is your gender?")
    Page_1_MLS=StringInput("Page_1_MLS")
    Page_1_Pagetime=StringInput("Page_1_Pagetime")
    Page_1_cr=models.FloatField()
    Page_2_MLS=StringInput("Page_2_MLS")
    Page_2_Pagetime=StringInput("Page_2_Pagetime")
    Page_2_cr=models.FloatField()
    Page_3_MLS=StringInput("Page_3_MLS")
    Page_3_Pagetime=StringInput("Page_3_Pagetime")
    Page_3_cr=models.FloatField()
    Page_4_MLS=StringInput("Page_4_MLS")
    Page_4_Pagetime=StringInput("Page_4_Pagetime")
    Page_4_cr=models.FloatField()
    Page_5_MLS=StringInput("Page_5_MLS")
    Page_5_Pagetime=StringInput("Page_5_Pagetime")
    Page_5_cr=models.FloatField()
    Page_6_MLS=StringInput("Page_6_MLS")
    Page_6_Pagetime=StringInput("Page_6_Pagetime")
    Page_6_cr=models.FloatField()
    Page_7_MLS=StringInput("Page_7_MLS")
    Page_7_Pagetime=StringInput("Page_7_Pagetime")
    Page_7_cr=models.FloatField()
    Page_8_MLS=StringInput("Page_8_MLS")
    Page_8_Pagetime=StringInput("Page_8_Pagetime")
    Page_8_cr=models.FloatField()
    Page_9_MLS=StringInput("Page_9_MLS")
    Page_9_Pagetime=StringInput("Page_9_Pagetime")
    Page_9_cr=models.FloatField()
    Page_10_MLS=StringInput("Page_10_MLS")
    Page_10_Pagetime=StringInput("Page_10_Pagetime")
    Page_10_cr=models.FloatField()
    Page_11_MLS=StringInput("Page_11_MLS")
    Page_11_Pagetime=StringInput("Page_11_Pagetime")
    Page_11_cr=models.FloatField()
    Page_12_MLS=StringInput("Page_12_MLS")
    Page_12_Pagetime=StringInput("Page_12_Pagetime")
    Page_12_cr=models.FloatField()
    Page_13_MLS=StringInput("Page_13_MLS")
    Page_13_Pagetime=StringInput("Page_13_Pagetime")
    Page_13_cr=models.FloatField()
    Page_14_MLS=StringInput("Page_14_MLS")
    Page_14_Pagetime=StringInput("Page_14_Pagetime")
    Page_14_cr=models.FloatField()
    Page_15_MLS=StringInput("Page_15_MLS")
    Page_15_Pagetime=StringInput("Page_15_Pagetime")
    Page_15_cr=models.FloatField()
    Page_16_MLS=StringInput("Page_16_MLS")
    Page_16_Pagetime=StringInput("Page_16_Pagetime")
    Page_16_cr=models.FloatField()
    RIR_1=RIR_items("Which of the following occupations were you asked about earlier in this questionnaire?",["Lawyer", "Physician", "Veterinarian", "Librarian"])
    RIR_2=RIR_items("Which type of music were you asked about earlier in this questionnaire?",["Rap", "Classical", "Rock", "Country"])
    RIR_3=RIR_items("Which of the following \"extreme\" sports were you asked about earlier in this questionnaire?",["Skydiving", "Hang gliding", "Scuba diving", "Bungee jumping"])
    RIR_4=RIR_items("Which of the following vegetables were you asked about earlier in this questionnaire?",["Carrots", "Brussel sprouts", "Spinach", "Corn"])
    RIR_6=RIR_items("Which U.S. State were you asked about earlier in this questionnaire?",["California", "Hawaii", "Alaska", "Texas"])
    RIR_5=RIR_items("Which of the following hobbies were you asked about earlier in this questionnaire?",["Photography", "Woodworking", "Gardening", "Stamp collecting"])
    RIR_7=RIR_items("Earlier in this questionnaire, we asked you about eating _______ as part of a dare.",["A plate of hot peppers", "A plate of crickets", "A live goldfish", "An earth worm"])
    RIR_8=RIR_items("Earlier in the questionnaire, we asked you if you had experienced a recurring dream about _________.",["Being able to fly", "Having your teeth fall out", "Being naked in public", "Winning the lottery"])
    RIR_9=RIR_items("Earlier in the questionnaire, we asked you whether you had a fear of __________.",["Spiders", "Dogs", "Thunderstorms", "Heights"])
    RIR_10=RIR_items("Earlier in the questionnaire, we asked you whether you would like to spend an afternoon at _________.",["A flea market", "A city park", "An art museum", "An antique store"])
    RIR_11=RIR_items("Earlier in the questionnaire, we asked you whether you would be impatient if you had to wait in line at ___________.",["A public restroom", "The grocery store", "A restaurant", "An amusement park ride"])

    def checkMaxLongString(self):
      s=0
      c=0
      (s,c)=self.IterateMLS(self.Page_1_MLS,s,c)
      (s,c)=self.IterateMLS(self.Page_2_MLS,s,c)
      (s,c)=self.IterateMLS(self.Page_3_MLS,s,c)
      (s,c)=self.IterateMLS(self.Page_4_MLS,s,c)
      (s,c)=self.IterateMLS(self.Page_5_MLS,s,c)
      (s,c)=self.IterateMLS(self.Page_6_MLS,s,c)
      (s,c)=self.IterateMLS(self.Page_7_MLS,s,c)
      (s,c)=self.IterateMLS(self.Page_8_MLS,s,c)
      (s,c)=self.IterateMLS(self.Page_9_MLS,s,c)
      (s,c)=self.IterateMLS(self.Page_10_MLS,s,c)
      (s,c)=self.IterateMLS(self.Page_11_MLS,s,c)
      (s,c)=self.IterateMLS(self.Page_12_MLS,s,c)
      (s,c)=self.IterateMLS(self.Page_13_MLS,s,c)
      (s,c)=self.IterateMLS(self.Page_14_MLS,s,c)
      (s,c)=self.IterateMLS(self.Page_15_MLS,s,c)
      (s,c)=self.IterateMLS(self.Page_16_MLS,s,c)
      return self.div_z(s,c)

    def checkPageTime(self):
      s=0
      c=0
      (s,c)=self.IteratePageTime(self.Page_1_Pagetime,len(Constants.Page_1),s,c)
      (s,c)=self.IteratePageTime(self.Page_2_Pagetime,len(Constants.Page_2),s,c)
      (s,c)=self.IteratePageTime(self.Page_3_Pagetime,len(Constants.Page_3),s,c)
      (s,c)=self.IteratePageTime(self.Page_4_Pagetime,len(Constants.Page_4),s,c)
      (s,c)=self.IteratePageTime(self.Page_5_Pagetime,len(Constants.Page_5),s,c)
      (s,c)=self.IteratePageTime(self.Page_6_Pagetime,len(Constants.Page_6),s,c)
      (s,c)=self.IteratePageTime(self.Page_7_Pagetime,len(Constants.Page_7),s,c)
      (s,c)=self.IteratePageTime(self.Page_8_Pagetime,len(Constants.Page_8),s,c)
      (s,c)=self.IteratePageTime(self.Page_9_Pagetime,len(Constants.Page_9),s,c)
      (s,c)=self.IteratePageTime(self.Page_10_Pagetime,len(Constants.Page_10),s,c)
      (s,c)=self.IteratePageTime(self.Page_11_Pagetime,len(Constants.Page_11),s,c)
      (s,c)=self.IteratePageTime(self.Page_12_Pagetime,len(Constants.Page_12),s,c)
      (s,c)=self.IteratePageTime(self.Page_13_Pagetime,len(Constants.Page_13),s,c)
      (s,c)=self.IteratePageTime(self.Page_14_Pagetime,len(Constants.Page_14),s,c)
      (s,c)=self.IteratePageTime(self.Page_15_Pagetime,len(Constants.Page_15),s,c)
      (s,c)=self.IteratePageTime(self.Page_16_Pagetime,len(Constants.Page_16),s,c)
      return self.div_z(s,c)

    def checkSynonym(self):
      s=0
      c=0
      (s,c)=self.IterateSyn(self.Syn_1a,self.Syn_1b,s,c)
      (s,c)=self.IterateSyn(self.Syn_2a,self.Syn_2b,s,c)
      (s,c)=self.IterateSyn(self.Syn_3a,self.Syn_3b,s,c)
      (s,c)=self.IterateSyn(self.Syn_4a,self.Syn_4b,s,c)
      (s,c)=self.IterateSyn(self.Syn_5a,self.Syn_5b,s,c)
      (s,c)=self.IterateSyn(self.Syn_6a,self.Syn_6b,s,c)
      (s,c)=self.IterateSyn(self.Syn_7a,self.Syn_7b,s,c)
      (s,c)=self.IterateSyn(self.Syn_8a,self.Syn_8b,s,c)
      (s,c)=self.IterateSyn(self.Syn_9a,self.Syn_9b,s,c)
      (s,c)=self.IterateSyn(self.Syn_10a,self.Syn_10b,s,c)
      (s,c)=self.IterateSyn(self.Syn_11a,self.Syn_11b,s,c)
      (s,c)=self.IterateSyn(self.Syn_1a,self.Syn_1b,s,c)
      (s,c)=self.IterateSyn(self.Syn_5a,self.Syn_5b,s,c)
      (s,c)=self.IterateSyn(self.Syn_6a,self.Syn_6b,s,c)
      (s,c)=self.IterateSyn(self.Syn_7a,self.Syn_7b,s,c)
      (s,c)=self.IterateSyn(self.Syn_2a,self.Syn_2b,s,c)
      (s,c)=self.IterateSyn(self.Syn_4a,self.Syn_4b,s,c)
      (s,c)=self.IterateSyn(self.Syn_8a,self.Syn_8b,s,c)
      (s,c)=self.IterateSyn(self.Syn_3a,self.Syn_3b,s,c)
      (s,c)=self.IterateSyn(self.Syn_9a,self.Syn_9b,s,c)
      (s,c)=self.IterateSyn(self.Syn_10a,self.Syn_10b,s,c)
      (s,c)=self.IterateSyn(self.Syn_11a,self.Syn_11b,s,c)
      return self.div_z(s,c)

    def checkAntonym(self):
      s=0
      c=0
      (s,c)=self.IterateAnt(self.Ant_1a,self.Ant_1b,s,c)
      (s,c)=self.IterateAnt(self.Ant_2a,self.Ant_2b,s,c)
      (s,c)=self.IterateAnt(self.Ant_3a,self.Ant_3b,s,c)
      (s,c)=self.IterateAnt(self.Ant_4a,self.Ant_4b,s,c)
      (s,c)=self.IterateAnt(self.Ant_5a,self.Ant_5b,s,c)
      (s,c)=self.IterateAnt(self.Ant_6a,self.Ant_6b,s,c)
      (s,c)=self.IterateAnt(self.Ant_1a,self.Ant_1b,s,c)
      (s,c)=self.IterateAnt(self.Ant_7a,self.Ant_7b,s,c)
      (s,c)=self.IterateAnt(self.Ant_8a,self.Ant_8b,s,c)
      (s,c)=self.IterateAnt(self.Ant_9a,self.Ant_9b,s,c)
      (s,c)=self.IterateAnt(self.Ant_10a,self.Ant_10b,s,c)
      (s,c)=self.IterateAnt(self.Ant_11a,self.Ant_11b,s,c)
      (s,c)=self.IterateAnt(self.Ant_9a,self.Ant_9b,s,c)
      (s,c)=self.IterateAnt(self.Ant_2a,self.Ant_2b,s,c)
      (s,c)=self.IterateAnt(self.Ant_4a,self.Ant_4b,s,c)
      (s,c)=self.IterateAnt(self.Ant_10a,self.Ant_10b,s,c)
      (s,c)=self.IterateAnt(self.Ant_11a,self.Ant_11b,s,c)
      (s,c)=self.IterateAnt(self.Ant_8a,self.Ant_8b,s,c)
      (s,c)=self.IterateAnt(self.Ant_5a,self.Ant_5b,s,c)
      (s,c)=self.IterateAnt(self.Ant_6a,self.Ant_6b,s,c)
      (s,c)=self.IterateAnt(self.Ant_7a,self.Ant_7b,s,c)
      (s,c)=self.IterateAnt(self.Ant_3a,self.Ant_3b,s,c)
      return self.div_z(s,c)

    def checkInfreq(self):
      s=0
      c=0
      (s,c)=self.IterateInfreq(self.Infreq_1,Constants.infreq_ans[0],s,c)
      (s,c)=self.IterateInfreq(self.Infreq_2,Constants.infreq_ans[1],s,c)
      (s,c)=self.IterateInfreq(self.Infreq_3,Constants.infreq_ans[2],s,c)
      (s,c)=self.IterateInfreq(self.Infreq_4,Constants.infreq_ans[3],s,c)
      (s,c)=self.IterateInfreq(self.Infreq_5,Constants.infreq_ans[4],s,c)
      (s,c)=self.IterateInfreq(self.Infreq_6,Constants.infreq_ans[5],s,c)
      (s,c)=self.IterateInfreq(self.Infreq_7,Constants.infreq_ans[6],s,c)
      (s,c)=self.IterateInfreq(self.Infreq_8,Constants.infreq_ans[7],s,c)
      (s,c)=self.IterateInfreq(self.Infreq_9,Constants.infreq_ans[8],s,c)
      (s,c)=self.IterateInfreq(self.Infreq_10,Constants.infreq_ans[9],s,c)
      (s,c)=self.IterateInfreq(self.Infreq_11,Constants.infreq_ans[10],s,c)
      (s,c)=self.IterateInfreq(self.Infreq_12,Constants.infreq_ans[11],s,c)
      return self.div_z(s,c)
