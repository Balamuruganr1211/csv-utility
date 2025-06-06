# Flask CSV Utility

A simple Flask web application to upload and process CSV files with operations like filtering, sorting, aggregation, and palindrome counting.

## Features

- Upload CSV files via web interface
- Filter rows by column with operators (`>`, `<`, `==`, `contains`)
- Sort rows by selected column (ascending/descending)
- Aggregate numeric columns (`sum`, `avg`, `min`, `max`)
- Count palindrome entries in a selected column that consist solely of the letters A, D, V, B, and N.
- Download processed CSV results

## Technologies Used

- Python 3.11
- Flask
- Pandas
- Docker

## Getting Started

### Prerequisites

- Docker installed on your machine (for Docker deployment)
- Python 3.11 and pip (for running locally)

### Running with Docker

1. Build the Docker image or use can skip when using my image from Docker Hub:
   - Clone the repository and navigate into it.
   - docker build -t flask-csv-utility .

2. docker run -p 5000:5000 flask-csv-utility -d (or) docker run -p 5000:5000 balamuruganram1211/csv-utility:latest -d

3. Open your browser and go to http://localhost:5000

### Running Locally(Without Docker)
1. Clone the repository and navigate into it.

2. Create and activate a virtual environment:
    - python3 -m venv venv
    - source venv/bin/activate 

3. Install dependencies:
    - pip install -r requirements.txt

4. Run the Flask app:
    - flask run

5. Open your browser and visit http://localhost:5000

### Tests
To run tests, use:
   python -m unittest discover
