'''
@Author:Shivam Mathur
@Date:2021-06-11
@Last Modified by:Shivam Mathur
@Last Modified time: 4:00 PM
@Title: Take Input in 2D array and print 2D array
'''

def two_d_array():
    '''	
    Description:	    
        Takes input from user for row and column of 2D Matrix.	        
    Parameters:	        
        No parameters.	    
    Return:	
        List of row and column.	    
    '''

     # take number of rows and columns fom user
    num_of_rows = int(input("enter number of rows: "))
    num_of_columns = int(input("enter number of columns: "))
    final_array = []
    for i in range(0,num_of_rows):
        final_array.append([])

    for i in range(0, num_of_rows):
        for j in range(0, num_of_columns):
            num = int(input(f"enter value for row {i} column {j} "))
            final_array[i].append(num)
    print(final_array)
two_d_array()
