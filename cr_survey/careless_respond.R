# careless responding script
# first load in the data
df1=read.csv("D:/downloads_D/CR.Motivation Survey Items.csv",header=F,stringsAsFactors = F)

df1=(Filter(function(x)!all(is.na(x)), df1))

# correct for blank entries
pages=df1[,1]
p=""
for(r in 1:length(pages)){
  if(pages[r]!=""){
    p=pages[r]
  }
  else{
    pages[r]=p
  }
}
df1[,1]=pages

colnames(df1)=c("page","survey","text")

# correcting for misspelling

df1$page=unlist(
  lapply(df1$page,
  function(x){
    ifelse(x=="page 13",
           "Page 13",
           x)
  }
  )
)

# correct for lack of scale information
item_scale_list=list(
  GO="GoalOrientation",
  "F"="GoalOrientation",
  O="Big5",
  C="Big5",
  E="Big5",
  A="Big5",
  N="Big5",
  IM="Likert7",
  WE="Likert5",
  d="Likert5",
  m="Likert5",
  Infreq="Likert5",
  Syn="Likert5",
  Ant="Likert5",
  RI="Likert5",
  RIR="Likert5",
  Dem="Likert5",
  Age="StringInput",
  Gender="StringInput"
)

scales=
  lapply(df1$survey,function(x){
    item_scale_list[unlist(strsplit(x,"_"))[1]]
      }
  )

df1$scale=unlist(scales)

# in case we want to look at which items are semantic synonyms or antonyms
if(F){
  View(df1[sapply(strsplit(df1$survey,"_"),function(x){x[1]})=="Ant",])
  View(df1[sapply(strsplit(df1$survey,"_"),function(x){x[1]})=="Syn",])
  View(df1[sapply(strsplit(df1$survey,"_"),function(x){x[1]})=="Infreq",])
}

# need a list of proper answers for infrequency measures
# we'll just randomize it here
inf_count=nrow(df1[sapply(strsplit(df1$survey,"_"),function(x){x[1]})=="Infreq",])
infreq_answers=sample.int(5, inf_count, replace = TRUE)


make_mls_func=function(pagelist){
  prepend="
def checkMaxLongString(self):
  s=0
  c=0"
  append="
  return self.div_z(s,c)"

  body="
  (s,c)=self.IterateMLS(%s,s,c)"
  
  middle=c()
  for(page in pagelist){
    p_name=paste0(unlist(strsplit(page," ")),collapse="_")
    middle=c(middle,sprintf(body,paste0("self.",p_name,"_MLS"),collapse=""))
  }
  return(paste0(prepend,paste0(middle,collapse=""),append,collapse=""))
}


make_syn_func=function(){
  prepend="
def checkSynonym(self):
  s=0
  c=0"
  append="
  return self.div_z(s,c)"
  
  body="
  (s,c)=self.IterateSyn(%s,%s,s,c)"
  
  syn=df1[sapply(strsplit(df1$survey,"_"),function(x){x[1]})=="Syn",]$survey
  
  syn_list=unlist(lapply(syn,function(x){substr(x,1,nchar(x)-1)}))
  
  middle=c()
  for(sn in syn_list){
    middle=c(middle,sprintf(body,paste0("self.",sn,"a"),paste0("self.",sn,"b")))
  }
  return(paste0(prepend,paste0(middle,collapse=""),append,collapse=""))
}

make_ant_func=function(){
  prepend="
def checkAntonym(self):
  s=0
  c=0"
  append="
  return self.div_z(s,c)"
  
  body="
  (s,c)=self.IterateAnt(%s,%s,s,c)"
  
  ant=df1[sapply(strsplit(df1$survey,"_"),function(x){x[1]})=="Ant",]$survey
  
  ant_list=unlist(lapply(ant,function(x){substr(x,1,nchar(x)-1)}))
  
  middle=c()
  for(an in ant_list){
    middle=c(middle,sprintf(body,paste0("self.",an,"a"),paste0("self.",an,"b")))
  }
  return(paste0(prepend,paste0(middle,collapse=""),append,collapse=""))
}


make_infreq_func=function(){
  prepend="
def checkInfreq(self):
  s=0
  c=0"
  append="
  return self.div_z(s,c)"
  body="
  (s,c)=self.IterateInfreq(self.%s,%s,s,c)"
  
  infreq_l=df1[sapply(strsplit(df1$survey,"_"),function(x){x[1]})=="Infreq",]$survey
  middle=c()
  for(n in 1:length(infreq_l)){
    middle=c(middle,sprintf(body,infreq_l[n],paste0("Constants.infreq_ans[",as.character(n-1),"]")))
  }
  return(paste0(prepend,paste0(middle,collapse=""),append,collapse=""))
}

