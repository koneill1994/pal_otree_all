library(jsonlite)

# this reads in the ratpal list and exports a formatted csv

rm(list = ls())

# ratpal=read.csv(file.choose(),header=FALSE)
ratpal=read.csv("RAT items.csv",header=FALSE,stringsAsFactors = F)

# remove the entry with 2 answers
# (high/district/house)
ratpal=data.frame(ratpal[1:nrow(ratpal)!=20,])


#######
# PREPROCESSING
# this takes the raw input file
# and turns it into a dataframe with columns for words & match
#######

wordlist=data.frame(words=character(),match=character(),stringsAsFactors = F)

wordpairs=vector("list",nrow(ratpal))

numpairs=vector("list",nrow(ratpal))

for(r in 1:nrow(ratpal)){
  # get each row of the ratpal words and format it
  row=ratpal[r,]
  r2=unlist(strsplit(as.character(row)," "))
  # get the words (r3[1:(length(r3)-1)]) and the match (r3[length(r3)])
  r3=(r2[1:(length(r2)-10)])
  match=r3[length(r3)]
  words=paste(r3[1:(length(r3)-1)],collapse = '')
  
  # add them to a df wordlist
  wordlist=rbind(wordlist,data.frame(words,match))
  
  # wordpairs[[r]]=(list(words,match))
  # numpairs[[r]]=(list(round(runif(1,1,9)),match))
}

# uncomment these lines to save the generated words to file
# write.csv(wordlist,"ratpal_words.csv")
# 
# write(toJSON(wordpairs),"wordlist.json")
# write(toJSON(numpairs),"numlist.json")



# dump words into groups, along with foils, which will be read by otree

foils=read.csv("ratpal_foils.csv",header=FALSE,stringsAsFactors = F)

foil_list=unlist(lapply(foils$V2,tolower))

# for both hometime and study time
# 5 old (last 5 of last round), 5 new, 10 foils sampled from list

# so they'll see all of them once in school time
# except for first 5 and last 5



# remove from the list of foils any words which overlap between foils and match words
foil_list=
  foil_list[
    unlist(lapply(
      foil_list,function(x){
        !(x %in% intersect(wordlist$match,foil_list))
        }
    ))
    ]


# change the data types of the columns from factor to characters
wordlist$words=as.character(wordlist$words)
wordlist$match=as.character(wordlist$match)


# this is the function that specifies, for a given session number sesh domain (1:6)
# the indices of the words from wordlist that should be presented in that session
words_i=function(sesh){
  if(sesh==1){
    1:10
  }
  else{
    (sesh-2)*5+6:15
  }
}

words_i_general=function(sesh,words_per_session,overlap){
  (sesh-1)*overlap+1:words_per_session
}

words_i_general(2,25,10)

# the number list which holds all the word-number pairs we'll want
nlist=list()


n_words=10
n_foils=10

# for each session
for(n in 1:6){
  
  # words, gets the words for this session
  w=wordlist[words_i(n),]$match
  
  # foils, gets random foils for this session
  f=sample(foil_list,n_foils)
  
  # sesh hold the list of word-number pairs for this session
  sesh=list()
  
  # word count, foil count, initialized at 1 (so we can use it as an index)
  wc=1
  fc=1
  
  # keep adding random words from either worsd or foils until we have
  # 10 words and 10 foils
  # each paired with a random number [1:9]
  while(wc<n_words+1 | fc<n_foils+1){
    if(wc>=n_words+1){
      sesh[[length(sesh)+1]]=c(f[fc],round(runif(1,1,9)))
      fc=fc+1
    }
    else if(fc>=n_foils+1){
      sesh[[length(sesh)+1]]=c(w[wc],round(runif(1,1,9)))
      wc=wc+1
    }
    else{
      if(runif(1)>.5){
        sesh[[length(sesh)+1]]=c(f[fc],round(runif(1,1,9)))
        fc=fc+1
      }
      else{
        sesh[[length(sesh)+1]]=c(w[wc],round(runif(1,1,9)))
        wc=wc+1
      }
    }

  }
  # add this session's word list to the overall list
  nlist[[n]]=sesh
  
}


wlist=list()
# if we want to replace the schooltime stuff use this code below

for(n in 1:6){

  wordgroup=wordlist[words_i(n),]

  w=list()

  for(row in 1:nrow(wordgroup)){
    w[[row]]=unlist(list(wordgroup[row,]$words,wordgroup[row,]$match))
  }
  
  wlist[[n]]=w
  
}

# uncomment these lines to save the generated word pairs to file
# write(toJSON(nlist),"nlist.json")
# write(toJSON(wlist),"wlist.json")
# 
# write(toJSON(wordpairs),"wordlist.json")
