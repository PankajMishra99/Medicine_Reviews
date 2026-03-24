import os 
import sys 
from src.medicine_review.logger import logging 
from src.medicine_review.exception import CustomException 
import numpy as np 
import pandas as pd 
import pickle
from sklearn.metrics import *

def read_df():
    try:
        train_df = os.path.join(os.dirname(os.getcwd(),'artifacts','drugsComTrain_raw','drugsComTrain_raw.csv'))
        logging.info("Read traing data successfull..")
        test_df = os.path.join(os.dirname(os.getcwd(),'artifacts','drugsComTest_raw','drugsComTest_raw.csv'))
        logging.info('Read test data successfull..')
        return train_df, test_df 
    except Exception as e:
        raise CustomException(e,sys) 

def save_object(file_path,object): 
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True) 

        with open(file_path,'wb') as file:
            pickle.dump(object,file) 
            logging.info("Model saved successfull..")
    except Exception as e:
        raise CustomException(e,sys) 


def evaluate_model(x_train,x_test,y_train,y_test,models,param): 
    try:
        report={}
        for i in range(list(models.keys())):
            model = list(models.keys())[i] 

            model.fit(x_train,y_train)
            
            y_train_pred = model.predict(x_train) 
            y_test_pred = model.predict(x_test)

            train_model_score = f1_score(y_train,y_train_pred) 
            test_model_score=f1_score(y_test,y_test_pred) 

            report[list(models.keys())[i]] =test_model_score 
        return report 
    
    except Exception as e:
        raise CustomException(e,sys) 
