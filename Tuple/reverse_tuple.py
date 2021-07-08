'''
@Author: Shivam Mathur
@Date: 2021-07-06
@Last Modified by: Shivam Mathur
@Title : Reverse a tuple
'''

from loggers import logger
tuples = ('z','a','d','f','g','e','e','k')

def reverse_tuple(tuples):
    try:
        tuple1 = tuples[::-1]
        return tuple1
    except Exception as ex:
        logger.error(ex)



print(reverse_tuple())
