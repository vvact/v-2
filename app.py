from flask import Flask,render_template,jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))      
    jobs = []
    for row in result.all():
        jobs.append(dict(row))
    return jobs
    
   

@app.route('/')
def home():
    jobs = load_jobs_from_db()
    return render_template("home.html",jobs =jobs,company_name = ' LocalJobs')

@app.route('/jobs')
def list_jobs():
    return jsonify(load_jobs_from_db)


if __name__ == '__main__':
  app.run(debug=True)