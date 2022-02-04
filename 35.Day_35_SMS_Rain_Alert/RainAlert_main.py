import os
import requests
import twilio.http
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from config import *

# Your city
MY_LAT = 53.367220
MY_LNG = 14.971260

OPEN_WEATHER_MAP_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'


parameters = {
    'lat': MY_LAT,
    'lon': MY_LNG,
    'appid': API_KEY,
    'exclude': 'current,minutely,daily',
    'units': 'metric',
}

response = requests.get(url=OPEN_WEATHER_MAP_ENDPOINT, params=parameters)
response.raise_for_status()  # 200 all ok
data = response.json()

# check if id < 700 (meaning some kind of rain) in next 24 hours
# we run the scrip at 0:00

will_rain = False

for hour in range(24):
    hour_data_id = data['hourly'][hour]['weather'][0]['id']
    if hour_data_id < 700:
        will_rain = True

if will_rain:
    # create Twilio Client to send SMS Alert
    proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body='Bring an umbrella. ☂️',
        from_='+17755425641',
        to=my_number
    )

    print(message.status)


