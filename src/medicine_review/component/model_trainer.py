import os 
import sys 
import numpy as np  
import pandas as pd 
from src.medicine_review.logger import logging 
from src.medicine_review.exception import CustomException 
from src.medicine_review.component.data_ingestion import * 
from src.medicine_review.component.data_transformation import * 
from dataclasses import dataclass 
from sklearn.metrics.pairwise import cosine_similarity
from src.medicine_review.utiles import *
@dataclass
class ModelTrainerConfig:
    model_trainer_config_path = os.path.join(os.getcwd(),'artifacts','train_data.pkl')
    similarity_matrix_path = os.path.join(os.getcwd(),'artifacts') 
    os.makedirs(similarity_matrix_path,exist_ok=True)

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self,x_train:np.ndarray):
        try:
            logging.info("Starting model training..(similairy based..)")
            similarity_score = cosine_similarity(x_train)
            logging.info('similairty matrix created successfully..')

            # save matrix.pkl 
            save_object(
                self.model_trainer_config.similarity_matrix_path,
                object=similarity_score
            ) 
            return similarity_score
        
        except Exception as e: 
            raise CustomException(e,sys)
    
    def recommnadation_system(self,review,train_vec,raw_data_path,top_n=5):
        try:
            raw_data= pd.read_csv(raw_data_path)
            data_transformer = DataTransformation()
            vector = load_object(data_transformer.data_transformat_path.model_transformation_config_path)
            #  test to numerical data
            review = vector.transform([review]) 
            logging.info("Vectorization for user review done successfully..")
            similarity_path = os.path.join(self.model_trainer_config.similarity_matrix_path,'preprocess.pkl')
            # print(similarity_path)
            # cosine_sim  = load_object(similarity_path)
            # print(cosine_sim)
            
            sim=cosine_similarity(review,train_vec)
            sim_score = list(enumerate(sim[0]))
            sim_score = sorted(sim_score, key=lambda x: x[1], reverse=True)
        
            top_idx = [i[0] for i in sim_score[:top_n]]
        
            result = raw_data.iloc[top_idx].copy()
            result = result[result['rating']==result['rating'].max()]
            # print(result)
        # condition index se nikalna
            # result['condition'] = raw_data.index[top_idx]
            return result
        
        except Exception as e:
            raise CustomException(e,sys)
    




