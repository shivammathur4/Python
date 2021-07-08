'''
@Author: Shivam Mathur
@Date: 2021-07-06
@Last Modified by: Shivam Mathur
@Title : Iteration over sets
'''
from loggers import logger
'''
Iteration over sets
'''
def iterate_set():
    
    
        try:
            item = set([0, 1, 2, 3, 4, 5])
            for n in item:
                print(n)
        except Exception as ex:
            logger.error(ex)

iterate_set() 