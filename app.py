from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [
    {
        "id": 1,
        "title": "Frontend Developer",
        "company": "Tech Corp",
        "location": "Remote",
        "salary": "$70,000 - $90,000",
        "type": "Full-time"
    },
    {
        "id": 2,
        "title": "Backend Developer",
        "company": "InnovateX",
        "location": "New York, NY",
        "salary": "$80,000 - $100,000",
        "type": "Full-time"
    },
    {
        "id": 3,
        "title": "UI/UX Designer",
        "company": "Creative Minds",
        "location": "San Francisco, CA",
        "salary": "$60,000 - $85,000",
        "type": "Part-time"
    },
    {
        "id": 4,
        "title": "Software Engineer",
        "company": "CodeLab",
        "location": "Seattle, WA",
        "salary": "$90,000 - $120,000",
        "type": "Full-time"
    },
    {
        "id": 5,
        "title": "DevOps Engineer",
        "company": "CloudWorks",
        "location": "Austin, TX",
        "salary": "$95,000 - $130,000",
        "type": "Full-time"
    },
  
]

@app.route("/")
def home():
    return render_template('home.html', Jobs = jobs )

@app.route("/api/jobs")
def json():
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)

print(jobs)