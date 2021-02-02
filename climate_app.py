# 1. Import dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import scipy as stats

import datetime as dt

from flask import Flask, jsonify
################
# Database Set-Up
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# Reflect an existing database into a new model
Base = automap_base()
# Reflect the tables
Base.prepare(engine, reflect =True)
# Save reference to the tables
measurement = Base.classes.measurement
station = Base.classes.station

################
# Flask Set-Up
################

# 2. Create an app, being sure that we are passing __name__ 
app = Flask(__name__)

# 3. 
@app.route("/")
def home():
    return (
        f"Welcome to the Climate API!<br/>"
        f"<br/>"
        f"Available Routes:<br/>"
        f"<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start/<start><br/>"
        f"/api/v1.0/start/end/<start><end><br/>"
        f"<br/>"
        f"*Enter dates in YYYY-MM-DD format.<br/>"
        f"*Example: /api/v1.0/start/2015-08-27/end/2016-01-27<br/>"
        f"<br>"
        f"Note: Data acquistion for start and end dates must be<br/>"
        f"within the date ranges of 2010-01-01 and 2017-08-23."
    )

# 4. API STATIC ROUTE (precipitation route)
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    results = session.query(measurement.date, measurement.prcp).all()
    session.close()

    prcp_data = []
    for date, prcp, in results:
        prcp_dict = {}
        prcp_dict['date'] = date
        prcp_dict['prcp'] = prcp
        prcp_data.append(prcp_dict)
    
    return jsonify(prcp_data)

# 5. API STATIC ROUTE (Stations route)
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(measurement.station).\
        group_by(measurement.station).all()
    session.close()

    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

# 6. API STATIC ROUTE (tobs route)
@app.route("/api/v1.0/tobs")
def temperatures():
    session = Session(engine)
    year_date = dt.datetime(2016, 8, 18)
    results = session.query(measurement.date, measurement.tobs).\
        filter(measurement.station == 'USC00519281').\
        filter(measurement.date > year_date).all()
    session.close()

    station_temps = list(np.ravel(results))
    
    return jsonify(station_temps)

# 7. API DYNAMIC ROUTE (start route) processing (ref= chinook_db)
@app.route("/api/v1.0/start/<start>")
def start(start):
    session = Session(engine)

    year, month, day = map(int, start.split('-'))
    date = dt.date(year, month, day)
    
    results = session.query(measurement.date, func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
        filter(measurement.date >= date).\
        group_by(measurement.date).\
        order_by(measurement.date).all()
    session.close()    
    date_selection = list(np.ravel(results))

    return jsonify(date_selection)

# 8. API DYNAMIC ROUTE (start/end route)
@app.route("/api/v1.0/start/<start>/end/<end>")
def start_end(start, end):
    session = Session(engine)

    year, month, day = map(int,start.split('-'))
    date = dt.date(year, month, day)

    year, month, day = map(int,end.split('-'))
    end_date = dt.date(year, month, day)

    results = session.query(measurement.date, func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
        filter(measurement.date >= date).\
        filter(measurement.date <= end_date).\
        group_by(measurement.date).\
        order_by(measurement.date).all()
    session.close()    
    date_selection = list(np.ravel(results))

    return jsonify(date_selection)

# Define our main behavior
if __name__ == "__main__":
    app.run(debug=True)