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



######## Dolly code #########

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
    app.run(debug=True)
