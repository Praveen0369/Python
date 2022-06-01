import numpy as np
import nltk
import string
import random
from nltk.stem import WordNetLemmatizer
f=open('/content/trainer.txt','r',errors='ignore')
raw_doc=f.read()
raw_doc=raw_doc.lower()
nltk.download('punkt')
nltk.download('wordnet')
sent_tokens=nltk.sent_tokenize(raw_doc)
word_tokens=nltk.word_tokenize(raw_doc)
lemmatizer = WordNetLemmatizer()
def LemTokens(tokens):
  return[lemmatizer.lemmatize(token) for token in tokens]
remove_punct_dict=dict((ord(punct),None) for punct in string.punctuation)
def LemNormalize(text):
  return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
greet_inputs=("hello","hi","whatsapp","hey")
greet_responses=("hii","hello","hey","vannakam")
def greet(sentence):
  for word in sentence.split():
    if word.lower() in greet_inputs:
      return random.choice(greet_responses)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def response(User_response):
  robo1_response=''
  Tfidfvec=TfidfVectorizer(tokenizer=LemNormalize,stop_words='english')
  tfidf=Tfidfvec.fit_transform(sent_tokens)
  vals=cosine_similarity(tfidf[-1],tfidf)
  idx=vals.argsort()[0][-2]
  flat=vals.flatten()
  flat.sort()
  req_tfidf=flat[-2]
  if(req_tfidf==0):
    robo1_response=robo1_response+"sorry i can't understand you"
    return robo1_response
  else:
    robo1_response=robo1_response+sent_tokens[idx]
    return robo1_response
flag=True
print("BOT: My name is Stark Ask me Any thing , if not type BYE to exit")
while(flag==True):
  User_response=input()
  User_response=User_response.lower()
  if(User_response!='bye'):
    if(User_response=="thanks" or User_response=="thank you"):
      flag=False
      print("Bot:you are welcome")
    else:
      if(greet(User_response)!=None):
        print("Bot: "+greet(User_response))
      else:
        sent_tokens.append(User_response)
        word_tokens=word_tokens+nltk.word_tokenize(User_response)
        final_words=list(set(word_tokens))
        print("Bot: ",end="")
        print(response(User_response))
        sent_tokens.remove(User_response)
  else:
    flag=False
    print("BOT :Good Bye Take Care <3")
