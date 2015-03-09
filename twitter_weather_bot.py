import tweepy, requests, time
#some variables for all the little children
#remember to insert your own api keys for your twitter app
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
#because typing that out is a pain
newline = '\n'

#it's our url for openweathermap and our payload of url parameters
url = 'http://api.openweathermap.org/data/2.5/weather?'
#APPID is the api key for openweathermap.org
payload = {
            'q': 'Uniontown,pa', 'units': 'imperial',
            'type': 'like', 'APPID': ''
          }
#our main loop.  All kinds of gains.
while True:
    #our json response object from owm and some variables obtained therin
    weather = requests.get(url, params=payload).json()
    temp = weather['main']['temp']
    humidity = weather['main']['humidity']
    clouds = weather['clouds']['all']
    #sending our tweet with our variables and our sleepy-time, so we don't send out 100s of tweets a second or whatever.
    api.update_status(status = 'The current Conditions in Uniontown:\nTepmerature: ' + str(temp) + u'\u00B0F\nHumidity: ' + str(humidity) + '%\nCloud Coverage: ' + str(clouds) + '%')
    time.sleep(3600)