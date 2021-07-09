'''
@Author: Shivam Mathur
@Date: 2021-07-08
@Last Modified by: Shivam mathur
@Title : Program for uppercase and lowercase
'''
from logger import logger

try:
    inputString = input('Enter something: ')
    print({inputString.upper()})
    print({inputString.lower()})
except Exception:
    logger.error("Invalid Input")