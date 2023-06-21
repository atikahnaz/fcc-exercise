from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'KL',
        'salary': 'RM5000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'KL',
        'salary': 'RM4000'
    },
    {
        'id': 3,
        'title': 'Back End Engineer',
        'location': 'KL',

    },
    {
        'id': 4,
        'title': 'Front End engineer',
        'location': 'KL',
        'salary': 'RM4000'
        
    }

]


@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='Atikah')

# also can use route from api
#@app.route("/api/jobs")
#def list_jobs():
    #return jsonify(JOBS)

if __name__ == "__main__":
    app.run('0.0.0.0', debug= True)
   

