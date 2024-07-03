
``markdown
# Weather Data API using Flask and SQLAlchemy

## Project Overview

This project aims to perform a climate analysis on data from 9 weather stations in Honolulu, Hawaii using Python and SQLAlchemy. The steps involved include:

1. **Climate Data Analysis**:
    - Use SQLAlchemy to connect to a SQLite database.
    - Reflect the database tables and map them to SQLAlchemy ORM classes.
    - Perform precipitation and station analysis.

2. **Flask API Development**:
    - Create an API using Flask that serves the results of the climate analysis.
    - Develop endpoints to provide precipitation data, station data, temperature observations, and statistical data based on date ranges.
    
    By following these instructions, you will set up the project, run the analysis, and deploy the API successfully.
``
# Setup Instructions

## Cloning the Repository

1. Clone the repository to your local computer:

    ```sh
    git clone https://github.com/kjrebeck/sqlalchemy-challenge.git
    ```

2. Navigate to the project directory:

    ```sh
    cd sqlalchemy-challenge
    ```

## Dependencies

1. Ensure Python 3.x is installed.
2. Install the required Python libraries using pip:

    ```sh
    pip install Flask SQLAlchemy pandas numpy matplotlib
    ```
## Jupyter Notebook Setup

1. Open the provided Jupyter notebook file `climate_starter.ipynb` using Jupyter Notebook:

    ```sh
    jupyter notebook climate_starter.ipynb
    ```

2. Follow the steps outlined in the notebook to perform the climate analysis and data exploration:
    - Connect to the SQLite database.
    - Reflect the database tables into SQLAlchemy ORM classes.
    - Perform precipitation analysis.
    - Perform station analysis.

## Database Setup

1. Use the provided `hawaii.sqlite` SQLite database.
2. Ensure your SQLAlchemy connection string points to this database (`sqlite:///hawaii.sqlite`).

## Running the Application

1. Navigate to the app directory:

    ```sh
    cd climate_app
    ```

2. Start the Flask application by running:

    ```sh
    python app.py
    ```

3. The API will be accessible at `http://localhost:5000/`.

``
## API Endpoints

### GET /api/v1.0/precipitation

Returns a JSON object with date and precipitation data from 2016-08-23 through 2017-08-23

### GET /api/v1.0/stations

Returns a JSON object listing all weather station ids and names.

### GET /api/v1.0/tobs

Returns temperature observations (TOBs) for the most active station from 2016-08-23 through 2017-08-23

### GET /api/v1.0/<start>

Returns minimum, maximum, and average temperatures from a given start date (YYYY-MM-DD).

### GET /api/v1.0/<start>/<end>

Returns minimum, maximum, and average temperatures between a start and end date (YYYY-MM-DD/YYYY-MM-DD).


## Notes

- Documentation within the code (docstrings) helps in understanding each method's purpose and expected inputs/outputs.

## GNU General Public License v3.0
