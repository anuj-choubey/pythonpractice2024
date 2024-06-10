import requests
from geopy.distance import geodesic

def get_current_location():
    response = requests.get('http://ipinfo.io/json')
    data = response.json()
    location = data['loc'].split(',')
    latitude = float(location[0])
    longitude = float(location[1])
    return latitude, longitude

def compare_locations(current_location, target_location):
    distance = geodesic(current_location, target_location).kilometers
    return distance

if __name__ == "__main__":
    # Get current location
    current_lat, current_lon = get_current_location()
    print(f"Current location: Latitude = {current_lat}, Longitude = {current_lon}")

    # Define target location (example: London coordinates)
    target_location = (51.5074, -0.1278)

    # Compare locations
    current_location = (current_lat, current_lon)
    distance = compare_locations(current_location, target_location)

    print(f"Distance to target location: {distance:.2f} km")

