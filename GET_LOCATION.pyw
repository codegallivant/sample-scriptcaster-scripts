import geocoder
import lib.exterior_connection as exterior_connection
from geopy.geocoders import Nominatim
import socket
import os


g = geocoder.ip('me')
print(g)
print(g.latlng)

# initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")
# Latitude & longitude input
lat = str(g.latlng[0])
lng = str(g.latlng[1])

location = geolocator.geocode(f"{lat},{lng}")
# Display
print(location)

print("Authenticating with Exterior...")
client = exterior_connection.authenticate(os.path.join(os.environ['SC_APP_FOLDER_PATH'],"creds/service_account_credentials.json"))
print("Getting sheet...")
sheet = exterior_connection.open_sheet("Exterior", os.environ["SC_COMPUTER_NAME"], client)
sheet_values = sheet.get_all_values()
print("Updating Exterior...")
exterior_connection.update_parameter_value(sheet, "IP", socket.gethostbyname(socket.gethostname()), sheet_values)
exterior_connection.update_parameter_value(sheet, "IP Location Coordinates", f"({lat},{lng})", sheet_values)
exterior_connection.update_parameter_value(sheet, "IP Location", str(location), sheet_values)

print("Done.")

