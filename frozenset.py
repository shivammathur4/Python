'''
@Author: Shivam Mathur
@Date: 2021-07-06
@Last Modified by: Shivam Mathur
@Title : This function uses frozen sets to store keys of dictionary.
'''
from loggers import logger
def frozen_set():
    """
    This function uses frozen sets to store keys of dictionary. 
    """
    try:
        # creating a dictionary
        dict =   {
                        "item1": "40", 
                        "item2": 30.5, 
                        "item3": "Shivam" 
                        }

        # making keys of dictionary as frozenset
        key = frozenset(dict)
        print(key)
    except Exception as ex:
        logger.error(ex)

frozen_set()


