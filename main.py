##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
# from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import datetime as dt
import smtplib
import random

email = "*******@gmail.com"
password = "*******"

birthdays_data = pandas.read_csv("birthdays.csv")  # converts the csv into a data frame
birthdays_dict = birthdays_data.to_dict(orient="records")  # create a dictionary from the data frame (list of dict)

now = dt.datetime.now()  # takes the current date
current_day = now.day  # takes the current day
current_month = now.month  # takes the current month


for info in birthdays_dict:

    if info['month'] == current_month and info['day'] == current_day:  # checks to see if today's month and day matches
        name = info['name']  # take the name of the recipient
        recipient_email = info['email']  # takes the email of the recipient

        letter_number = random.randint(1, 3)  # chooses a random number for which letter to be sent

        with open(f"letter_templates/letter_{letter_number}.txt", mode="r") as file:
            content = file.read()  # reads the letter and saves it inside the variable
            new_content = content.replace("[NAME]", name)  # replace the string [NAME] with recipient name

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()  # secure connection with TLS
            connection.login(user=email, password=password)  # login into the email address of the sender
            connection.sendmail(from_addr=email, to_addrs=recipient_email,
                                msg=f"Subject: Happy Birthday !\n\n{new_content}")  # sends email
