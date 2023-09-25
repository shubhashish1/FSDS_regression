"""
This file we have created to write all the generic reusable codes say reading the data
from any source say sql,mongodb,csv etc
So utils file include all the functionalities that we think are reusable in different other
files and classes.
"""

import os
import sys
import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logging

from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import pickle

def save_object(file_path, obj): # file_path for pickle file path, obj is the preprocessor object
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as f:
            pickle.dump(obj,f)
    except Exception as e:
        logging.error("pickle file didn't create due to : ".format(str(e)))
        raise CustomException(e,sys)


def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            # Train the model
            model.fit(X_train,y_train)

            #Predict train data
            y_train_pred = model.predict(X_train)

            #Predict Test the data
            y_test_pred = model.predict(X_test)

            # Get r2 score for train and test data
            train_model_score = r2_score(y_train,y_train_pred)
            test_model_score = r2_score(y_test,y_test_pred)
            report[list(models.keys())[i]] = test_model_score # Key value pair
        return report

    except Exception as e:
        raise CustomException(e,sys)
        logging.error(f"Model evaluation failed with error : {str(e)}")

def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.error("file not loaded successfully")
        raise CustomException(e,sys)