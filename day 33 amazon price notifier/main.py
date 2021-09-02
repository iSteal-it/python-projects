import requests
from bs4 import BeautifulSoup
import time
import smtplib

item_url = input("please enter the url of item whos price you wanted to track: ")
buying_price = int(input("please enter the price at which you would like to buy it: "))

while True:
    header =  {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language' : 'en-US,en;q=0.5',
    'Accept-Encoding' : 'gzip',
    'DNT' : '1',
    'Connection' : 'close'
    }
    response = requests.get(url=item_url,headers=header)
    data = response.text

    soup = BeautifulSoup(data,"html.parser")

    founnd = soup.find("span", {"id": "priceblock_ourprice"}).text
    char = ","
    x = founnd.replace("₹","")
    x3 = x.replace(".00","")
    if char in x:
        x2 = x3.replace(",","")
    price_on_website = int(x2)

    if price_on_website <= buying_price:
        my_email = "admin@pixelpaste.net"
        msg = f"price of your wished product is:{price_on_website}\n go buy it how at {item_url}"
        password = "Krevory123@"
        connection = smtplib.SMTP("smtp.hostinger.com", 587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="bobbobpvp@gmail.com",
            msg=f"From:Admin@pixelpaste.net\nSubject:Yeeh you can buy it now\n\n {msg}"
        )
        connection.close()
        break
    time.sleep(21600)
