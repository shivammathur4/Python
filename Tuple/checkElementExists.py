'''
@Author: Shivam Mathur
@Date: 2021-07-06
@Last Modified by: Shivam Mathur
@Title : Check whether an element exists within a tuple
'''
from loggers import logger
def check_element_exists():
        '''
        Check whether an element exists within a tuple
        '''
        try:
            mytuple = tuple(int(item) for item in input("Enter the integer elements(seprated by space): ").split())
            element = int(input('Enter the integer which you want to check exists or not :'))
            if element in mytuple:
                return True
            return False
        except Exception as ex:
          logger.error(ex)

print(check_element_exists())          