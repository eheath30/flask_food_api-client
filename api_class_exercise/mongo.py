from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
app.config["MONGO_URI"] = "mongodb+srv://flaskexercise:flaskexercise@flaskexercise.rkhk2ye.mongodb.net/?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route("/")
def home_page():
    online_users = mongo.db.test.find({"test": "test1"})
    print(online_users)
