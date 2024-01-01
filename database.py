from sqlalchemy import create_engine,text
import os

db_connection_string = os.environ['db_connection']

engine = create_engine(
db_connection_string,
connect_args={
     "ssl": {
           
           r"C:\Users\Administrator\Downloads\cacert.pem"
           
        }
}
)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))      
    jobs = []
    for row in result.all():
        jobs.append(dict(row))
    return jobs
    