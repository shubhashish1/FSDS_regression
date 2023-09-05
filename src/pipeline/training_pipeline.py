from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import Model_trainer
from src.exception import CustomException
from src.logger import logging

import os
import sys
import pandas as pd

# Run Training model

if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    input_feature_train_arr,input_feature_test_arr,pkl_object = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
    model_trainer = Model_trainer()
    model_trainer.initiate_model_training(input_feature_train_arr,input_feature_test_arr)