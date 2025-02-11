import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging
from src.components.data_transformnation import DataTransformation
from src.components.model_traniner import ModelTrainer

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifact", "train.csv")
    test_data_path: str = os.path.join("artifact", "test.csv")
    raw_data_path: str = os.path.join("artifact", "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Enter the data ingestion method or component")

        try:
            dataset_path = "notebook/data/stud.csv"
            if not os.path.exists(dataset_path):
                raise FileNotFoundError(f"Dataset not found at {dataset_path}")

            df = pd.read_csv(dataset_path)
            logging.info("Read the dataset into a DataFrame")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info(f"Saved raw data to {self.ingestion_config.raw_data_path}")

            logging.info("Train-test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info(f"Saved train data to {self.ingestion_config.train_data_path}")
            logging.info(f"Saved test data to {self.ingestion_config.test_data_path}")

            logging.info("Data ingestion completed successfully.")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    try:
        obj = DataIngestion()
        train_data, test_data = obj.initiate_data_ingestion()

        data_transformation = DataTransformation()
        train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(train_data, test_data)

        # ✅ Ensure Pickle File is Created
        if not os.path.exists(preprocessor_path):
            raise FileNotFoundError(f"❌ Pickle file was not created at {preprocessor_path}")

        print(f"✅ Pickle File Created: {preprocessor_path}")

        # ✅ Train the Model and Compute R² Score
        model_trainer = ModelTrainer()  # Ensure ModelTrainer is correctly initialized
        r2_score_value = model_trainer.initiate_model_trainer(train_arr, test_arr, preprocessor_path)

        print(f"🎯 Final R² Score: {r2_score_value:.4f}")

    except Exception as e:
        print(f"❌ Error: {e}")
