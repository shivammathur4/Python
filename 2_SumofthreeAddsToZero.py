'''
@Author:Shivam Mathur
@Date:2021-06-11
@Last Modified by:Shivam Mathur
@Last Modified time: 6:00 PM
@Title: Sum of three integers add to zero
'''
Description:	    
        Run three nested loops with loop counter i, j, k and check  if the sum of elements at i’th, j’th, k’th is equal to zero or not.
'''           
       

def findTriplets(arr, n):
 
    found = False
    for i in range(0, n-2):
     
        for j in range(i+1, n-1):
         
            for k in range(j+1, n):
             
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True
     
             
    
    if (found == False):
        print(" not exist ")
 

arr = [0, -1, 2, -3, 1]
n = len(arr)
findTriplets(arr, n)
