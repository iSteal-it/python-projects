import pandas
import datetime
import smtplib
import random

now = datetime.datetime.now()
month = (now.month)
day = (now.day)

data = pandas.read_csv("birthdays.csv").to_dict(orient="records")
for person in data:
    if person["month"] == month and person["day"] == day:
        email = person["email"]

        file = open(f"letter_templates/letter_{random.randint(1,3)}.txt")
        content = file.read()
        msg_to_send =content.replace("[NAME]",person["name"])
        file.close()

        my_email = "admin@pixelpaste.net"
        password = "Krevory123@"
        connection = smtplib.SMTP("smtp.hostinger.com", 587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"From:Admin@pixelpaste.net\nSubject:Happy Birthday\n\n {msg_to_send}"
            )
        connection.close()