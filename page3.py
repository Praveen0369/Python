from distutils.cmd import Command
from re import T
from tkinter import END, EW, INSERT, N,S,E,W, NE, NS, NW, Button, Scrollbar, Tk, Canvas, PhotoImage,Text
import cv2 
import mediapipe as mp
import numpy as np
import nltk
import string
import random
from nltk.stem import WordNetLemmatizer
nltk.download('omw-1.4')
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils



def photo_image(img):
    h, w = img.shape[:2]
    data = f'P6 {w} {h} 255 '.encode() + img[..., ::-1].tobytes()
    return PhotoImage(width=w, height=h, data=data, format='PPM')

def update():
    ret, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handslms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handslms, mpHands.HAND_CONNECTIONS)
    if ret:
        photo = photo_image(img)
        canvas.create_image(0, 0, image=photo, anchor=NW)
        canvas.image = photo
    root.after(15, update)

def getvalue():
    pilp=text1.get(1.0, "end-1c")
    return pilp


root = Tk()
root.title("Handmapping")
cap = cv2.VideoCapture(0)
canvas = Canvas(root,height=500,width=600)
canvas.grid(row=0,column=0,sticky=NS)
text=Text(root,yscrollcommand=Scrollbar.set)
text.grid(row=0,column=1,sticky=NS)
text1=Text(root,height=30)
text1.grid(row=1,column=1,sticky=EW)


sub_btn=Button(root,text = 'Submit', command ="",width=30)
sub_btn.grid(row=1,column=1,sticky=NW)



def chat():
    f=open('trainer.txt','r',errors='ignore')
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
    text.insert(INSERT,"BOT: My name is Stark Ask me Any thing , if not type BYE to exit")
    while(flag==True):
        User_response=getvalue()
        User_response=User_response.lower()
        if(User_response!='bye'):
            if(User_response=="thanks" or User_response=="thank you"):
                flag=False
                text.insert(INSERT,"Bot:you are welcome")
            else:
                if(greet(User_response)!=None):
                    text.insert(INSERT,"Bot: "+greet(User_response))
                else:
                    sent_tokens.append(User_response)
                    word_tokens=word_tokens+nltk.word_tokenize(User_response)
                    final_words=list(set(word_tokens))
                    text.insert(INSERT,"Bot: ")
                    text.insert(INSERT,response(User_response))
                sent_tokens.remove(User_response)
        else:
            flag=False
            text.insert(INSERT,"BOT :Good Bye Take Care <3")


update()
chat()
root.mainloop()
cap.release()