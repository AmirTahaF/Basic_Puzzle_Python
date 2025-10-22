# Write a Python program that accepts a list of integers 
# calculates the length and the fifth element. 
# Return true if:
#    the length of the list is 8  
#    the fifth element occurs thrice in the said list.


def check_rules(lis):
    if (len(lis) == 8 and 
        lis.count(lis[4]) == 3):
        return True
    else:
        return False

testList1 = [19, 19, 15, 5, 5, 5, 1, 2] # True 
testList2 = [19, 15, 11, 7, 5, 6, 2] # False 

