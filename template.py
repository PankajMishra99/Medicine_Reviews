import os 
import sys 
import logging 
from pathlib import Path

project_name= 'medicine_review'
logging.basicConfig(level=logging.INFO) 

list_of_files = [
     f"artifacts/",
    f"notebooks/",
    f"src/{project_name}/component/__init__.py",
    f"src/{project_name}/component/data_ingestion.py",
    f"src/{project_name}/component/data_transformation.py",
    f"src/{project_name}/component/model_trainer.py",
    f"src/{project_name}/component/feature_selection.py",
    f"src/{project_name}/component/model_monitoring.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/testing_pipeline.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/exception.py", 
    f"src/{project_name}/utiles.py",
    "app.py",
    "main.py",
    "setup.py",
    "Dockerfile",
    "requirements.txt",
]

for file_path in list_of_files: 
    filepath = Path(file_path)
    filedir,filename = os.path.split(filepath) 

    if filedir !='':
        os.makedirs(filedir,exist_ok=True) 
        logging.info(f"Creating filedir {filedir} and filename is {filename}")
    
    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        pass 
        logging.info(f"creating empty file {filepath}") 
    else:
        logging.info(f"Filename {filename} has been already creadted..")
