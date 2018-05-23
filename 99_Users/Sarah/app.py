from flask import Flask, jsonify, render_template
import pandas as pd
import numpy as np

# DO ALL CLEANING IN JUPYTER, THEN PASTE HERE
# ======================================

df = pd.read_csv("Job_Data.csv")

# this is your x axis on line 31
x = ["New York, NY", "New York State"]

location = df["Location"].value_counts()
location_dict = location.to_dict()
ny = int(location_dict["New York, NY"]) # remember to cast all ints
nys = int(location_dict["New York State"]) # remember to cast all ints
# your y axix on line 32
y = [ny, nys]

# ======================================

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/bar")
def test():
    data = [{
        "x": x,
        "y": y,
        "type": "bar" 
        }]

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)