import os
import googlemaps
import requests
import datetime

# Get environment variables
MAPS_API_KEY = os.environ.get("MAPS_API_KEY")
FIRESTORE_PROJECT_ID = os.environ.get("GCP_PROJECT")

# Initialize clients outside the function for efficiency
from google.cloud import firestore
gmaps = googlemaps.Client(key=MAPS_API_KEY)
db = firestore.Client(project=FIRESTORE_PROJECT_ID)

def fetch_traffic_data(request):
    """
    Cloud Function to fetch traffic data and save it to Firestore.
    """
    # Define two points in Mumbai
    origin = "Chhatrapati Shivaji Maharaj Terminus, Mumbai"
    destination = "Bandra Worli Sea Link, Mumbai"
    now = datetime.datetime.now()

    try:
        # Request directions and traffic information
        directions_result = gmaps.directions(origin, destination, mode="driving", departure_time=now)

        # Extract the travel time
        duration_in_traffic_seconds = directions_result[0]['legs'][0]['duration_in_traffic']['value']

        # Prepare the data to save
        traffic_data = {
            "timestamp": now, # Firestore handles datetime objects correctly
            "origin": origin,
            "destination": destination,
            "duration_seconds": duration_in_traffic_seconds
        }

        # Save data to Firestore
        doc_ref = db.collection('traffic_data').document()
        doc_ref.set(traffic_data)

        message = f"Successfully fetched and saved data with doc ID: {doc_ref.id}"
        print(message)
        return message, 200

    except Exception as e:
        error_message = f"Error: {e}"
        print(error_message)
        return error_message, 500