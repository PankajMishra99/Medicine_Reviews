import os 
import sys 
from src.medicine_review.logger import logging 
from src.medicine_review.exception import CustomException 
import numpy as np 
import pandas as pd 
import pickle
from sklearn.metrics import *
from dataclasses import dataclass 
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig: 
    train_data_path:str = os.path.join(os.getcwd(),'artifacts','drugsComTrain_raw','drugsComTrain_raw.csv') 
    test_data_path:str = os.path.join(os.getcwd(),'artifacts','drugsComTest_raw','drugsComTest_raw.csv')
    raw_data_path:str = os.path.join(os.getcwd(),'artifacts','raw_data',) 
    os.makedirs(raw_data_path,exist_ok=True)

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def get_ingestion_config(self):
        try:
            train_data = pd.read_csv(self.ingestion_config.train_data_path) 
            logging.info('Read train data successfully in ingestion file..')
            test_data = pd.read_csv(self.ingestion_config.test_data_path)
            logging.info('Read test data sucessfully in  ingestion file..')

            raw_data:pd.DataFrame = pd.concat([train_data,test_data],axis=0) 
            # raw_data['date'] = pd.to_datetime(raw_data['date'])
            raw_data.dropna(inplace=True)
            print(raw_data.columns)
            raw_data['total_review']  = raw_data['drugName'] + raw_data['condition'] + raw_data['clean_review']
            
            # cleaning and remove special charecter..
            raw_data['clean_review'] = (raw_data['total_review']
                      .str.lower()
                      .str.replace(r'\d','',regex=True)
                      .str.replace(r'[^\w\s]','',regex=True)
            ) 
            stop_word = stopwords.words('english')
            raw_data['clean_review'] = raw_data['clean_review'].apply(lambda x:' '.join(w for w in str(x).split() if w not in stop_word))
            raw_data['sentiment']=raw_data['rating'].apply(lambda x:'postive' if x>5 else 'negative')
            raw_data['sentiment']=raw_data['sentiment'].map({'postive':1,'negative':0})
            #  important feature selection..
            raw_data = raw_data[['clean_review','drugName','condition','sentiment','rating']] 
            raw_file_path =os.path.join(self.ingestion_config.raw_data_path,'raw_data.csv')
            raw_data.to_csv(raw_file_path,index=False,header=True) 
            logging.info('raw data saved successfully..')
            # train_data,test_data = train_test_split(raw_data,test_size=0.2,random_state=42)
            # train_data.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            # logging.info('clean train_data saved successfully..')
            # test_data.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            # logging.info('clean test data saved successfully..')
            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path 

        except Exception as e:
            raise CustomException(e,sys)

    
