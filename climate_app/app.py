from flask import Flask, jsonify
import pandas as pd
import numpy as np
from sqlHelper import SQLHelper

#################################################
# Flask Setup
################################################
app = Flask(__name__)
sql = SQLHelper()
#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
	"""List all available routes."""
	return (
		f"Available Routes:<br/>"
		f"/api/v1.0/precipitation<br/>"
		f"/api/v1.0/stations<br/>"
		f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

#precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    data = sql.query_precipitation()
    return(jsonify(data))

#stations
@app.route("/api/v1.0/stations")
def stations():
    data = sql.query_stations()
    return(jsonify(data))

#tobs
@app.route("/api/v1.0/tobs")
def tobs():
    data = sql.query_tobs()
    return(jsonify(data))

#start date
@app.route("/api/v1.0/<start>")
def stats_start(start):
    data = sql.query_stats_start(start)
    return(jsonify(data))

#start/end date
@app.route("/api/v1.0/<start>/<end>")
def stats_start_end(start, end):
    data = sql.query_stats_start_end(start, end)
    return(jsonify(data))

# Run the App
if __name__ == '__main__':
    app.run(debug=True)