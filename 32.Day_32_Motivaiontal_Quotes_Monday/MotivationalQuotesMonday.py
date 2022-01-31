import smtplib
import datetime as dt
import random

my_email = 'fatpytest@gmail.com'
password = 'fatpytest1?x'

current_time = dt.datetime.now()
today = current_time.weekday()  # 0 - Monday, 1 - Tuesday ...
print(today)

if today == 0:  # if today is Monday

    #  Send motivational quote form quotes.txt
    with open('quotes.txt', 'r') as data_file:
        quotes = data_file.readlines()
        # Get one random quote
        quote = quotes[random.randint(0, len(quotes))]
        print(quote)

        # Send it in an email
        with smtplib.SMTP_SSL('smtp.gmail.com', timeout=60) as connection:
            # connection.starttls()  # Secure the connection
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs='bartser95@gmail.com',
                                msg=f'Subject:Your Monday Motivational Quote\n\n{quote}')


