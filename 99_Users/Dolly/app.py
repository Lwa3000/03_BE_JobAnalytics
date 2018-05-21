from skills_info import get_skills

from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/pie")
def sf_skills():

    skills = get_skills("San Francisco")
    labels, values = zip(*skills.items())

    data = [{
        "labels": labels,
        "values": values,
        "type": "pie"
        }]

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
