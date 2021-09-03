import flight_search
import smtplib
fl = flight_search.Flight_Search()

fl.get_price()
fl_data = fl.flight_data
current_price = fl.prices
listed_price = fl.prices_l

count = 0
cheap_flight_index = []
print(fl_data)
print(current_price)
print(listed_price)

for price in listed_price:
    if int(current_price[count]) < int(price):
        index = current_price.index(current_price[count])
        my_email = "admin@pixelpaste.net"
        msg = f"your flight from {fl_data[index]['origin_city']} to {fl_data[index]['destination_city']} is now available for {fl_data[index]['price']}"
        password = "Krevory123@"
        connection = smtplib.SMTP("smtp.hostinger.com", 587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="bobbobpvp@gmail.com",
            msg=f"From:Admin@pixelpaste.net\nSubject:Flight Price Alert\n\n {msg}"
        )
        connection.close()
    count += 1

for i in cheap_flight_index:
    print(fl_data[i])


