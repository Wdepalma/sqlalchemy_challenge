from flask import Flask, jsonify


app = Flask(__Climate__)




@app.route("/")
def home():
    return "Hi"

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
    return 
    
    #hello_dict


@app.route("/api/v1.0/stations")
def stations():
    return jsonify(hello_dict)

@app.route("/api/v1.0/tobs")
def tobs():
    return jsonify(hello_dict)

@app.route("/api/v1.0/<start>")
def from_when(start):
    return jsonify(hello_dict)


@app.route("/api/v1.0/<start>/<end>")
def range(start, end):
    return jsonify(hello_dict)


if __name__ == "__main__":
    app.run(debug=True)
