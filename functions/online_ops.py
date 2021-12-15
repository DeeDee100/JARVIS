import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")
TMDB_API_KEY = config("TMDB_API_KEY")
NEWS_API_KEY = config("NEWS_API_KEY")

def my_ip():
	ip = requests.get('https://api64.ipify.org/?format=json').json()
	return ip['ip']

def search_wikipedia(query):
	results = wikipedia.summary(query, sentences=2)
	return results

def youtube(video):
	kit.playonyt(video)

def search_google(query):
	kit.search(query)

def whatsapp_message(number, message):
	kit.sendwhatmsg_instantly(f"+55{number}", message)


def send_email(receiver_address, subject, message):
	try:
		email = EmailMessage()
		email['To'] = receiver_address
		email["Subject"] = subject
		email['From'] = EMAIL
		email.set_content(message)
		s = smtplib.SMTP("smtp.gmail.com", 587)
		s.starttls()
		s.login(EMAIL, PASSWORD)
		s.send_message(email)
		s.close()
		return True
	except Exception as e:
		print(e)
		return False

def trending_movies():
	trending_movies =[]
	res = requests.get(f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
	results = res['results']
	for r in results:
		trending_movies.append(r['original_title'])
	return trending_movies

def trending_series():
	trending_series = []
	res = requests.get(f"https://api.themoviedb.org/3/trending/tv/day?api_key={TMDB_API_KEY}").json()
	results = res['results']
	for r in results:
		trending_series.append(r['name'])
	return trending_series

def random_joke():
	headers = {'Accept': 'application/json'}
	result = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
	return result['joke']

def random_advice():
	result = requests.get("https://api.adviceslip.com/advice").json()
	return result['slip']['advice']

def get_news():
	news = {}
	res = requests.get("https://newsapi.org/v2/top-headlines?sources=google-news-br&apiKey=93db446587ea43d9810b7011e915b4dd").json()
	result = res['articles']
	for n in result:
		news[n['title']] = n['description']
	return news

