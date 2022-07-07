# Route for handling the login page logic
from flask import Flask, render_template, redirect, url_for, request
from flask import Flask,jsonify
import json
app = Flask(__name__)
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        import pymongo
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        if request.form['username'] == 'kishan' and request.form['password'] == 'kishan':
                  # Database Name
            db = client["Kishan"]

            # Collection Name
            col = db["Kishan"]

            x = col.find()
            #print(type(x))
            a=[]
            for data in x:
                a.append(data)

            return json.dumps(a, default=str)
        elif request.form['username'] == 'riya' and request.form['password'] == 'riya':
            

        # Database Name
            db = client["admin"]

            # Collection Name
            col = db["Riya"]

            x = col.find()
            print(type(x))
            a=[]
            for data in x:
                a.append(data)

            return json.dumps(a, default=str)
        else:
            return "wrong username or password enter no results to display"
        #return 'Url entered successfully'
    return render_template('login.html', error=error)
app.run()