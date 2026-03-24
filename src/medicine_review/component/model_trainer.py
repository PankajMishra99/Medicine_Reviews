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

@dataclass
class ModelTrainerConfig:
    model_trainer_config_path = os.path.join(os.getcwd(),'artifacts','train_data.pkl')
    similarity_matrix_path = os.path.join(os.getcwd(),'artifacts','similarity.pkl') 

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self,x_train):
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
    
    def recommnadation_system(self,review,raw_data_path,top_n=1):
        try:
            raw_data= pd.read_csv(raw_data_path)
            data_transformer = DataTransformation()
            vector = data_transformer.model_transformation_config_path
            #  test to numerical data
            review = vector.transform([review]) 
            cosine_sim = self.model_trainer_config.similarity_matrix_path
            sim=cosine_sim(review,raw_data['clean_review'])
            sim_score = list(enumerate(sim[0]))
            sim_score = sorted(sim_score, key=lambda x: x[1], reverse=True)
        
            top_idx = [i[0] for i in sim_score[:top_n]]
        
            result = raw_data.iloc[top_idx].copy()
        
        # condition index se nikalna
            result['condition'] = raw_data.index[top_idx]
            return result['drugName'][0]
        
        except Exception as e:
            raise CustomException(e,sys)
    




