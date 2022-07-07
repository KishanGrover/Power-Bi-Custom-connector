import json
from flask import Flask,jsonify
app = Flask(__name__)
@app.route('/')
def index():
    import pymongo
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Database Name
    db = client.admin

    # Collection Name
    col = db.Riya

    x = col.find()
    a=[]
    for data in x:
      a.append(data)

    return json.dumps(a, default=str)
        
    

app.run()