'''
@Author:Shivam Mathur
@Date:2021-07-03
@Last Modified by:Shivam Mathur
@Title:Clinic Management Application
'''

import random
stakeAmount = int(input('Enter the stake amount '))
betAmount = int(input('Enter the bet amount '))
goalAmount = int(input('Enter the goal amount '))
countWin = 0
countLost = 0
#Starting game
while(1):
    """"
    0 - lost bet amount
    1 - gain bet amount
    """
    bet = random.randint(0,1)
    if( bet == 0 ):
        print("Oops !!! You lost")
        stakeAmount -= betAmount
        countLost += 1
    else:
        print("Congrats!!!! You Won ")
        stakeAmount += betAmount
        countWin += 1
    print("You stake amount is ",stakeAmount)
    
    if(stakeAmount == goalAmount):
        print("You have reached your goal amount")
        break;
    elif(stakeAmount <= 0 ):
        print("You have lost your whole money...Game Stops")
        break;

percentageWin = (countWin / (countWin + countLost)) * 100
percentageLose = (countLost / (countWin + countLost)) * 100
print("The winning percentage is ",round(percentageWin,2))
print("The losing percentage is ",round(percentageLose,2))
        
