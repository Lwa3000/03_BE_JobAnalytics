# Goal: To do the tasks for homework 13, but with Indeed website instead of NASA websites.
# Result: Was able to display at least 1 position for the job search: 'Data Engineer'.
# Future work: - To display all 16 positions on 1 page for the job search.
#              - To also gather data from other search results. 



from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_page

app = Flask(__name__)

mongo = PyMongo(app)


@app.route("/")
def index():
    cursor_position = mongo.db.dataanalyst.find_one()
    return render_template("index.html", positions_1=cursor_position)


@app.route("/scrape")
def scrape():
    #positions = mongo.db.dataanalyst
    positions_data = scrape_page.scrape()
    print("Finalizing process..")
   # print(positions_data)
    #print(len(positions_data))
    #for item in positions_data:
     #   positions.update(
      #      {},
       #     item,
         #   upsert=True
        #)
    return jsonify(positions_data)


if __name__ == "__main__":
    app.run(debug=True)
