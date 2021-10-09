#Text to Speech Convertion
from gtts import gTTS  
from playsound import playsound  
what=input("Enter The Text : ")
while True:
	f = open('document.txt', 'w')
	f.write(what)
	language = 'en'  
	obj = gTTS(text=what, lang=language, slow=False)  
	obj.save("storedtext.mp3")    
	playsound('storedtext.mp3')
	input("Press ENTER To Stop Playback")
	break
