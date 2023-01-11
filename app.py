from flask import Flask, jsonify, render_template
import numpy as np
from bson import json_util, ObjectId
import json
import pandas as pd

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.heart_db

# Drops collection if available to remove duplicates
# db.heartData.drop()

# Set route
@app.route("/")
def home():
    return render_template("/index.html")

# @app.route("/")
# def welcome():
#     return (f"Available Routes: <br>"
#     f"/api/mongoData"
#     )

@app.route("/apiMongo")
def get_data():
    # Store the entire heartData in a list
    heartData = list(db.heartData.find())
    finalData = []
    for data in heartData:
        del data['_id']
        finalData.append(data)
    
    return jsonify(finalData) 

@app.route ("/api/mvf")
def mvf():
    heartData = list(db.heartData.find())
    finalData = []
    for data in heartData:
        del data['_id']
        finalData.append(data)

    df = pd.DataFrame(finalData)
    male = df[df['Sex'] == 'Male']
    male.head()
    male['HeartDisease'].value_counts()

    male_no = male['HeartDisease'].value_counts()['No']
    male_no

    male_yes = male['HeartDisease'].value_counts()['Yes']
    male_yes

    male_per = (male_yes /(male_no+male_yes))
    male_per

    df = pd.DataFrame(finalData)
    female = df[df['Sex'] == 'Female']
   
    female['HeartDisease'].value_counts()
    female_no = female['HeartDisease'].value_counts()['No']
    
    female_yes = female['HeartDisease'].value_counts()['Yes']
    
    female_per = (female_yes /(female_no + female_yes))
    female_per

    gender = {"male":male_per, "female": female_per}

    return jsonify(gender)


if __name__ == "__main__":
    app.run(debug=True)