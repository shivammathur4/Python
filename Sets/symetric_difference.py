'''
@Author: Shivam Mathur
@Date: 2021-07-06
@Last Modified by: Shivam Mathur
@Title : This function will give symmetric difference of two sets.
'''
from loggers import logger
def symmentricdifferenceofsets():
    """
    This function will give symmetric difference of two sets. 
    """
    set1 = {1,2,3,4,5}
    set2 = {6,7,8,9,1,2,3}
    try:
        
        symm_diff = set1.symmetric_difference(set2)
        print(symm_diff)
    except Exception as ex:
        logger.error(ex)

symmentricdifferenceofsets()