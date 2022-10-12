import MetaTrader5 as mt5
import time
import smtplib

Trade_Active = False
Trade_Price = "1699"
Trade_Direction = "Buy"
Upper_level = 1681
Lower_Level = 1670
Previous_Price = 0

if not mt5.initialize(path="C:\\Program Files\\MetaTrader 5 IC Markets (SC)\\terminal64.exe", login=50994288,
                      server="ICMarketsSC-Demo", password="2MvVLnHL"):
    print("Failed to connect error code = ", mt5.last_error())


def mail(alert):
    my_email = "admin@pixelpaste.net"
    msg = alert
    password = "Krevory123@"
    connection = smtplib.SMTP("smtp.hostinger.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="karanalyadav420@gmail.com",
        msg=f"From:Admin@pixelpaste.net\nSubject:Gold Price Alert\n\n {msg}"
    )
    connection.close()


while Trade_Active:
    gold_info = mt5.symbol_info_tick("XAUUSD")
    if Previous_Price - gold_info.ask >= 2:
        Previous_Price = gold_info.ask
        alert = f"\nGold Price is down 200 Points.\n"f"Current Price {gold_info.ask}\n"f"Trade Price {Trade_Price} {Trade_Direction}"
        mail(alert)
    if Previous_Price - gold_info.ask <= -2:
        Previous_Price = gold_info.ask
        alert = f"\nGold Price is up 200 Points.\n"f"Current Price {gold_info.ask}\n"f"Trade Price {Trade_Price} {Trade_Direction}"
        mail(alert)
    time.sleep(10)

while not Trade_Active:
    gold_info = mt5.symbol_info_tick("XAUUSD")
    if Upper_level - gold_info.ask <= 2:
        alert = f"\nPrice reaching your upper level {Upper_level}\n"f"Current Price {gold_info.ask}"
        mail(alert)
        quit()
    if Lower_Level - gold_info.ask  >= 2:
        alert = f"\nPrice reaching your lower level {Lower_Level}\n"f"Current Price {gold_info.ask}"
        mail(alert)
        quit()
    time.sleep(10)
