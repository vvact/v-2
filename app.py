from flask import Flask



app = Flask(__name__)


@app.route('/')
def hello():
    return"<H1>This the home page and wellcome to our new home page<H1>"


if __name__ == '__main__':
    app.run(debug=True)