'''
@Author: Shivam Mathur
@Date: 2021-07-08
@Last Modified by: Shivam mathur
@Title : Program Aim to check the length of a string
'''
from logger import logger

def length():
    '''
    Description:
        This function finds the length of a string.
    '''

    try:
        str = "Shivam"
        return(len(str))
    except Exception as ex:
        logger.error(ex)    