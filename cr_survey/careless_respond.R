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
  Age="Likert5",
  Gender="Likert5"
)

scales=
  lapply(df1$survey,function(x){
    item_scale_list[unlist(strsplit(x,"_"))[1]]
      }
  )

df1$scale=unlist(scales)

# in case we want to look at which items are semantic synonyms or antonyms
View(df1[sapply(strsplit(df1$survey,"_"),function(x){x[1]})=="Ant",])
View(df1[sapply(strsplit(df1$survey,"_"),function(x){x[1]})=="Syn",])

{
  # creating the code to paste into the otree models.py script
  lines=c()
  
  # this bit will go in constants
  for(page in unique(df1$page)){
    varname=paste0(unlist(strsplit(page," ")),collapse="_")
    varlist=paste0(sapply((df1[df1$page == page,]$survey),
                         function(x){paste0("\"",x,"\"",sep="")}),collapse=", ")
    lines=c(lines,paste0(varname,"=[",varlist,"]"))
  }
  
  # separate them
  lines=c(lines,"")
  
  # this bit will go into player
  for(n in 1:nrow(df1)){
    row=df1[n,]
    fix_rowtext=paste0(unlist(strsplit(row$text,"\"")),collapse="\\\"")
    coderow=paste0(row$survey,"=",row$scale,"(\"",fix_rowtext,"\")")
    fix_apos=paste0(unlist(strsplit(coderow,"'")),collapse="'")
    lines=c(lines,fix_apos)
  }
  
  lines=c(lines,"")
  
  
  page_class1="class "
  page_class2="(Page):
      form_model='player'
      form_fields=Constants."
  page_class3="
      def vars_for_template(self):
          return(dict(
              qnames=Constants."
  page_class4="
          ))"
  
  for(page in unique(df1$page)){
    p=paste0(unlist(strsplit(page," ")),collapse="_")
    lines=c(lines,paste(page_class1,p,page_class2,p,page_class3,p,page_class4,sep=""))
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



