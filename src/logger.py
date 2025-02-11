import logging
import os
from datetime import datetime

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join("logs", LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode="a",  # Append mode
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Print log file path for debugging
print(f"Logging to: {LOG_FILE_PATH}")

# Test log
logging.info("Test log: Logging is working correctly!")


# import logging
# import os
# from datetime import datetime

# LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%S')}.log"
# logs_path=os.path.join(os.getcwd(),'logs',LOG_FILE)
# os.makedirs(logs_path,exist_ok=True)

# LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    
#     level=logging.INFO,
    
# )

# #to check weather working or not
# # if __name__=="__main__":
# #     logging.info("Logging has started")