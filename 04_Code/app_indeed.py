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
    db.drop_all()
    db.create_all()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/view2")
def view2display():
    return render_template("view2.html")


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

@app.route("/api/view2")
def view2():
    results = db.session.query(DataAnalyticsJob.title, DataAnalyticsJob.location).all()

    view2_data = scrape_page.get_view2_data(results)
    # print(view2_data)
    titles = list(view2_data.index)
    percentages = list(view2_data["Percentage"])
    plot2_data = {
        "labels": titles,
        "values": percentages,
        "type": "pie"
    }
    return jsonify(plot2_data)

if __name__ == "__main__":
    app.run()
    