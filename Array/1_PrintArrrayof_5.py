'''
@Author:Shivam Mathur
@Date:2021-07-05
@Last Modified by:Shivam Mathur
@Title: Print Array values using indexes.
'''


def print_array_using_index():
    '''
    '''
    try:
        array=list(input("Enter 5 number without space then enter "))
        for count in range(len(array)):
            print(array[count])
    except Exception as ex:
        print(ex)

print_array_using_index()