import googlemaps
import requests
import datetime
import os # Import the os module

# --- CONFIGURATION ---
# IMPORTANT: It's better to get the API key from an environment variable for security.
# On your terminal, run: set MAPS_API_KEY="YOUR_KEY_HERE"
MAPS_API_KEY = os.environ.get("MAPS_API_KEY", "AIzaSyAepmwW_kCKM2pJmeaHv0rnG3HgPyhvfzI")
CLOUD_RUN_URL = "https://project-vahana-api-977755135273.asia-south1.run.app"

# Define two points in Mumbai
origin = "Chhatrapati Shivaji Maharaj Terminus, Mumbai"
destination = "Bandra Worli Sea Link, Mumbai"
# --- END CONFIGURATION ---

# Initialize the Google Maps client
# FIX 1: Use the variable MAPS_API_KEY, not the raw string.
gmaps = googlemaps.Client(key=MAPS_API_KEY)

# Get the current time
now = datetime.datetime.now()

# Request directions and traffic information
print(f"Requesting directions from {origin} to {destination}...")
directions_result = gmaps.directions(origin,
                                     destination,
                                     mode="driving",
                                     departure_time=now)

# Extract the travel time in traffic
duration_in_traffic_seconds = directions_result[0]['legs'][0]['duration_in_traffic']['value']
duration_in_traffic_text = directions_result[0]['legs'][0]['duration_in_traffic']['text']

print(f"Current travel time: {duration_in_traffic_text}")

# Prepare the data to send to your API
traffic_data = {
    "timestamp": now.isoformat(),
    "origin": origin,
    "destination": destination,
    "duration_seconds": duration_in_traffic_seconds
}

# Send the data to your Cloud Run API's /traffic endpoint
# FIX 2: Use the CLOUD_RUN_URL variable in the f-string correctly.
print(f"Sending data to {CLOUD_RUN_URL}/traffic...")
try:
    # FIX 3: Use the CLOUD_RUN_URL variable here as well.
    response = requests.post(f"{CLOUD_RUN_URL}/traffic", json=traffic_data)
    response.raise_for_status()  # Raise an exception for bad status codes
    print("Data sent successfully!")
    print("API Response:", response.json())
except requests.exceptions.RequestException as e:
    print(f"Error sending data: {e}")