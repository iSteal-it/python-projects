import smtplib
import pandas
import datetime
import random

now = datetime.datetime.now()

now_day = now.strftime("%A")

if now_day == "Friday":
    data = pandas.read_csv("quotes.txt",header=None).to_dict(orient="records")
    quote = random.choice(data)
    my_email = "admin@pixelpaste.net"
    password = ""
    connection = smtplib.SMTP("smtp.hostinger.com",587)
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="bobbobpvp@gmail.com",
        msg=f"From:Admin@pixelpaste.net\nSubject:Today Quote\n\n {quote[0]}"
    )
    connection.close()
