'''
@Author: Shivam Mathur
@Date: 2021-07-06
@Last Modified by: Shivam Mathur
@Title : Slice a tuple
'''

from loggers import logger
def slice_tuple():
        '''
        Slice a tuple
        '''
        try:
            mytuple = tuple(int(item) for item in input("Enter the integer elements(seprated by space): ").split())
            start = int(input('Enter the start index where you want to start for slicing :'))
            stop = int(input('Enter the last index where you want to stop for slicing :'))
            sliceList = []    # store the tuple element after slicing
            for index in range(start,stop):       # For tuple slicing also use myTuple[start:stop:step]
                sliceList.append(mytuple[index])
            return tuple(sliceList)
        except Exception as ex:
            logger.error(ex)

print(slice_tuple())           