'''
@Author: Shivam Mathur
@Date: 2021-07-06
@Last Modified by: Shivam Mathur
@Title : Create a tuple 
'''
from loggers import logger
'''
Create a tuple
'''
def create_tuple():
    try:
        my_tuple = (1,2,3)
        return my_tuple
    except Exception as ex:
     logger.error(ex) 

print(create_tuple()) 