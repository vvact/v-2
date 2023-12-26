from flask import Flask,render_template,jsonify



app = Flask(__name__)

JOBS = [

    {
    'id' : 1,
    'title' : 'Data manager',
    'location' : 'Nairobi, Kenya',
    'salary' : 'Kes. 25000'
    },

     {
    'id' : 1,
    'title' : 'Data manager',
    'location' : 'Nairobi, Kenya',
    'salary' : 'Kes. 25000'
    },

     {
    'id' : 1,
    'title' : 'Data manager',
    'location' : 'Nairobi, Kenya',
    
    },
]


@app.route('/')
def home():
    return render_template("home.html",jobs =JOBS,company_name = ' LocalJobs')

@app.route('/jobs')
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(debug=True)