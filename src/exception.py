import sys
from src.logger import logging

def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exe_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message=f"Error occured in python script name [{0}] line number [{1}] error message[{2}] ".format()(
    file_name,exc_tb.tblineno,str(error)
    
    )
    return error_message
    
class CustomException(Exception):
    def __init_(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_details=error_details)
        
    def __str__(self):
        return self.error_message
    
    
    
