import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#Database set-up:

engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
station = Base.classes.station
measurement = Base.classes.measurement


app = Flask(__name__)


@app.route("/")
def Climate_Home_Page():
    return (
        f"Welcome to the Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
      )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    precips = session.query(measurement.date, measurement.prcp).all()

    session.close()

    # Create a dictionary 
    prcp_list=[]
    for date, prcp in precips:
        rain_dict = {}
        rain_dict["date"] = date
        rain_dict["prcp"] = prcp
        prcp_list.append(rain_dict)    

    return jsonify(prcp_list)



#@app.route("/api/v1.0/stations")
#def stations():
#    return jsonify(hello_dict)

#@app.route("/api/v1.0/tobs")
#def tobs():
#    return jsonify(hello_dict)

#@app.route("/api/v1.0/<start>")
#def from_when(start):
#    return jsonify(hello_dict)


#@app.route("/api/v1.0/<start>/<end>")
#def range(start, end):
#    return jsonify(hello_dict)


if __name__ == "__main__":
    app.run(debug=True)
