"""
Here we will be writing the custom exception
"""

import sys
from src.logger import logging

def error_message_detail(error, error_detail : sys):
    _,_,exc_tb = error_detail.exc_info() # Exc_info returns 3 arguments
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = f"Error occured in python script name [{file_name}] line_number [{exc_tb.lineno}] and" \
                    f"error mesaage [{error}] "

    return error_message

class customException(Exception): # Here it inherits from Exception super class
    def __init__(self,error_message, error_detail: sys):
        super().__init__(error_message) # Here we are importing the init of the Exception class
        self.error_message = error_message_detail(error_message = error_message,error_details = error_detail)

    def __str__(self):
        return self.error_message