# def checkPageTime():
#   s=0
# c=0
# (s,c)=IteratePageTime(Page_1_Pagetime,len(Constants.Page_1),s,c)
# # calculated as 2*number of questions is the cutoff where more than this time indicates "good quality" and less time is careless.
# return s/c


make_pt_func=function(pagelist){
  prepend="
def checkPageTime(self):
  s=0
  c=0"
  append="
  return self.div_z(s,c)"
  body="
  (s,c)=self.IteratePageTime(%s,%s,s,c)"
  
  middle=c()
  for(page in pagelist){
    p_name=paste0(unlist(strsplit(page," ")),collapse="_")
    middle=c(middle,sprintf(body,paste0("self.",p_name,"_Pagetime"),paste0("len(Constants.",p_name,")")))
  }
  return(paste0(prepend,paste0(middle,collapse=""),append,collapse=""))
}


{
  # the variables which will bring our metrics from js into python
  cr_measures=c("MLS","Infreq","Syn","Ant","Pagetime")
  cr_measures_page=c("MLS","Pagetime")
  
  # creating the code to paste into the otree models.py script
  lines=c()
  
  lines=c(lines,"# Paste the following into Constants")
  
  # this bit will go in constants
  lines=c(lines,paste0("infreq_ans=[",paste0(as.character(infreq_answers),collapse=","),"]"))
  
  for(page in unique(df1$page)){
    varname=paste0(unlist(strsplit(page," ")),collapse="_")
    cr_page=sapply(cr_measures_page,function(x){paste0(varname,"_",x,collapse="")})
    varlist=paste0(sapply(c(df1[df1$page == page,]$survey,cr_page),
                         function(x){paste0("\"",x,"\"",sep="")}),collapse=", ")
    lines=c(lines,paste0(varname,"=[",varlist,"]"))
  }
  
  # separate them

  lines=c(lines,"")
  
  # this bit will go into player
  
  lines=c(lines,"# Paste the following into player")
  
  for(n in 1:nrow(df1)){
    row=df1[n,]
    fix_rowtext=paste0(unlist(strsplit(row$text,"\"")),collapse="\\\"")
    coderow=paste0(row$survey,"=",row$scale,"(\"",fix_rowtext,"\")")
    fix_apos=paste0(unlist(strsplit(coderow,"'")),collapse="'")
    lines=c(lines,fix_apos)
  }
  for(page in unique(df1$page)){
    varname=paste0(unlist(strsplit(page," ")),collapse="_")
    cr_page=sapply(cr_measures_page,function(x){paste0(varname,"_",x,collapse="")})
    for(var in cr_page){
      coderow=paste0(var,"=","StringInput","(\"",var,"\")")
      lines=c(lines,coderow)
    }
    lines=c(lines,paste0(varname,"_cr=models.FloatField()"))
  }
  
  # functions to calculate all the stuff
  
  lines=c(lines,make_mls_func(unique(df1$page)))
  lines=c(lines,make_pt_func(unique(df1$page)))
  lines=c(lines,make_syn_func())
  lines=c(lines,make_ant_func())
  lines=c(lines,make_infreq_func())

  lines=c(lines,"")
  
  lines=c(lines,"# Paste the following into pages.py")
  
  pc1=
"class Page_%s(Page):
  form_model='player'
  form_fields=Constants.Page_%s
  def vars_for_template(self):
    return(dict(
      qnames=Constants.Page_%s"
  page_class_cr=",
      cr_score=self.player.Page_%s_cr"
  page_class_cr2=",
      cr_score=None"
  pc2="
      ))
  def before_next_page(self):
    self.player.Page_%s_cr=self.player.get_CR_Metric()
  "

  
  for(n in 1:length(unique(df1$page))){
    num=as.character(n)
    part1=sprintf(pc1,num,num,num)
    part_m=sprintf(page_class_cr,as.character(n-1))
    part2=sprintf(pc2,num)
    if(n==1){
      part_m=page_class_cr2
    }
    lines=c(lines,paste0(part1,part_m,part2))
  }
  
  lines=c(lines,"")
  
  
  lines=c(lines,"page_sequence = [")
  for(page in unique(df1$page)){
    p=paste0(unlist(strsplit(page," ")),collapse="_")
    lines=c(lines,paste0("    ",p,",",sep=""))
  }
  lines=c(lines,"]")
  
  # save it to a document
  setwd("D:/downloads_D")
  fileConn<-file("cr_for_otree.txt")
  writeLines(lines,fileConn)
  close(fileConn)
}




