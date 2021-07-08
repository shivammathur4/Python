'''
@Author: Shivam Mathur
@Date: 2021-07-06
@Last Modified by: Shivam Mathur
@Title : This function will intersect two sets.
'''
from loggers import logger
def intersectsection():
    """
    This function will intersect two sets. 
    """
    
    set1 = {1,2,3,4,5}
    set2 = {6,7,8,9,1,2,3}
    try:
        # use intersection() method to get intersection of two sets
        intersection_set = set((set1.intersection(set2)))
        print(intersection_set)
    except Exception as ex:
        logger.error(ex)

intersectsection()