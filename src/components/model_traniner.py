import os
import pickle
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

class ModelTrainer:
    def __init__(self):
        self.model = None  # Model instance will be created later

    def initiate_model_trainer(self, train_arr, test_arr, preprocessor_path):
        # ✅ Load Preprocessor
        if not os.path.exists(preprocessor_path):
            raise FileNotFoundError(f"❌ Pickle file not found: {preprocessor_path}")

        with open(preprocessor_path, "rb") as f:
            preprocessor = pickle.load(f)

        # ✅ Train the Model
        self.model = LinearRegression()
        X_train, y_train = train_arr[:, :-1], train_arr[:, -1]
        X_test, y_test = test_arr[:, :-1], test_arr[:, -1]

        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)

        # ✅ Compute R² Score
        r2 = r2_score(y_test, y_pred)
        print(f"✅ Model Training Completed. R² Score: {r2:.4f}")

        # ✅ Save Model as model.pkl
        model_path = "artifacts/model.pkl"
        with open(model_path, "wb") as f:
            pickle.dump(self.model, f)

        print(f"✅ Model Saved Successfully: {model_path}")

        return r2

# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

# from dataclasses import dataclass
# from catboost import CatBoostRegressor
# from sklearn.ensemble import (
#     AdaBoostRegressor,
#     GradientBoostingRegressor,
#     RandomForestRegressor
# )
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import r2_score
# from sklearn.neighbors import KNeighborsRegressor
# from sklearn.tree import DecisionTreeRegressor
# from xgboost import XGBRegressor
# from src.exception import CustomException
# from src.logger import logging

# from src.utils import save_object,evaluate_models

# @dataclass
# class ModelTrainerConfig:
#     trained_model_file_path=os.path.join("artifacts","model.pkl")

# class ModelTrainer:
#     def __init__(self):
#         self.model_trainer_config=ModelTrainerConfig()
        
#     def initiate_model_trainer(self,train_array,test_array):
#         try:
#             logging.info("Spling training and test input data")
#             X_train, y_train,X_test,y_test=(
#                 train_array[:,:-1],
#                 train_array[:,-1],
#                 test_array[:,:-1],
#                 test_array[:,-1]
#             )
            
#             models = {
#                 'LinearRegression': LinearRegression(),
#                 'K-Neighbors Regressor': KNeighborsRegressor(),
#                 'Decision Tree': DecisionTreeRegressor(),
#                 'Random Forest Regressor': RandomForestRegressor(),
#                 'XGBRegressor': XGBRegressor(),
#                 'CatBoost Regressor': CatBoostRegressor(verbose=False),
#                 'AdaBoost Regressor': AdaBoostRegressor(),
#                 'Gradient Boosting':GradientBoostingRegressor()
#             }
            
            
#             model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)
#             print("Model Report:", model_report)
            
#             ## to get best model score from dict
#             best_model_score=max(sorted(model_report.values()))
            
#             ## To get best model name from dict
#             best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            
#             best_model = models[best_model_name]
            
#             if best_model_score<0.6:
#                 raise CustomException("No best mdoel found")
#             logging.info(f"Best found model on both training and testing dataset")
            
#             save_object(
#                 file_path=self.model_trainer_config.trained_model_file_path,
#                 obj=best_model
#             )
            
#             predicted=best_model.predict(X_test)
#             return r2_score(y_test,predicted)
            
#         except Exception as e:
#             raise CustomException(e,sys)
            
        

