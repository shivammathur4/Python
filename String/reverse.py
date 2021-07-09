'''
@Author: Shivam Mathur
@Date: 2021-07-08
@Last Modified by: Ranjith G C
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