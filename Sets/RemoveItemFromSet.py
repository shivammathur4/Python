'''
@Author: Shivam Mathur
@Date: 2021-07-06
@Last Modified by: Shivam Mathur
@Title : Remove items from set
'''
from loggers import logger
def remove_items():
 

my_set = {1,2,3,4,5}
try:
    my_set.discard(5)
    print(my_set)
except Exception as ex:
        logger.error(ex)



remove_items()          