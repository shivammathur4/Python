'''
@Author: Shivam Mathur
@Date: 2021-07-06
@Last Modified by: Shivam Mathur
@Title : Create the colon of a tuple
'''
from loggers import logger
from copy import deepcopy
'''
Create the colon of a tuple
'''
def colon_of_tuple():
    try:
        #create a tuple
        mytuple = ("HELLO", 5, [], True) 
        return("Original tuple",mytuple)
        #make a copy of a tuple using deepcopy() function
        tuple_colon = deepcopy(mytuple)
        tuple_colon[2].append(50)
        return("Copy of original tuple with modified :",tuple_colon)
    except Exception as ex:
        logger.error(ex) 

print(colon_of_tuple())         