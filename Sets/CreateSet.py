'''
@Author: Shivam Mathur
@Date: 2021-07-06
@Last Modified by: Shivam Mathur
@Title : Create a set
'''
from loggers import logger
def create_set():
        '''
        Create a set
        '''
        try:
            new_set = set([1,2,3,4])
            return new_set
        except Exception as ex:
            logger.error(ex)

print(create_set())        