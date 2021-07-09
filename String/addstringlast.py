'''
@Author: Shivam Mathur
@Date: 2021-07-08
@Last Modified by: Shivam
@Title : Program to add "ing" at last
'''


from logger import logger
def add_string(str1):
    try:
        length = len(str1)
            if length > 2:
                if str1[-3:] == 'ing':
                str1 += 'ly'
                else:
                str1 += 'ing'

            return str1
    except Exception as ex:
        logger.error(ex)  

print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))