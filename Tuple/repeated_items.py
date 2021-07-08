'''
@Author: Shivam Mathur
@Date: 2021-07-06
@Last Modified by: Shivam Mathur
@Title : Find the repeated items of a tuple
'''
from loggers import logger
'''
Find the repeated items of a tuple
'''
def repeated_items():
    try:
        sampletuple = 2,4,5,6,9,8,10,5,5
        return(sampletuple)
        count = sampletuple.count(4)
        return(count)
    except Exception as ex:
     logger.error(ex)

print(repeated_items())         
