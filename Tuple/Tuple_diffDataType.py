'''
@Author: Shivam Mathur
@Date: 2021-07-06
@Last Modified by: Shivam Mathur
@Title : Create a tuple with different data types
'''
from loggers import logger

'''
Create a tuple with different data types
'''
def tuplewithdiffdatatype():
    
  try:
    my_tuple = (30,40.5,'Shivam')
    return(my_tuple)
  except Exception as ex:
     logger.error(ex) 

print(tuplewithdiffdatatype())