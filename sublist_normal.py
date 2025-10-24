"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    """
    Func to see the relation between two lists

    :param list_one: int - list of integers
    :param list_two: int - list of integers

    :return:
    SUBLIST = 1 if list_one is a sublist of list_two
    SUPERLIST = 2 if list_two is a sublist of list_one
    EQUAL = 3 if these lists have the same numbers in the same sequence
    UNEQUAL = 4 if they are nothing that listed above
    """
    if list_one == list_two:
        return EQUAL

    if len(list_one) > len(list_two):
        if len(list_two) == 0:
            return SUPERLIST
        index1 = len(list_one) - 1
        index2 = len(list_two) - 1
        for i in range(index1):
            ptr = -1
            if list_one[i] == list_two[0]:
                ptr = i
            if ptr >= 0:
                for i in range(ptr, len(list_two) + ptr ):
                    if list_one[i] == list_two[i-ptr]:#take out the second check for the beginiing of similarity
                        if i-ptr == len(list_two)-1:
                            return SUPERLIST
                        continue
                    elif i + ptr == len(list_one):
                        return UNEQUAL
                    break



    if len(list_two) > len(list_one):
        if len(list_one) == 0:
            return SUBLIST
        index1 = len(list_one) - 1
        index2 = len(list_two) - 1
        for i in range(index2):
            ptr = -1
            if list_two[i] == list_one[0]:
                ptr = i
            if ptr >= 0:
                for i in range(ptr, len(list_one) + ptr ):
                    if list_two[i] == list_one[i-ptr]:#take out the second check for the beginiing of similarity
                        if i-ptr == len(list_one)-1:
                            return SUBLIST
                        continue
                    elif i+ptr == len(list_two):
                        return UNEQUAL
                    break
    return UNEQUAL

print(sublist([1, 2, 5], [0, 1, 2, 3, 1, 2, 5, 6]))


"""Much better solution that uses capability of lists to check if they are the same 

def sublist(list_one, list_two):
    if list_one == list_two:
        return 3
    elif is_sublist(list_one, list_two):
        return 2
    elif is_sublist(list_two, list_one):
        return 1
    return 0
    
    
def is_sublist(one, two):
    for i in range(len(one) - len(two) + 1):
        if not two or two == one[i : i + len(two)]:
            return True
    return False
    
"""