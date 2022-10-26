# min conflicts solver for NQueens problems
from time import sleep
size = 8
from copy import copy, deepcopy
our_matrix = [[0 for x in range(size)] for y in range(size)]
# columns[r] is a number c if a queen is placed at row r and column c.

stack = []
import random  # hint -- you will need this for the following code: column=random.randrange(0,size)


def display():
    for row in range(size):
        for column in range(size):
            if our_matrix[column][row] == 1:
                print('♛', end=' ')
            else:
                print(' .', end=' ')
        print()



number_of_moves = 0  # where do I change this so it counts the number of Queen moves?
number_of_iterations = 0

def place_in_next_row(column, row):
    matrix_copy = deepcopy(our_matrix)
    stack.append(matrix_copy)
    our_matrix[column][row] = 1
    for i in range(size):
        if i is not row:
            our_matrix[column][i] = 2
    for j in range(size):
        if j is not column:
            our_matrix[j][row] = 2

    # check diagonal
    row_check = row
    col_check = column
    while row_check > 0 and col_check > 0:
        row_check -= 1
        col_check -= 1
        our_matrix[col_check][row_check] = 2

    row_check = row
    col_check = column
    while row_check < size - 1 and col_check < size - 1:
        row_check += 1
        col_check += 1
        our_matrix[col_check][row_check] = 2

    row_check = row
    col_check = column
    while row_check > 0 and col_check < size - 1:
        row_check -= 1
        col_check += 1
        our_matrix[col_check][row_check] = 2

    row_check = row
    col_check = column
    while row_check < size - 1 and col_check > 0:
        row_check += 1
        col_check -= 1
        our_matrix[col_check][row_check] = 2


def remove_in_current_row(row):
    global our_matrix
    prev_column = 0
    for i in range(size):
        if our_matrix[i][row - 1] == 1:
            prev_column = i
    our_matrix = stack.pop()
    return prev_column



"""Let's setup one iteration of the British Museum algorithm-- we'll put down 4 queens randomly."""

"""Now, we can print the result with a simple loop:"""


done = False

def solve():
    number_of_moves = 0  # where do I change this so it counts the number of Queen moves?
    number_of_iterations = 0
    global our_matrix
    our_matrix = [[0 for x in range(size)] for y in range(size)]
    global stack
    stack = []
    column = 0
    row = 0
    while(True):
        number_of_iterations += 1
        while column < size:
            print(number_of_iterations)
            if our_matrix[column][row] == 0:
                place_in_next_row(column, row)
                number_of_moves += 1
                row += 1
                column = 0
                break
            else:
                column += 1
        if column == size or row == size or check_beyond_row(row+1):
            if row == size:
                return number_of_iterations, number_of_moves
            prev_column = remove_in_current_row(row)
            if prev_column == -1:
                return number_of_iterations, number_of_moves
            row -= 1
            column = 1 + prev_column

def check_beyond_row(row):
    for j in range(row, size - 1):
        available = False
        for k in range(size - 1):
            if our_matrix[k][j] == 0:
                available = True
                break
        if not available:
            return True
    return False

def check_all_col():
    for j in range(size - 1):
        available = False
        for k in range(size - 1):
            if our_matrix[k][j] == 0 or our_matrix[k][j] == 1:
                available = True
                break
        if not available:
            return True
    return False


tot_num_iterations = 0
tot_num_moves = 0
min_iterations = 5000000000
max_iterations = 0
min_moves = 5000000000
max_moves = 0
for i in range(100):
    num_iterations = 0
    number_moves = 0
    columns = []
    num_iterations, number_moves = solve()
    if num_iterations > max_iterations:
        max_iterations = num_iterations
    if num_iterations < min_iterations:
        min_iterations = num_iterations
    if number_moves > max_moves:
        max_moves = number_moves
    if number_moves < min_moves:
        min_moves = number_moves
    tot_num_moves += number_moves
    tot_num_iterations += num_iterations

print("number of moves " + str(tot_num_moves/100))
print("number of iterations " + str(number_of_iterations/100))
print("min moves: " + str(min_moves))
print("max moves: " + str(max_moves))
print("min iterations: " + str(min_iterations))
print("max iterations: " + str(max_iterations))
