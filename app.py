import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#Database set-up:

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

print(Base.classes.keys())
# Save reference to the table
station_tbl = Base.classes.station
measurement_tbl = Base.classes.measurement


app = Flask(__name__)


@app.route("/")
def Climate_Home_Page():
    return (
        f"Welcome to the Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
      )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    precips = session.query(measurement_tbl.date, measurement_tbl.prcp).all()

    session.close()

    # Create a dictionary 
    prcp_list=[]
    for date, prcp in precips:
        rain_dict = {}
        rain_dict["date"] = date
        rain_dict["prcp"] = prcp
        prcp_list.append(rain_dict)    

    return jsonify(prcp_list)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    stat_list = session.query(station_tbl.station,station_tbl.name).all()
        
    session.close()
    return jsonify(stat_list)

@app.route("/api/v1.0/tobs")
def tobs():
    tobs_list=[]
    session = Session(engine)
    tobs_lastyear = session.query(measurement_tbl.station,measurement_tbl.date,measurement_tbl.tobs).\
        filter(measurement_tbl.station =="USC00519281").\
        filter(measurement_tbl.date > "2016-08-22")

    session.close()
    for s,d,t in tobs_lastyear:
        temp_dict={}
        temp_dict["station"]=s
        temp_dict["date"] = d
        temp_dict["tobs"] = t
        tobs_list.append(temp_dict)

    return jsonify(tobs_list)


#@app.route("/api/v1.0/<start>")
#def from_when(start):
#    return jsonify(hello_dict)


#@app.route("/api/v1.0/<start>/<end>")
#def range(start, end):
#    return jsonify(hello_dict)


if __name__ == "__main__":
    app.run(debug=True)
