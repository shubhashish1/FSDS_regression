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