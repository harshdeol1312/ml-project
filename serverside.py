import numpy as np
import pandas as pd
from flask import Flask,redirect,session,abort,jsonify
from flask import request, render_template,flash
from models import Model

import os

app = Flask(__name__)


@app.route('/')
def root():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')

@app.route('/login', methods=['POST'])
def alogin():
    if request.form['password'] == 'python' and request.form['username'] == 'pycharm':
        session['logged_in'] = True
    else :
        flash('username or password in incorrect')
    return root()


@app.route("/logout")
def alogout():
    session['logged_in'] = False
    return root()


@app.route('/predict', methods=["POST"])
def predict():
    q1 = int(request.form['a1'])
    q2 = int(request.form['a2'])
    q3 = int(request.form['a3'])
    q4 = int(request.form['a4'])
    q5 = int(request.form['a5'])
    q6 = int(request.form['a6'])
    q7 = int(request.form['a7'])
    q8 = int(request.form['a8'])
    q9 = int(request.form['a9'])
    q10 = int(request.form['a10'])

    values = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    model = Model()
    classifier = model.svm_classifier()
    prediction = classifier.predict([values])
    if prediction[0] == 0:
            result = 'You are not depressed '
    if prediction[0] == 1:
            result = 'You have slight depression'
    if prediction[0] == 2:
            result = 'You have mild deression'
    if prediction[0] == 3:
            result = 'You have moderate depression'
    if prediction[0] == 4:
            result = 'You have severe depression'
    return render_template("result.html", result=result)

app.secret_key = os.urandom(10)
app.run(port=5833, host='0.0.0.0', debug=True)