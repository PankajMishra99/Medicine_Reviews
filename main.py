import os , sys  
from src.medicine_review.logger import logging 
from src.medicine_review.exception import CustomException
from src.medicine_review.component.data_ingestion import * 
from src.medicine_review.component.data_transformation import * 
from src.medicine_review.component.model_trainer import * 

if __name__=="__main__":
    logging.info("Program excuted..") 
    try:
        # data ingestion
        ingestion = DataIngestion() 
        train_data_path, test_data_path  = ingestion.get_ingestion_config() 

        #  data transformation 
        data_transformer= DataTransformation()
        train_arr, test_arr = data_transformer.initiate_data_transformer(train_data_path, test_data_path) 

        #  model trainer 
        model_trainer = ModelTrainer() 
        recomend = model_trainer.recommnadation_system(review='chest pain and breathing issue',train_vec = train_arr,raw_data_path=train_data_path) 
        # logging.info('Recommend DrugName :',recomend)
        
    except Exception as e: 
        raise CustomException(e,sys)



