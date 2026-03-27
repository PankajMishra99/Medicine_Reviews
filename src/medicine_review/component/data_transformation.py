import os 
import sys 
import numpy as np  
import pandas as pd 
from src.medicine_review.logger import logging 
from src.medicine_review.exception import CustomException 
from sklearn.compose import ColumnTransformer 
from sklearn.preprocessing import OneHotEncoder,OrdinalEncoder 
from dataclasses import dataclass 
from src.medicine_review.utiles import save_object
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.pipeline import Pipeline

@dataclass 
class DataTransformationConfig:
    model_transformation_config_path = os.path.join(os.getcwd(),'artifacts','preprocess.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformat_path = DataTransformationConfig() 
    
    def get_data_transformation(self): 
        try:
            pipeline = Pipeline(
                steps=[
                    ('tfidf',TfidfVectorizer(max_features=1000,
                    stop_words='english',
                    ngram_range=(1,2),
                    lowercase=True
                    ))
                ]
            )
            return pipeline
        except Exception as e:
            raise CustomException(e,sys)
    
    def initiate_data_transformer(self,train_path,test_path):
        try:
            train_data = pd.read_csv(train_path)
            logging.info('Read train data successfully..')
            test_data = pd.read_csv(test_path) 
            logging.info('Read test data successfully..')

            preporcess_obj = self.get_data_transformation()
            #  for train_data
            x_train_vector = preporcess_obj.fit_transform(train_data['clean_review'])
            #  for test_data 
            x_test_vector = preporcess_obj.transform(test_data['clean_review']) 

            save_object( self.data_transformat_path.model_transformation_config_path,
                        object=preporcess_obj
                        )
            return x_train_vector,x_test_vector 
        
        except Exception as e:
            raise CustomException(e,sys)

