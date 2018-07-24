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


# Quiz8

def check_sudoku(list):
    list_len = len(list)
    all_list = []
    i = 1
    
    sum_all_list_index = list_len*(list_len+1)/2 - list_len
    while list_len > 0:
        all_list.append(i)
        list_len = list_len -1
        i = i + 1
    print all_list
    
    is_sudokou = False
    
    print sum_all_list_index
    
    while not is_sudokou:
        is_sudokou = do_test_in_per_row(list, all_list, sum_all_list_index)
            
    print is_sudokou
    
    
def do_test_in_per_row(list, all_list, sum_all_list_index):
    list_len = len(list)
    e_len = 0
    for e in list:
        e_len = len(e)
        i = 0
        sum_e_index = 0
        while i < e_len:
            if all_list.index(e[i]) != -1:
                sum_e_index += all_list.index(e[i])
                i = i + 1
            else:
                return False
        if sum_e_index != sum_all_list_index:
            return False
    return True
            
        

    
print check_sudoku(incorrect)
