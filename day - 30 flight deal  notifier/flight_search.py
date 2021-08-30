from sheety import *
import requests
import datetime
from dateutil.relativedelta import relativedelta


date_now = datetime.datetime.today().strftime('%d/%m/%Y')

date_six_month = datetime.datetime.today() + relativedelta(months=+6)
date_six_month = date_six_month.strftime('%d/%m/%Y')



class Flight_Search:
    def __init__(self):
        self.sh = Sheety()
        self.citis = self.sh.citis
        self.prices_l = self.sh.prices
        self.iata = []
        self.flight_data = []
        self.prices = []

    def get_iata(self):
        for city in self.citis:
            header = {
                "apikey":"3g9YS-QlFtl6CJLjfxm0K-SmmLeyY3du",
                "Content-Type": "application/json"
            }

            endpoint = "https://tequila-api.kiwi.com/locations/query"

            params = {
                "term":{city}
            }

            response = requests.get(url=endpoint,headers=header,params=params)
            data = response.json()
            code = data["locations"][0]["code"]
            self.iata.append(code)
        return self.iata

    def update_iata(self):
        self.get_iata()
        sheety_data = self.sh.get_sheety_data()
        leng = len(sheety_data["prices"]) + 2

        header = {
            "Authorization": "Bearer Krevory123",
            "Content-Type": "application/json"
        }

        for _ in range(2,leng):
            sheety_endpoint = f"https://api.sheety.co/b12703464b519b11311d5ecf11464c42/flightDeals/prices/{_}"

            body = {
                "price": {
                    "iataCode": f"{self.iata[_-2]} ",
                }
            }
            requests.put(url=sheety_endpoint, headers=header, json=body)

    def get_price(self):
        self.update_iata()
        header = {
            "apikey": "3g9YS-QlFtl6CJLjfxm0K-SmmLeyY3du",
            "Content-Type": "application/json"
        }
        endpoint = "https://tequila-api.kiwi.com/v2/search"

        for iata in self.iata:
            params = {
                "fly_from": "LON",
                "fly_to":{iata},
                "date_from":date_now,
                "date_to":date_six_month

            }

            response = requests.get(url=endpoint, headers=header, params=params)
            data =  response.json()["data"][0]
            try:
                data_flight = {
                "price":data["price"],
                "origin_city":data["route"][0]["cityFrom"],
                "origin_airport":data["route"][0]["flyFrom"],
                "destination_city":data["route"][0]["cityTo"],
                "destination_airport":data["route"][0]["flyTo"],
                "out_date":data["route"][0]["local_departure"].split("T")[0],
                "return_date":data["route"][1]["local_departure"].split("T")[0]
                }
                self.flight_data.append(data_flight)
            except:
                self.prices.append(0)

            price = data["price"]
            self.prices.append(price)

