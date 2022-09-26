from flight_data import FlightData
import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/"
TEQUILA_API_KEY = "FPqNpck_4QEVhL3a399277vHlvAmM2Ol"

class FlightSearch:

    def get_destination_code(self, city_name):
        header = {
            "apikey":TEQUILA_API_KEY
                }
        query = {
        "term":city_name,
        "location_types": "city"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}locations/query", headers=header, params=query)
        code = response.json()["locations"][0]['code']
        return code

    def flight_search(self, origin_city_code, destination_city_code,
                            from_time, to_time):
        header = {
            "apikey": TEQUILA_API_KEY
        }

        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 15,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}v2/search", headers=header, params=query)

        try:
            data = response.json()["data"][0]
            print(f"{destination_city_code} {data['price']}")
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(url=f"{TEQUILA_ENDPOINT}v2/search", headers=header, params=query)
            data = response.json()["data"][0]

        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )


            return flight_data

