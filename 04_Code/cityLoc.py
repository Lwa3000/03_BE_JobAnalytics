from flask import Flask, jsonify, render_template
import pandas as pd
import numpy as np

# DO ALL CLEANING IN JUPYTER, THEN PASTE HERE
# ======================================



# function to extract only cities from location column
def split_record(location):
    ret_val = location.split(",")[0]
    # if ("NY" in location):
    #     ret_val = location.split(", NY")[0]
    # else:
    #     if "CA" in location:
    #         ret_val = location.split(", CA")[0]
    return ret_val

def run_location():
#import file
    job_data = pd.read_csv('../03_Data/Job_Data.csv')
    job_data = job_data.dropna(how="any")

#add column 'city'
    job_data["City"] = job_data["location"].map(split_record)

# addtl cleaning
    job_filtered = job_data.loc[job_data["City"] != "New York State"]



# this is your x axis on line 31
    x = ["New York", "Brooklyn", "Manhattan", "Upton", "San Francisco", "Redwood City", "Oakland", "San Mateo", "San Bruno", "Foster City"]


    location_count = job_filtered["City"].value_counts()
    location_dict = location_count.to_dict()
    y = []
    for value in x:
        try:
            loc = int(location_dict[value])
            y.append(loc)
        except:
            loc = 0
            y.append(loc)

# ny = int(location_dict["New York"]) # remember to cast all ints
# brk = int(location_dict["Brooklyn"]) # remember to cast all ints
# man = int(location_dict["Manhattan"])
# upton = int(location_dict["Upton"])
# sf = int(location_dict["San Francisco"])
# rdw = int(location_dict["Redwood City"])
# oak = int(location_dict["Oakland"])
# smto = int(location_dict["San Mateo"])
# sbr = int(location_dict["San Bruno"])
# fst = int(location_dict["Foster City"])
# south = int(location_dict["South San Francisco"])
# # your y axix on line 32
# y = [ny, brk, man, upton, sf, rdw, oak, smto, sbr, fst, south]
    
    data = [{
        "x": x,
        "y": y,
        "type": "bar" ,
        "marker": {
        "color": ['#1ED2FF', '#00A7D2', '#007EA7', '#00577E', '#F736B9', '#FFBBFF', '#EB24AE', '#D3009A', '#B0007B', '#8E005E', '#6C0043'],
        "opacity": 1
            }
        }]

    return data

# ======================================

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template('index.html')


# @app.route("/bar")
# def test():
#     data = [{
#         "x": x,
#         "y": y,
#         "type": "bar" 
#         }]

#     return jsonify(data)

# if __name__ == "__main__":
#     app.run(debug=True)