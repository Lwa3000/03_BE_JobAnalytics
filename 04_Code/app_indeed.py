# Goal: To do the tasks for homework 13, but with Indeed website instead of NASA websites.
# Result: Was able to display at least 1 position for the job search: 'Data Engineer'.
# Future work: - To display all 16 positions on 1 page for the job search.
#              - To also gather data from other search results. 

import os
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_page
import flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from skills_info import get_skills



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/datanalyticsjobs.sqlite"

db = SQLAlchemy(app)

# Define a JobPosition class
### BEGIN SOLUTION
class DataAnalyticsJob(db.Model):
    __tablename__ = "job_position"
    
    id =db. Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    company = db.Column(db.String) 
    location = db.Column(db.String) 
    description = db.Column(db.Text) 
    search_city = db.Column(db.String) 
    link = db.Column(db.String) 
    



@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/scrape")
def scrape():
    #positions = mongo.db.dataanalyst
    positions_data = scrape_page.scrape()
    print("Finalizing process..")
    try:
        db.session.bulk_insert_mappings(DataAnalyticsJob, positions_data)
        db.session.commit()
        print("Done")
    except:
        db.session.rollback()

    
   # print(positions_data)
    #print(len(positions_data))
    #for item in positions_data:
     #   positions.update(
      #      {},
       #     item,
         #   upsert=True
        #)
    return jsonify(positions_data)







##### DOLLY ADDED CODE #####

@app.route("/data")
def data():
    
    city1 = "New York"
    city2 = "San Francisco"
    
    results = db.session.query(DataAnalyticsJob.search_city, DataAnalyticsJob.description).all()

    job_desc1 = []
    job_desc2 = []

    [job_desc1.append(result[1]) for result in results if result[0] == city1]
    [job_desc2.append(result[1]) for result in results if result[0] == city2]

    city1_skills = get_skills(city1, job_desc1)
    city2_skills = get_skills(city2, job_desc2)

    skills_df = pd.merge(city1_skills, city2_skills, how='outer', on='skill_type', left_index=True, right_index=True)
    skills_df = skills_df.rename(columns={str(city1)+"_count":"city1", str(city2)+"_count":"city2"})
    skills_df = skills_df.fillna(value=0)

    return jsonify(skills_df.to_dict(orient="records"))






if __name__ == "__main__":
    app.run()
    