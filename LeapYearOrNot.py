'''
@Author:Shivam Mathur
@Date:2021-06-14
@Last Modified by:Shivam Mathur
@Title:Leap year or not

'''
'''
    Description:
        Takes input from user for the year.
    Parameters:
        No parameters.
    Return:
        Returns the year leap or not.
 '''

try:
    year = int(input("Enter the year "))
    if ( len(str(year)) != 4 ):
        raise Exception
    #For a year to be a leap year,it should be divsible for 4 and not by 100 ar divisible for 400
    if( (year % 4 == 0 and year % 100 !=0) or  (year % 400 == 0) ):
        print("It's a leap year")
    else:
        print("It's not a leap year")
        
except(Exception):
    print("Please Enter a 4 digit number")

