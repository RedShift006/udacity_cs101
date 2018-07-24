# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.
# my solution
def product_list(list_of_numbers):
    if len(list_of_numbers) == 1:
        return list_of_numbers[0]
    if len(list_of_numbers) == 0:
        return 1
    if len(list_of_numbers) > 1:
        sum = 1
        for e in list_of_numbers:
            sum *= e
        return sum

# the Udactiy solution
def product_list2(p):
    total = 1
    for e in p:
        total = total* e
    return total


# print product_list([9])
#>>> 9

#print product_list([1,2,3,4])
#>>> 24

#print product_list([])
#>>> 1

# --------------------------------------
# Quiz4

# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    greatest = 0
    for e in list_of_numbers:
        if greatest <= e:
            greatest = e
        
    return greatest




print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

    
