"""
In this file we will have model training and evaluation both are there
"""

import numpy as np
import pandas as pd
import os
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_model

import sys
from dataclasses import dataclass

@dataclass
class Model_trainer_config:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class Model_trainer:

    def __init__(self):
        self.model_trainer_config = Model_trainer_config()

    def initiate_model_training(self,train_array,test_array):
        try:
            logging.info("Splitting train and test array")
            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            logging.info(f"X_train is {len(X_train)} and y_train is {len(y_train)}")
            print(f"X_train is {len(X_train)} and y_train is {len(y_train)}")

            models = { 
                'LinearRegression': LinearRegression(),'Lasso':Lasso(), 'Ridge':Ridge(),
                'ElasticNet':ElasticNet()
                 }

            # Evaluate model function will be under utils.py as it will be reused
            model_report:dict=evaluate_model(X_train,y_train,X_test,y_test,models)
            
            print(model_report)
            print("----------------------------------")
            logging.info(f"model report : {model_report}")

            # Now we need to have the model with best score
            best_model_score = max(sorted(model_report.values()))

            # Now let's get the best model name
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            logging.info(f"The best model is {best_model_name} with the r2 score {best_model_score}")

            save_object(self.model_trainer_config.trained_model_file_path,best_model)

            #return (best_model, best_model_score)
            print(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')


        except Exception as e:
            raise CustomException(e,sys)
            logging.error(f'Model training initiation failed with error : {str(e)}')