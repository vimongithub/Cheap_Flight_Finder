import requests
from pprint import pprint

SHEETY_ENDPOINT = "https://api.sheety.co/2d4d7c92237422808898ccfa36114183/flightDeals/sheet1"

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data["sheet1"]
        return self.destination_data

    def update_destination_data(self):
        for row in self.destination_data:
            new_data = {
                "sheet1" : {
                    "iataCode" : row["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{row['id']}", json=new_data)
            print(response.text)
