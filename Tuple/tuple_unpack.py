'''
@Author: Shivam Mathur
@Date: 2021-07-06
@Last Modified by: Shivam Mathur
@Title : Unpack tuple in different variables 
'''
from loggers import logger
'''
Unpack a tuple in several variables
'''
def unpackTuple():
    try:
        myTuple = (int(item) for item in input("Enter the 3 integer(seprated by space) for create tuple: ").split())
        item1, item2, item3 = myTuple
        return item1, item2, item3
    except Exception as ex:
        logger.error(ex) 


print(unpackTuple())