# Validate the input list is or not a sudoku
# 
# 
# correct = [[1,2,3],
#            [2,3,1],
#            [3,1,2]]

# incorrect = [[1,2,3,4],
#              [2,3,1,3],
#              [3,1,2,3],
#              [4,4,4,4]]

# incorrect2 = [[1,2,3,4],
#              [2,3,1,4],
#              [4,1,2,3],
#              [3,4,1,2]]

# incorrect3 = [[1,2,3,4,5],
#               [2,3,1,5,6],
#               [4,5,2,1,3],
#               [3,4,5,2,1],
#               [5,6,4,3,2]]

# incorrect4 = [['a','b','c'],
#               ['b','c','a'],
#               ['c','a','b']]

# incorrect5 = [ [1, 1.5],
#                [1.5, 1]]

def check_sudoku(p):
    n = len(p) #Extract size of grid
    digit = 1 #start with 1
    while digit <= n: #Go through each digit
        i = 0
        while i < n: #Go through each row and column
            row_count = 0
            col_count = 0
            j = 0
            while j < n: #For each entry in ith row/column
                if p[i][j] == digit: #check row count
                    row_count = row_count + 1
                if p[j][i] == digit: #check column count
                    col_count = col_count + 1
                j = j + 1
            if row_count != 1 or col_count != 1:
                return False
            i = i + 1 # next row/column
        digit = digit + 1 #next digit
    return True #Nothing was wrong
        


