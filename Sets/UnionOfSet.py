'''
@Author: Shivam Mathur
@Date: 2021-07-06
@Last Modified by: Shivam Mathur
@Title : Create a union of sets
'''
from loggers import logger
def unionofset():
        '''
        Create a union of sets
        '''
set1 = {1,2,3,4,5}
set2 = {6,7,8,9,1,2,3}
try:
        
        union_set = set1.union(set2)
        print(union_set)
except Exception as ex:
        logger.error(ex)

unionofset()