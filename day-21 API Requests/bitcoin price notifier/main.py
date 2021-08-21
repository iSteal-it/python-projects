import requests
import time
import smtplib

parameter = {
    "ids": "bitcoin",
    "vs_currencies": "usd"
}

previous_price = 0


def mail(current_price,previous_price,difference_by,sub):
     msg_to_send = f"previous price:${previous_price}\n current price:${current_price}\n difference:{difference_by}"
     email="bobbobpvp@gmail.com"
     my_email = "admin@pixelpaste.net"
     password = ""
     connection = smtplib.SMTP("smtp.hostinger.com", 587)
     connection.starttls()
     connection.login(user=my_email, password=password)
     connection.sendmail(
          from_addr=my_email,
          to_addrs=email,
          msg=f"From:Admin@pixelpaste.net\nSubject:{sub}\n\n {msg_to_send}"
     )
     connection.close()


while True:
    time.sleep(300)
    response = requests.get(url="https://api.coingecko.com/api/v3/simple/price", params=parameter)
    data = response.json()
    current_price = int(data["bitcoin"]["usd"])
    if previous_price < current_price:
        difference_by = current_price - previous_price
        sub = "Price Went Up"
        if (difference_by) >= 100:
             mail(current_price,previous_price,difference_by,sub)
             previous_price = current_price
    if previous_price > current_price:
        difference_by = previous_price - current_price
        sub = "Price Went Down"
        if (difference_by) >= 100:
             mail(current_price,previous_price,difference_by,sub)
             previous_price = current_price


