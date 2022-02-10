import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# verified numbers from twilio account
PHONE_NUMBER_FROM = ''
PHONE_NUMBER_TO = ''

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = 'RO50IZSOPQYSLU81'

STOCK_PARAMS = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMS)
stock_data = stock_response.json()
print(stock_data)

# https://www.alphavantage.co/documentation/#daily
# Access yesterday close price
yesterday_close_price = float(stock_data['Time Series (Daily)']['2022-01-28']['4. close'])
print(yesterday_close_price)

# Access the day before yesterday close price
before_yesterday_close_price = float(stock_data['Time Series (Daily)']['2022-01-27']['4. close'])
print(before_yesterday_close_price)

# Find absolute difference in %
day_difference = abs(yesterday_close_price - before_yesterday_close_price)
print(day_difference)

day_difference_percent = round((day_difference / yesterday_close_price) * 100)
print(f'{day_difference_percent}%')

# When stock price increase/decreases by 5% between yesterday and the day before yesterday then ("Get News").

# day_difference_percent = 6  # testing

if day_difference_percent > 5:

    # Get news for COMPANY_NAME
    # https://newsapi.org/

    NEWS_KEY = '2037f235f1334634ac4215667b709e6d'
    NEWS_PARAMS = {
        'apiKey': NEWS_KEY,
        'q': 'Tesla'
    }

    news_response = requests.get(url='https://newsapi.org/v2/top-headlines', params=NEWS_PARAMS)
    news_data = news_response.json()

    # Access content for 3 first articles
    articles = news_data['articles'][:3]

    # Put articles data in a list
    articles_list = [[news_data['articles'][i]['title'], news_data['articles'][i]['description']]
                     for i in range(len(articles))]

    # Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

    # twilio data
    ACCOUNT_SID = 'AC496ebc1c379819f9845bf0acadced4fe'
    AUTH_TOKEN = '48a2d8a59b10ce5334c755ada5dd5618'

    if yesterday_close_price > before_yesterday_close_price:
        sign = '🔺'
    else:
        sign = '🔻'

    for article in articles_list:
        proxy_client = TwilioHttpClient()
        client = Client(ACCOUNT_SID, AUTH_TOKEN, http_client=proxy_client)

        message = client.messages \
            .create(
            body=f'{STOCK_NAME}: {sign}{day_difference_percent}\nHeadline: {article[0]}\nBrief: {article[1]}',
            from_=PHONE_NUMBER_FROM,
            to=PHONE_NUMBER_TO
        )

        print(message.status)


