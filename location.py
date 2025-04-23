from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="your_app_name")  # Replace "your_app_name"

def get_airport_coordinates(airport_name):
    location = geolocator.geocode(airport_name)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

airport_name = "KLAX"
coordinates = get_airport_coordinates(airport_name)

if coordinates:
    print(f"The coordinates for {airport_name} are: Latitude {coordinates[0]}, Longitude {coordinates[1]}")
else:
    print(f"Could not find coordinates for {airport_name}")
