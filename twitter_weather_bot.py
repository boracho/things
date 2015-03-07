import tweepy, requests, time
CONSUMER_KEY = 'jwKKVXXsprcTXxAELCbwT2NSi'
CONSUMER_SECRET = 'XqFMMybRZDJx3LBBY1SI9ejWiAnPW6f6mDZlBZxCLvOOtGevTR'
ACCESS_KEY = '3073786817-nnXmbkReKpz8mQd1zY2Bot165w4z9hUlwKfNLVs'
ACCESS_SECRET = '8kfDSBioW9xw0BAtDvIcGPuD5w3j7u3SLVdoije984AUL'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

newline = '\n'

url = 'http://api.openweathermap.org/data/2.5/weather?'
payload = {
            'q': 'Uniontown,pa', 'units': 'imperial',
            'type': 'like', 'APPID': 'd009cf498679747e03a4350b3f5e761d'
          }

while True:
    weather = requests.get(url, params=payload).json()
    temp = weather['main']['temp']
    humidity = weather['main']['humidity']
    clouds = weather['clouds']['all']
    
    api.update_status(status = 'The current Conditions in Uniontown:\nTepmerature: ' + str(temp) + u'\u00B0F\nHumidity: ' + str(humidity) + '%\nCloud Coverage: ' + str(clouds) + '%')
    time.sleep(3600)