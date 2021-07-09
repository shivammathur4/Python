'''
@Author: Shivam Mathur
@Date: 2021-07-08
@Last Modified by: Shivam
@Title : Program to reverse a string
'''
from logger import logger

def reverse():
    '''
    Description:
        This function reverses a string
    '''
    try:
    
        s = "Shivam"
        string = s[::-1]
        print(string)
    
    except Exception:
        logger.error("Invalid Input") 

reverse()