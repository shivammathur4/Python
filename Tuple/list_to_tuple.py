'''
@Author: Shivam Mathur
@Date: 2021-07-06
@Last Modified by: Shivam Mathur
@Title : Convert a list to a tuple
''' 
from loggers import logger
def listToTuple():
        '''
        Convert a list to a tuple
        '''
        try:
            myList = [int(item) for item in input("Enter the list of integer elements(seprated by space) : ").split()]
            return tuple(myList)
        except Exception as ex:
         logger.error(ex) 

print(listToTuple())         
