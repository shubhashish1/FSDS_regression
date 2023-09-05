import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object

@dataclass
class DataTransformationConfig: # Here we will be creating the pkl file for the artifact
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')

# Now we need to create the DataTransformation class and save the transformed data into pkl
# through DataTransformationConfig class in artifacts
class DataTransformation:

    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_obj(self):
        try:
            logging.info("data transformation started")

            # Let's get the details of the features need to be encoded vs scaled
            numerical_column = ['carat', 'depth', 'table', 'x', 'y', 'z']
            categorical_column = ['cut', 'color', 'clarity']
            logging.info("Numerical and Categorical columns separated for transformation")

            # Define the categories with their sequence for the ranking

            cut_categories = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_category = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']
            logging.info("Categorical features sorted in order for the encoding")

            logging.info("pipelione initiated")
            logging.info("Starting numerical pipeline for numerical feature transformation")
            numerical_pipeline = Pipeline(

                steps=[  # steps to perform for the pipeline
                    ('imputer', SimpleImputer(strategy='median')),  # Here 'imputer' is the imputation variable required
                    ('scaler', StandardScaler())
                ]
            )
            logging.info("numerical feature transformation pipeline created")

            logging.info("Starting categorical feature transformation")
            categorical_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('ordinalencoder', OrdinalEncoder(categories=[cut_categories, color_categories, clarity_category])),
                    ('scaler', StandardScaler())
                ]
            )
            logging.info("Categorical feature transformation pipeline created")

            # Now let's combine our numerical and categorical pipeline

            logging.info("combining the numerical and categorical feature transformation pipelines")
            preprocessor = ColumnTransformer([
                ('numerical_pipeline', numerical_pipeline, numerical_column),
                ('categorical_pipeline', categorical_pipeline, categorical_column)
            ])

            return preprocessor

            logging.info("Categorical and Numerical feature transformation pipelines combined")
            logging.info("pipeline completed")
        except Exception as e:
            logging.error("exception occured with error".format(str(e)))
            raise CustomException(e,sys)

        # Now let's apply these pipelines to the train and test data

    def initiate_data_transformation(self,train_path,test_path):
        try:
            logging.info("Applying the transformation to train and test data")

            # Reading the data

            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Reading the train and test data completed")

            logging.info(f"Training data head : \n {train_df.head().to_string()}")
            logging.info(f"Testing data head : \n {test_df.head().to_string()}")

            logging.info("Obtaining data preprocessing object")

            preprocessing_obj = self.get_data_transformation_obj()

            target_column_name = 'price'
            drop_columns = [target_column_name,'Unnamed: 0']

            input_feature_train_df = train_df.drop(drop_columns,axis=1)
            target_feature_train_df = train_df[target_column_name]

            logging.info(f"The input training feature dataframe is : \n {input_feature_train_df.head().to_string()}")

            input_feature_test_df = test_df.drop(drop_columns,axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info(f"The input testing feature dataframe is : \n {input_feature_test_df.head().to_string()}")

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            save_object(file_path=self.data_transformation_config.preprocessor_obj_file_path,
                        obj=preprocessing_obj)
            # With this we will have our pickle file created and saved in the artifacts folder

            logging.info("preprocessor pickle object created and saved in artifacts folder")

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            # In train_arr we are combining the training X and y togethere in to an array

            logging.info("applying preprocessing to training and testing data")

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )


        except Exception as e:
            logging.error("Exception occured".format(str(e)))
            raise CustomException(e,sys)