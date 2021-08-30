import requests


class Sheety:
    def __init__(self):
        self.citis = []
        self.prices = []
        self.get_city_data()

    def get_sheety_data(self):
        header = {
            "Authorization": "Bearer Krevory123"
        }

        sheety_endpoint = "https://api.sheety.co/b12703464b519b11311d5ecf11464c42/flightDeals/prices"

        response = requests.get(url=sheety_endpoint, headers=header)
        return response.json()

    def get_city_data(self):
        data = self.get_sheety_data()
        rows =  data["prices"]

        for list in rows:
            self.citis.append(list["city"])
            self.prices.append(list["lowestPrice"])
