import os 
import sys  
import logging 
from datetime import datetime 

log_files = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(),'logs',log_files)
os.makedirs(log_path,exist_ok=True)

log_file_path = os.path.join(log_path,log_files) 

logging.basicConfig(level=logging.INFO,
                    filename=log_file_path,
                    format="[%(asctime)s] %(lineno)ss %(levelname)s - %(message)s"
                    )