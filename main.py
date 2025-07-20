from flask import Flask, request, jsonify
from google.cloud import firestore
import datetime

# Initialize Firestore client
db = firestore.Client()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Project Vahana API is running!"

@app.route("/traffic", methods=['POST'])
def receive_traffic_data():
    data = request.get_json()
    print(f"Received traffic data: {data}")

    try:
        # Create a reference to a new document in the 'traffic_data' collection
        doc_ref = db.collection('traffic_data').document()
        doc_ref.set(data)
        print(f"Data saved to Firestore with document ID: {doc_ref.id}")

        return jsonify({"status": "success", "firestore_doc_id": doc_ref.id}), 200

    except Exception as e:
        print(f"Error saving to Firestore: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)