'''
@Author:Shivam Mathur
@Date:2021-07-05
@Last Modified by:Shivam Mathur
@Title: Print Array values after reversing order.
'''


def reverseArray(array):
    '''
    Description:
    Parameters:
    Return:
    '''
    count=len(array)-1
    length=len(array)//2
    for index in range(length):
        temp=array[index]
        array[index]=array[count]
        array[count]=temp
        count-=1
    print(array)

reverseArray(['a','b','c','d'])

def reverseArray(array):
    '''
    Description:
    Parameters:
    Return:
    '''
    start=0
    end=len(array)-1
    while(start<end):
        array[start],array[end]=array[end],array[start]
        start+=1
        end-=1
    print(array)

reverseArray([1,2,3,4,5])