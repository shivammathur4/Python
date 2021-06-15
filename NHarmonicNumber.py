'''
@Author:Shivam Mathur
@Date:2021-06-14
@Last Modified by:Shivam Mathur
@Title:Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N

'''
'''
    Description:
        Takes input from user for nth harmonic no.
    Parameters:
        No parameters.
    Return:
        Returns the nth term and nth number.
 '''

nthNumber=0
try:
    nthTerm=int(input(" Enter nthTerm for Harmonic nth Number\n"))
    for count in range(1,(nthTerm+1)):
        nthNumber+=(1/count)
    print("nthNumber {0} for nthTerm {1}".format(nthNumber,nthTerm))
except Exception as ex:
    print(ex.__class__)
