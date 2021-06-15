'''
@Author:Shivam Mathur
@Date:2021-06-14
@Last Modified by:Shivam Mathur
@Title:String Replacement Replacing Username with Name

'''
'''
    Description:
        Takes input from user for Username.
    Parameters:
        No parameters.
    Return:
        Returns the name.
 '''

templateString = "Hello <<UserName>> How are you ? "
while(1):
    userName = input("Enter the UserName\n")
    if( len(userName) >= 3 ):
        break;
    else:
        print("The length of the name should be atleast 3")

newTemplateString = templateString.replace("<<UserName>>",userName)
print(newTemplateString)



