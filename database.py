from sqlalchemy import create_engine,text

db_connection_string = "mysql+pymysql://8eb8lwqddbrtop65l8q3:pscale_pw_XaoyNUM70A6XkJLnsdenIaAaecYIo1YRZ0kFieCHE3a@aws.connect.psdb.cloud/victor?charset=utf8mb4"

engine = create_engine(
db_connection_string
)
