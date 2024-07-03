# Weather Data API using Flask and SQLAlchemy

This project implements a RESTful API using Flask, which interacts with a SQLite database containing weather data. The API provides various endpoints to retrieve weather information, including precipitation, station lists, temperature observations (TOBs), and statistics based on date ranges.

## Setup Instructions

### Dependencies

1. Ensure Python 3.x is installed.
2. Install the required Python libraries using pip:

    ```sh
    pip install Flask SQLAlchemy pandas numpy matplotlib
    ```

### Database Setup

1. Use the provided `hawaii.sqlite` SQLite database.
2. Ensure your SQLAlchemy connection string points to this database (`sqlite:///hawaii.sqlite`).

### Running the Application

1. Start the Flask application by running:

    ```sh
    python app.py
    ```

2. The API will be accessible at `http://localhost:5000/`.

### Jupyter Notebook Setup

1. Open the provided Jupyter notebook file `climate_starter.ipynb` using Jupyter Notebook:

    ```sh
    jupyter notebook climate_starter.ipynb
    ```

2. Follow the steps outlined in the notebook to perform the climate analysis and data exploration:
    - Connect to the SQLite database.
    - Reflect the database tables into SQLAlchemy ORM classes.
    - Perform precipitation analysis.
    - Perform station analysis.

## API Endpoints

### GET /api/v1.0/precipitation

Returns a JSON object with date and precipitation data for the last 12 months.

### GET /api/v1.0/stations

Returns a JSON object listing all weather stations.

### GET /api/v1.0/tobs

Returns temperature observations (TOBs) for the most active station for the last 12 months.

### GET /api/v1.0/<start>

Returns minimum, maximum, and average temperatures from a given start date (YYYY-MM-DD).

### GET /api/v1.0/<start>/<end>

Returns minimum, maximum, and average temperatures between a start and end date (YYYY-MM-DD/YYYY-MM-DD).

## SQLHelper Class

The `SQLHelper` class encapsulates database interactions using SQLAlchemy's ORM. It includes methods to execute SQL queries and return results in JSON format for consumption by the Flask routes.

## Notes

- Ensure proper error handling for robustness, especially with database connections and query results.
- Documentation within the code (docstrings) helps in understanding each method's purpose and expected inputs/outputs.

