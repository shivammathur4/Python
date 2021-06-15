'''
@Author:Shivam Mathur
@Date:2021-06-14
@Last Modified by:Shivam Mathur
@Title:Count Percentage of Heads and Tails

'''
'''
    Description:
        Takes input from user for no of times coin flip.
    Parameters:
        No parameters.
    Return:
        Returns the head and tail percentage.
 '''
import random 

try:
    numberOfFlips = int(input("Enter the number of times you want to flip the coin "))
    if( numberOfFlips < 0 ):
        raise Exception
    #Total count
    totalCount = 0
    countHead = 0
    while( totalCount < numberOfFlips ):
        flip = random.random()
        if ( flip > 0.5 ):
            countHead += 1
        totalCount += 1
    headPercentage = (countHead / totalCount) * 100
    print("Percentage of Head is {0:.2f}".format(headPercentage))
    tailPercentage = ((totalCount - countHead) / totalCount) * 100
    print("Percentage of Tail is {0:.2f}".format(tailPercentage))

except(Exception):
    print("Enter a positive number")
    
    


