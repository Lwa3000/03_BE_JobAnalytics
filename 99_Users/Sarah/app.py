from flask import Flask, jsonify, render_template
import pandas as pd
import numpy as np

# DO ALL CLEANING IN JUPYTER, THEN PASTE HERE
# ======================================

#import file
job_data = pd.read_csv('Job_Data.csv')
job_data = job_data.dropna(how="any")

# function to extract only cities from location column
def split_record(location):
    ret_val = location
    if ("NY" in location):
        ret_val = location.split(", NY")[0]
    else:
        if "CA" in location:
            ret_val = location.split(", CA")[0]
    return ret_val

#add column 'city'
job_data["City"] = job_data["Location"].map(split_record)

# addtl cleaning
job_filtered = job_data.loc[job_data["City"] != "New York State"]



# this is your x axis on line 31
x = ["New York", "Brooklyn", "Manhattan", "Upton", "San Francisco", "Redwood City", "Oakland", "San Mateo", "San Bruno", "Foster City", "South San Francisco"]

location_count = job_filtered["City"].value_counts()
location_dict = location_count.to_dict()
ny = int(location_dict["New York"]) # remember to cast all ints
brk = int(location_dict["Brooklyn"]) # remember to cast all ints
man = int(location_dict["Manhattan"])
upton = int(location_dict["Upton"])
sf = int(location_dict["San Francisco"])
rdw = int(location_dict["Redwood City"])
oak = int(location_dict["Oakland"])
smto = int(location_dict["San Mateo"])
sbr = int(location_dict["San Bruno"])
fst = int(location_dict["Foster City"])
south = int(location_dict["South San Francisco"])
# your y axix on line 32
y = [ny, brk, man, upton, sf, rdw, oak, smto, sbr, fst, south]

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