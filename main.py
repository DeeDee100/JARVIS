import pyttsx3
from decouple import config
from datetime import datetime
import speech_recognition as sr
from random import choice
from utilis import opening_text
from functions.ops import open_notepad, open_discord, open_edge, open_terminal
from functions.online_ops import get_news, random_advice, random_joke, search_google, search_wikipedia, send_email, whatsapp_message, youtube, trending_series, trending_movies


USERNAME = config('USER')
BOTNAME = config('BOTNAME')

#English Voice:
engine = pyttsx3.init('sapi5') # sapi5 = Microsoft API to use voices

engine.setProperty('rate', 180) #Set Rate of speech
engine.setProperty('volume', 1.0) #Set Volume of speech

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # Set voice to English

#Txt to speech
def speak(text):
	engine.say(text)
	engine.runAndWait()

#greetings
def greetings():
	hour = datetime.now().hour
	if (hour >= 6) and (hour < 12):
		speak(f'Good Morning {USERNAME}')
	elif (hour >= 12) and (hour < 16):
		speak(f'Good Afternoon {USERNAME}')
	elif(hour >= 16) and (hour < 19):
		speak(f'Good Evening {USERNAME}')
	else:
		speak(f'Good night {USERNAME}')
	speak(f"I am {BOTNAME}. How can i help you ?")


def user_input():
	r = sr.Recognizer()
	while True:
		with sr.Microphone() as source:
			print('Listening...')
			r.pause_threshold=1
			audio = r.listen(source)
		try:
			print('Recognizing...')
			query = r.recognize_google(audio, language='en-in')
			if 'exit' in query or 'stop' in query:
				hour = datetime.now().hour
				if hour >= 21 and hour < 6:
					speak("Good night, take care!")
				else:
					speak('Have a good day.')
				exit()
			else:
				speak(choice(opening_text))
				return query
		except Exception:
			speak('Sorry, I could not understant. Repeat please.')
			query = None
	

if __name__ == '__main__':
	greetings()
	while True:
		query = user_input().lower()
		if "open notepad" in query:
			open_notepad()
		elif "open terminal" in query:
			open_terminal()
		elif "open edge" in query:
			open_edge()
		elif "open discord" in query:
			open_discord()
		elif "wikipedia" in query:
			speak("What do you want to search on Wikipedia ?")
			search = user_input().lower()
			try:
				results = search_wikipedia(search)
				speak(f"Wiki says: {results}")
				speak("I am also printing the results on screen")
				print(results)
			except Exception as e:
				speak("Something went wrong, check logs please.")
				print(e)
		elif "youtube" in query:
			speak("What do you want to see on Youtube?")
			video = user_input().lower()
			youtube(video)
		elif "google" in query:
			speak("What Do you want to ask google ?")
			search = user_input().lower()
			search_google(search)
		elif "send whatsapp message" in query:
			speak("Please enter number to send: ")
			number = input("Number input: ")
			speak('What is the message ?')
			message = user_input().lower()
			whatsapp_message(number, message)
			speak("Message sent.")
		elif "send email" in query:
			speak("Please enter which email address")
			email = input("Enter email: ")
			speak('What is the subject ?')
			subject = user_input().capitalize()
			speak("What is the message?")
			message = user_input().capitalize()
			if send_email(email, subject, message):
				speak("Email sent")
			else:
				speak("Something went wrong. Please verify logs")
		elif "joke" in query:
			joke = random_joke()
			speak(joke)
			print(joke)
		elif "advice" in query:
			advice = random_advice()
			speak(advice)
			print(advice)
		elif 'news' in query:
			engine.setProperty('voice', voices[0].id) # Set voice to PT
			speak("Lerei as noticias agora: ")
			speak(get_news())
			print(*get_news(), sep='\n')
			engine.setProperty('voice', voices[1].id) #swicht voice back to English
		elif 'trending movies' in query:
			speak(f"These are the trending movies today: {trending_movies()}")
			print(*trending_movies(), sep='\n')
			
		elif 'trending tv shows' in query:
			speak(f"These are the trending tv shows today: {trending_series()}")
			print(*trending_series(), sep='\n')



