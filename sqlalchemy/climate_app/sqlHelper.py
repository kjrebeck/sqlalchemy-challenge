import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, func

import datetime 

import pandas as pd
import numpy as np
#################################################
# Database Setup
#################################################
class SQLHelper():
	
    # Create engine using the `hawaii.sqlite` database file
	def __init__(self):
		self.engine = create_engine("sqlite:///hawaii.sqlite")
		self.Base = None

		# automap Base classes
		self.init_base()
	   
	# Declare a Base using `automap_base()`
	def init_base(self):
		# reflect an existing database into a new model
		self.Base = automap_base()
		# Use the Base class to reflect the database tables
		self.Base.prepare(autoload_with=self.engine)

		Measurement = self.Base.classes.measurement
		Station = self.Base.classes.station

	#function to return date and precipitation values previous 12 months
	def query_precipitation(self):
		Measurement = self.Base.classes.measurement

		# Create our session (link) from Python to the DB
		session = Session(self.engine)

		#12 months from most recent data point
		query_date = datetime.date(2017, 8, 23) - datetime.timedelta(days=365)

		#query
		results = session.query(Measurement.date, Measurement.prcp).\
			filter(Measurement.date >= query_date).\
			order_by(Measurement.date.asc()).all()
			
		# close session
		session.close()

		#save query to dataframe
		df = pd.DataFrame(results, columns=["Date", "Precipitation"])

		data = df.to_dict(orient="records")
		return(data)
	
	#function to return list of stations
	def query_stations(self):
		Measurement = self.Base.classes.measurement
		Station = self.Base.classes.station

		# Create our session (link) from Python to the DB
		session = Session(self.engine)

		#query 
		results = session.query(Measurement.station, Station.name).\
			join(Station, Measurement.station == Station.station).\
			group_by(Station.station).\
			order_by(func.count(Measurement.station).desc()).all()
		
		# close session
		session.close()

		df = pd.DataFrame(results, columns=["Station ID", "Station Name"])

		data = df.to_dict(orient="records")
		return(data)
	
	#function to return date and observed temperatures previous 12 months for most active station 
	def query_tobs(self):
		Measurement = self.Base.classes.measurement
		Station = self.Base.classes.station

		# Create our session (link) from Python to the DB
		session = Session(self.engine)

		#12 months
		query_date = datetime.date(2017, 8, 23) - datetime.timedelta(days=365)

		# query
		results = session.query(Measurement.date, Measurement.tobs).\
			filter(Measurement.date >= query_date).\
			filter(Measurement.station == 'USC00519281').all()

		# close session
		session.close()

		df = pd.DataFrame(results, columns=["Date", "Temperature"])
		data = df.to_dict(orient="records")
		return(data)#list
        
	
	def query_stats_start(self, start):
		Measurement = self.Base.classes.measurement

		# Create our session (link) from Python to the DB
		session = Session(self.engine)

		#start & end dates - referred to prof instructions
		start_date = datetime.datetime.strptime(start, '%Y-%m-%d')

		results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
			filter(Measurement.date  >= start_date).all()

		# close session
		session.close()

		df = pd.DataFrame(results, columns=["Min Temp", "Max Temp", "Average Temp"])

		data = df.to_dict(orient="records")
		return(data)
	
	def query_stats_start_end(self, start, end):
		Measurement = self.Base.classes.measurement

		# Create our session (link) from Python to the DB
		session = Session(self.engine)

		#start & end dates - referred to prof instructions
		start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
		end_date = datetime.datetime.strptime(end, '%Y-%m-%d')


		results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
			filter(Measurement.date  >= start_date).\
			filter(Measurement.date < end_date).all()

		# close session
		session.close()

		df = pd.DataFrame(results, columns=["Min Temp", "Max Temp", "Average Temp"])

		data = df.to_dict(orient="records")
		return(data)
