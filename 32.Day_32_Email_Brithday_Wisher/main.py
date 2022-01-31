import smtplib
import datetime as dt
import random
import pandas

my_email = 'fatpytest@gmail.com'
password = 'fatpytest1?x'

current_time = dt.datetime.now()
day = current_time.day
month = current_time.month
today = (day, month)
print(today)

# Read birthdays
data_file = pandas.read_csv('birthdays.csv')
# print(data_file)
birthday_dict = {data_row['name']: (data_row['day'], data_row['month'], data_row['email'])
                 for (index, data_row) in data_file.iterrows()}
# print(birthday_dict)

# check if someone's birthday is today
for name, info in birthday_dict.items():
    birthday = (info[0], info[1])

    if today == birthday:
        # Pick a random letter
        letter_nr = random.choice([1, 2, 3])

        with open(f'letter_templates/letter_{letter_nr}.txt') as letter:
            text = letter.read()

            # Replace the Placeholder
            text = text.replace('[NAME]', name)

            # Send it in an email
            with smtplib.SMTP_SSL('smtp.gmail.com', timeout=60) as connection:
                # connection.starttls()  # Secure the connection
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=info[2],
                                    msg=f'Subject:Happy Birthday!\n\n{text}')
