'''
@Author: Shivam Mathur
@Date: 2021-07-06
@Last Modified by: Shivam Mathur
@Title : Add member(s) in a set
'''
from loggers import logger
def addnewmembers():
    '''
    Add member(s) in a set
    '''
    members = {1,2,3,4,5}
    try:
        members.add(10)
        return members
    except Exception as ex:
        logger.error(ex)

print(addnewmembers) 