import os
import logging
from datetime import datetime


# 1.log file ka datetime m format likhgye.
LOG_FILE=f"{datetime.now().strftime("%m,%d,%Y,%H,%M,%S")}.log"

# fir log_path bano jaha usko save karna
log_path=os.path.join(os.getcwd(),'logs',LOG_FILE)

# or usko folder m save karegye.
os.makedirs(log_path,exist_ok=True)

LOG_PATH_FILE=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_PATH_FILE,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
    
)