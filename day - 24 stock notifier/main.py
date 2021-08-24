import requests
import smtplib

coingenko_url = "https://api.coingecko.com/api/v3/simple/price"
coingenko_parameter = {
    "ids": "bitcoin",
    "vs_currencies": "usd",
    "include_24hr_change": "true"
}


newsapi_key = "9234bd6931554d528a6d1a08260ccc6e"
newsapi_url = "https://newsapi.org/v2/top-headlines"
newsapi_parameter = {
    "q":"bitcoin",
    "apikey":newsapi_key
}


def get_news():
    response = requests.get(url=newsapi_url,params=newsapi_parameter)
    data = response.json()
    return data


def get_price():
    response = requests.get(url=coingenko_url,params=coingenko_parameter)
    data = response.json()
    return data

def mail(news,current_price,price_change_in_24hrs):
    my_email = "admin@pixelpaste.net"
    msg = f"bitcoin price:{current_price}\n price change:{price_change_in_24hrs}%\ntitle:{news['title'].encode('utf-8')}\n description:{news['description'].encode('utf-8')}"
    password = ""
    connection = smtplib.SMTP("smtp.hostinger.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="bobbobpvp@gmail.com",
        msg=f"From:Admin@pixelpaste.net\nSubject:Bitcoin Price Alert\n\n {msg}"
    )
    connection.close()


current_price = get_price()["bitcoin"]["usd"]
price_change_in_24hrs = round(get_price()["bitcoin"]["usd_24h_change"],2)

if price_change_in_24hrs > 1:
    news = get_news()["articles"][0]
    mail(news,current_price,price_change_in_24hrs)

if price_change_in_24hrs < -1:
    news = get_news()["articles"][0]
    mail(news, current_price, price_change_in_24hrs)
