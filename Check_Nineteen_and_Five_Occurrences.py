# Write a Python program to : 
# find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five.
# Return True otherwise False.

# Input: [19, 19, 15, 5, 3, 5, 5, 2]
# Output: True

# Input: [19, 15, 15, 5, 3, 3, 5, 2]
# Output: False


list1 = [19,19,15,5,2,5,5,2]
list2 = [19,15,15,5,3,3,5,2]

def Check(lis):

    if (lis.count(19) == 2 and lis.count(5) >= 3):
        return True
    else : 
        return False



