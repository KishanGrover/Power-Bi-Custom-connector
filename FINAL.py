from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

from flask import Flask, render_template, redirect, url_for, request
from flask import Flask,jsonify
import json
@app.route('/')
def welcome():
    return redirect('/authenticate')


@app.route('/home', methods=['GET','POST'])
# Route for handling the login page logic
def home():
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
		
            for data in x:
              a.append(data)
            return json.dumps(a, default=str)
        else:
            return "wrong username or password enter no results to display"
        #return 'Url entered successfully'
    return render_template('login.html', error=error)
@app.route('/homee', methods=['GET','POST'])
# Route for handling the login page logic
def homee():
    error = None
    if request.method == 'POST':
        import pymongo
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        if request.form['username'] == 'riya' and request.form['password'] == 'riya':
            

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


# Route for handling the login page logic
@app.route('/authenticate', methods=['GET', 'POST'])
def authenticate():
    error = None
    if request.method == 'POST':
        if request.form['Gateway'] == 'http://localhost:5000' and request.form['Token'] == 'ajhfuwgh83ye814719ifhfir87r923rufijfifh34':
            return redirect(url_for('homee'))
            
            
        elif request.form['Gateway'] == 'http://localhost:5000' and request.form['Token'] == 'ajlefhlqhfiu4979410419797iahrfieyrqr99u':
            return redirect(url_for('home'))
            
        else:
            return "Invalid token or gateway"
    return render_template('authenticate.html', error=error)


if __name__ == '__main__':
    app.run(host='localhost', port=5000)  