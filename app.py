# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

model = joblib.load("student_mark_predictor.pkl")



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    global df
    
    input_features = [int(x) for x in request.form.values()]
    features_value = np.array(input_features)
    
    #validate input hours
    if input_features[0] <=0 or input_features[0] >13:
        return render_template('index.html', prediction_text='Invalid Input!!! Please enter valid hours')
        

    output = model.predict([features_value])[0][0].round(2)


    return render_template('index.html', prediction_text='You will get {}% marks, when you study {} hours per day '.format(output, int(features_value[0])))


if __name__ == "__main__":
   
    app.run(host='0.0.0.0', port=8080)
    
