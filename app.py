from flask import Flask, request, render_template,jsonify
import os
import sys
from src.utils import *
from src.logger import logging
from src.exception import CustomException
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline
from src.pipeline.training_pipeline import *

application = Flask(__name__)

app = application

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods = ['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':   # Here we are having GET method means we need to pass the public input
        return render_template('form.html')
    else:
        data = CustomData(
            carat=float(request.form.get('carat')),
            depth=float(request.form.get('depth')),
            table=float(request.form.get('table')),
            x=float(request.form.get('x')),
            y = float(request.form.get('y')),
            z = float(request.form.get('z')),
            cut=request.form.get('cut'),
            color=request.form.get('color'),
            clarity=request.form.get('clarity')
        )
        """Now let's convert this dict into dataframe"""
        final_new_data = data.get_data_as_dataframe()
        """Since the data is ready we will call the predict pipeline"""
        predict = PredictPipeline()
        pred = predict.predict(final_new_data)
        """Now let's display the result from the output array"""
        results = round(pred[0],2)
        return render_template('result.html',final_result = results)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)