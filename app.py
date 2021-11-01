from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def welcome():
    return 'Here we go! deployed to heroku!'


if __name__=='__main__':
    app.run()