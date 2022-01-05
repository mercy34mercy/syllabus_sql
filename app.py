from flask import Flask
from flask import request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

DATABASE_URL = "postgres://hdskofuyufyqgx:18d75e06e7fd23852717b2f3903245d1b0691c56d8d5746fa66258e167f0019b@ec2-3-209-234-80.compute-1.amazonaws.com:5432/de5lc85kl2p0o"

@app.route('/',methods=['POST','GET'])
def index():
    return "hello world"