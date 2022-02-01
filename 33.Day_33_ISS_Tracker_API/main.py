import requests
import datetime as dt
import smtplib
import time

# My location
MY_LAT = 53.367220
MY_LNG = 14.971260
MY_POSITION = (MY_LAT, MY_LNG)

# My test email
MY_EMAIL = ''  # use gmail
PASSWORD = ''  # use gmail

# HTTP Codes
# 1xx - INFORMATION - Hold on, we are working on something
# 2xx - SUCCESS - everything worked as planned
# 3xx - REDIRECTION - go away, you don't have permission to access
# 4xx - CLIENT ERROR - something is missing, you screwed up
# 5xx - SERVER ERROR - server is down, bugged, etc.
# https://httpstatuses.com/


def is_ISS_near_me():  # returns True if within +/- 10 degrees

    # Access ISS API
    iss_response = requests.get(url='http://api.open-notify.org/iss-now.json')
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    # Find ISS Location
    iss_lng = float(iss_data['iss_position']['longitude'])
    iss_lat = float(iss_data['iss_position']['latitude'])
    iss_position = (iss_lat, iss_lng)

    # check if iss location is within +/- 10 degrees of my location
    if MY_LAT - 10 <= iss_lat <= MY_LAT + 10 and MY_LNG - 10 <= iss_lng <= MY_LNG + 10:
        return True
    else:
        return False


def is_night():  # You can only see ISS if it is night, returns True if after sunset or before sunrise

    # Access Sun API for My Location
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0
    }

    sun_response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    sun_response.raise_for_status()

    # Find Sunset and Sunrise time
    sun_data = sun_response.json()
    sunrise = sun_data['results']['sunrise']
    sunset = sun_data['results']['sunset']

    # Format the sunrise, sunset times to 24 hour clock
    sunrise = int(sunrise.split('T')[1].split(':')[0])
    sunset = int(sunset.split('T')[1].split(':')[0])

    # My current time
    time_now = dt.datetime.now().hour

    # check if night
    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False


while True:
    time.sleep(60)  # run every 60 sec

    # if ISS is near me and it is night I can see it, send and email to look up
    if is_ISS_near_me() and is_night():

        # Send email
        with smtplib.SMTP_SSL('smtp.gmail.com', timeout=60) as connection:
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg='Subject:ISS ALERT!\n\nLook up!')


