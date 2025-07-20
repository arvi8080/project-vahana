# Project Vahana: Cloud-Native Traffic Analysis Pipeline

**Project Vahana** is an end-to-end data engineering project that automatically collects, stores, and analyzes real-time traffic patterns in Mumbai using a serverless cloud architecture on Google Cloud Platform (GCP).

## Key Features

- **Automated Data Collection:** A serverless **Cloud Function** runs on a schedule via **Cloud Scheduler**, fetching live traffic data from the Google Maps API every 15 minutes.
- **Scalable Data Ingestion:** A containerized API built with **Flask** and deployed on **Cloud Run** receives and processes the incoming data.
- **Persistent Storage:** All collected traffic data is stored durably in a **Firestore** NoSQL database.
- **Data Analysis & Visualization:** A local Python script uses **Pandas** and **Matplotlib** to query the entire dataset and generate time-series plots to visualize traffic patterns and identify rush hour peaks.

## Technologies Used

- **Languages:** Python
- **Backend:** Flask
- **Cloud Platform:** Google Cloud Platform (GCP)
  - **Compute:** Cloud Run, Cloud Functions
  - **Database:** Firestore
  - **Automation:** Cloud Scheduler
- **Data Science:** Pandas, Matplotlib
- **APIs:** Google Maps Directions API
- **Version Control:** Git & GitHub

## Setup & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/arvi8080/project-vahana.git](https://github.com/arvi8080/project-vahana.git)
    cd project-vahana
    ```
2.  **Set up the Python environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # or .\venv\Scripts\activate on Windows
    pip install -r requirements.txt
    ```
3.  **Local Analysis:**
    To analyze the collected data, run the `analyze_data.py` script:
    ```bash
    python analyze_data.py
    ```
