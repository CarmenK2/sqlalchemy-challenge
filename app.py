import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)


# Save reference to the table
Measurement =Base.classes.measurement

Station =Base.classes.station

session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>")

@app.route("/api/v1.0/precipitation")
def prcp():

    select = [Measurement.date,Measurement.prcp]
    twelve_mths_ago = session.query(*select).\
    filter(func.strftime("%Y-%m-%d",Measurement.date) >= '2016-08-23').\
    order_by(Measurement.date).all()

    outcome =list(np.ravel(twelve_mths_ago))

    return jsonify(outcome)

@app.route("/api/v1.0/stations")
def stations():

    Count_station =session.query(Measurement.station,func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()
    
    return jsonify(Count_station)

@app.route("/api/v1.0/tobs")
def



if __name__ == '__main__':
    app.run(debug=True)