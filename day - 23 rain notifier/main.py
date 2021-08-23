import requests
import smtplib

url = "https://api.openweathermap.org/data/2.5/onecall"
key = "424b256b216be74c30e3c755c91088c9"

parameter = {
    "lat": 21.182659,
    "lon": 81.379669,
    "appid": key,
    "exclude": "current,minutely,daily"
}
response = requests.get(url=url, params=parameter)
data = response.json()

rain = False
weather_slice = data["hourly"][:12]
id_list = [int(data["weather"][0]["id"]) for data in weather_slice]

for _ in id_list:
    if _ < 700:
        rain = True
if rain:
    my_email = "admin@pixelpaste.net"
    password = "Krevory123@"
    connection = smtplib.SMTP("smtp.hostinger.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="bobbobpvp@gmail.com",
        msg=f"From:Admin@pixelpaste.net\nSubject:IT WILL RAIN\n\n Its going to rain today keep an umbrella with you"
    )
    connection.close()
