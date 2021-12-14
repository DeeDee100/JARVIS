import pyttsx3
from decouple import config
from datetime import datetime
import speech_recognition as sr
from random import choice
from utilis import opening_text
from functions.ops import open_notepad
from functions.online_ops import get_news

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine_PT = pyttsx3.init('sapi5') # sapi5 = Microsoft API to use voices

engine_PT.setProperty('rate', 190) #Set Rate of speech
engine_PT.setProperty('volume', 1.0) #Set Volume of speech

voices = engine_PT.getProperty('voices')
engine_PT.setProperty('voice', voices[0].id) #set voice to Male [0] or Female [1]

#Txt to speech
def speak_PT(text):
	engine_PT.say(text)
	engine_PT.runAndWait()

#greetings
def greetings():
	hour = datetime.now().hour
	if (hour >= 6) and (hour < 12):
		speak_PT(f'Bom dia {USERNAME}')
	elif (hour >= 12) and (hour < 16):
		speak_PT(f'Boa tare {USERNAME}')
	elif(hour >= 16) and (hour < 19):
		speak_PT(f'Boa tarde {USERNAME}')
	else:
		speak_PT(f'Boa noite {USERNAME}')
	speak_PT(f"Eu sou {BOTNAME}. Como posso ajudá-lo?")

def user_input():
	r = sr.Recognizer()
	while True:
		with sr.Microphone() as source:
			print('Listening...')
			r.pause_threshold=1
			audio = r.listen(source)
		try:
			print('Recognizing...')
			query = r.recognize_google(audio, language='pt-br')
			if 'parar' in query or 'sair' in query:
				hour = datetime.now().hour
				if hour >= 21 and hour < 6:
					speak_PT("Boa noite, até mais")
				else:
					speak_PT('Tenha um bom dia.')
				exit()
			else:
				speak_PT(choice(opening_text))
				return query
		except Exception:
			speak_PT('Não conseguir entender, fale denovo por favor ')
			query = None

def noticias():
	speak_PT("Lerei as notícias agora:")
	speak_PT(get_news())
	print(get_news())


# for voice in voices:
# 	print("Voice: %s" % voice.name)
# 	print(" - ID: %s" % voice.id)
# 	print(" - Languages: %s" % voice.languages)
# 	print(" - Gender: %s" % voice.gender)
# 	print(" - Age: %s" % voice.age)
# 	print("\n")

