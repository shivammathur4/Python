'''
@Author:Shivam Mathur
@Date:2021-07-05
@Last Modified by:Shivam Mathur
@Title: Number of occurence of specified element in Array.
'''


def user_input_to_array():
    '''
    Description:
    Parameters:
    Returns:
    '''
    array=[]
    choice=''
    print("Ener any number of values to enter in array")
    while(choice.lower()!='q'):
        userValue=input("Enter value\n")
        array.append(userValue)
        print("Do you want to add more values \nPress C to continue\nQ to stop\n")
        choice=input("Enter choice\n")
    return array

def occurence_of_specific_element_array(list,userSelection):
    '''
    Description:
    Parameters:
    Returns:
    '''
    count=0
    for index in range(len(list)-1):
        if(list[index]==userSelection):
            count+=1
    return userSelection,count+1

list=user_input_to_array()
print(list)
userSelection=input("Select Element to count its occurence in list\n")

returnList=occurence_of_specific_element_array(list,userSelection)

print("Selected element %s Occurence count %s " %(returnList[0],returnList[1]))
