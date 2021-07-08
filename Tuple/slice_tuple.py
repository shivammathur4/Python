'''
@Author: Shivam Mathur
@Date: 2021-07-06
@Last Modified by: Shivam Mathur
@Title : Slice a tuple
'''

from loggers import logger
tuple1 = (1, 2, 3, 4, 5, 6)
def slice_tuple():
        '''
        Slice a tuple
        '''
try:
    slice_this = tuple1[3:5]
    print(slice_this)
except Exception as ex:
    logger.error(ex)
    
    

slice_tuple()          
