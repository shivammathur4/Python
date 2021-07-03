'''
@Author:Shivam Mathur
@Date:2021-07-03
@Last Modified by:Shivam Mathur
@Title:Coupon Generator
'''

# Importing random module to generate random numbers.
import random



class CouponGenerator:
    '''
    this function genrates unique random coupon numbers
    
    take numberofvalues as parameters
    
    return uniqueCoupon
    '''
    def randomCoupon(self, numberOfValues):
        # Initializing a blank list to be filled by random coupon numbers.
        uniqueCoupon = []
        # Logic for generating unique random coupon numbers.
        for i in range(numberOfValues):
            randomNumber = random.randrange(10000, 20000)
            if randomNumber not in uniqueCoupon:
                uniqueCoupon.append(randomNumber)
        return uniqueCoupon


# Taking user input of the N number of coupons to be generated.
numberOfValues = int(input('Enter N coupon numbers to be generated: '))
# Creating object generate of class CouponGenerator.
generate = CouponGenerator()
# Calling the randomCoupon function by passing the numberOfValues as parameter.
print(f'The {numberOfValues} uniques coupon number are: {generate.randomCoupon(numberOfValues)}')
