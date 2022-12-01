#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iatacode"] == "":
    from flight_search in FlightSearch
print()

