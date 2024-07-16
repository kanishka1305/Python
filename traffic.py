  import requests

API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'
BASE_URL = 'https://maps.googleapis.com/maps/api/directions/json'

def fetch_traffic_data(start, destination):
    params = {
        'origin': start,
        'destination': destination,
        'key': API_KEY,
        'departure_time': 'now'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data['status'] == 'OK':
        route = data['routes'][0]
        legs = route['legs'][0]
        traffic_data = {
            'traffic_conditions': legs['traffic_speed_entry'],
            'travel_time': legs['duration_in_traffic']['text'],
            'incidents': route['warnings']
        }
        return traffic_data
    else:
        raise Exception('Error fetching traffic data: ' + data['status'])

def display_traffic_data(traffic_data):
    print("Current Traffic Conditions: ")
    for condition in traffic_data['traffic_conditions']:
        print(f"  - Speed: {condition['speed']} km/h")

    print(f"Estimated Travel Time: {traffic_data['travel_time']}")

    print("Incidents or Delays: ")
    if traffic_data['incidents']:
        for incident in traffic_data['incidents']:
            print(f"  - {incident}")
    else:
        print("  - No incidents or delays reported.")

def main():
    start = input("Enter the starting point: ")
    destination = input("Enter the destination: ")

    try:
        traffic_data = fetch_traffic_data(start, destination)
        display_traffic_data(traffic_data)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
