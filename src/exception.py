import sys
import logging
from logger import LOG_FILE_PATH

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # it gives where the error happened with line number
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = 'Error occurred in python script name [{0}] line Number [{1}] error message [{2}]'.format(file_name, exc_tb.tb_lineno, str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message

# to check working or not
# if __name__ == "__main__":
#     try:
#         a = 1 / 0
#     except ZeroDivisionError as e:
#         logging.error("An error occurred", exc_info=True)
#         raise CustomException("Division by zero error occurred", sys)







# import sys
# import logging
# from logger import LOG_FILE_PATH

# def error_message_detail(error,error_detail:sys):
#     _,_,exc_tb=error_detail.exc_info() # it gives where the error happen with line number
#     file_name=exc_tb.tb_frame.f_code.co_filename
#     error_message='Error occures in python script name[{0}] line Number [{1}] error message[{2}]'.format() 
#     file_name,exc_tb.tb_lineno,str(error)
    
#     return error_message
    
    
#     class CustomException(Exception):
#         def __init__(self,error_message,error_detail:sys):
#             super().__init(error_message)
#             self.error_message=error_message_detail(error_message,error_detail=error_detail)
        
#         def __str__(self):
#             return self.error_message
    
    
# if __name__=="__main__":
#     try:
#         a=1/0
#     except ZeroDivisionError as e:
#         logging.error("An error occurred", exc_info=True)
#         raise CustomException("Division by zero error occurred", sys.exc_info())
    
#     # except Exception as e:
#     #     logging.info("Divide by Zero")
#     #     raise CustomException(e,sys)