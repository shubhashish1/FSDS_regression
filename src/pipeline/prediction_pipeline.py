import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd

class PredictPipeline:

    def __init__(self):
        pass

    def predict(self,features):
        try:
            """ In the prediction pipeline we need to load the model for the prediction.
                Also we need to first load the preprocessor then the model to predict output."""
            preprocessor_path = os.path.join('artifacts','preprocessor.pkl')
            # This kind of code will run in both linux and windows where as
            # preprocessor_path = "artifacts/preprocessor.pkl" will work only in windows
            model_path = os.path.join('artifacts','model.pkl')

            """Now we have the pkl files. So we need to load them which is a common function.
               So need to write in the utils.py"""
            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)

            return pred

        except Exception as e:
            logging.error("Exception occured in predction.")
            raise CustomException(e,sys)


    """Now to call the predict() we need to create the 'features' also. So for that we will have a class"""

class CustomData:
    def __init__(self,
                carat:float,
                depth:float,
                table:float,
                x:float,
                y:float,
                z:float,
                cut:str,
                color:str,
                clarity:str):

        self.carat = carat
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z
        self.cut = cut
        self.color = color
        self.clarity = clarity

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'carat':[self.carat],
                'depth':[self.depth],
                'table':[self.table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity]
            }

            df = pd.DataFrame(custom_data_input_dict)
            logging.info("prediction input dataframe created successfully")
            return df
        except Exception as e:
            logging.error("Exception occur while creating prediction input dataframe")
            raise CustomException(e,sys)
