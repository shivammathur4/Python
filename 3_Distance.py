'''
@Author:Shivam Mathur	
@Date:2021-06-11
@Last Modified by:Shivam Mathur
@Last Modified time:7:00 PM
@Title: Euclidian Distance Between origin and Cartesian Co-oridnates  
'''
import math
x,y = [int(x) for x in input("Enter X and Y coordinates ").split()]
#calculating Euclidean Distance
distanceBetweenPoints = math.sqrt(math.pow(x,2) + math.pow(y,2))
print("The distance of the points from the origin is ",round(distanceBetweenPoints,2)) 

