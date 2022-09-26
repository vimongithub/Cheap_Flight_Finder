from data_manager import DataManager
from flight_search import FlightSearch
from pprint import  pprint
from datetime import datetime,timedelta
from notification import NotificationManager

ORIGIN_CITY_IATA = "LON"

notification_manager = NotificationManager()
data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row['city'])

    data_manager.destination_data = sheet_data
    data_manager.update_destination_data()

tommorow = (datetime.now() + timedelta(1)).strftime("%d/%m/%Y")
date_after_six_month = (datetime.now() + timedelta(days=6*30)).strftime("%d/%m/%Y")

for destination in sheet_data:
    flight = flight_search.flight_search(ORIGIN_CITY_IATA, destination["iataCode"],
                                         tommorow, date_after_six_month)

    if flight is None:
        continue
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"low price alert! only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-"
                    f"{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )

