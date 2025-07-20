import pandas as pd
from google.cloud import firestore
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Initialize Firestore client
db = firestore.Client(project="project-vahana-2025")

# Create a reference to the collection
docs_ref = db.collection('traffic_data')

# Get all documents from the collection
docs = docs_ref.stream()

print("Fetching data from Firestore...")
# Create a list to hold the data
data_list = []
for doc in docs:
    data_list.append(doc.to_dict())

if not data_list:
    print("No data found in Firestore. Let the scheduler run for a while to collect data.")
else:
    # Convert the list of dictionaries to a Pandas DataFrame
    df = pd.DataFrame(data_list)

    # --- FIX IS HERE ---
    # Convert timestamp column, forcing all values to be timezone-aware (UTC)
    df['timestamp'] = pd.to_datetime(df['timestamp'], utc=True)
    # --- END FIX ---

    df['duration_minutes'] = df['duration_seconds'] / 60

    # Sort the data by time
    df = df.sort_values(by='timestamp')

    print(f"Successfully loaded {len(df)} data points.")
    print("Latest data point:")
    print(df.tail(1))

    # --- Create the Plot ---
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(15, 7))

    ax.plot(df['timestamp'], df['duration_minutes'], marker='o', linestyle='-', label='Travel Time (minutes)')

    # Format the x-axis to be readable
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
    plt.gcf().autofmt_xdate() # Rotate date labels

    # Add titles and labels
    ax.set_title('Mumbai Traffic: CSMT to Bandra-Worli Sea Link', fontsize=16)
    ax.set_xlabel('Time', fontsize=12)
    ax.set_ylabel('Travel Time (minutes)', fontsize=12)
    ax.legend()
    plt.tight_layout()

    # Show the plot
    print("Displaying traffic pattern plot...")
    plt.show()