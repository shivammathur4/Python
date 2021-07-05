'''
@Author:Shivam Mathur
@Date:2021-07-05
@Last Modified by:Shivam Mathur
@Title: Add key to dictionary.
'''


def add_key_to_dict(dict1,dict2,dict3):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        dictk={}
        for d in (dict1,dict2,dict3):
            dictk.update(d)
        return dictk
    except Exception as ex:
        print(ex)

dictNew=add_key_to_dict({1:20},{2:10},{3:30})

def iterate_dictionary(dict):
    '''
    Description:
    Parameters:
    Returns:
    '''
    try:
        for item in dict.items():
            print(item)
    except Exception as ex:
        print(ex)

iterate_dictionary(dictNew)

