import requests
from pprint import pprint
API_ENDPOINT = "https://api.sheety.co/eb18b540be8e98c9e5d41d71afc68708/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=API_ENDPOINT)
        response.raise_for_status()
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "prices": {
                    "iataCode": city["iatacode"]
                }
            }
            response = requests.put(
                url=f"{API_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
