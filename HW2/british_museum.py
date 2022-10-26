import random

columns = [0, 0, 0, 0, 0, 0, 0, 0]  # columns is the locations for each of the queens
# columns[r] is a number c if a queen is placed at row r and column c.
size = 8


def next_row_is_safe(col, row):
    num_of_conflicts = 0
    # check column
    for q_row, q_column in enumerate(columns):
        if col == q_column and q_row != row:
            # print("straight line conflict ", row, q_row)
            return False

    # check diagonal
    for q_row, q_column in enumerate(columns):
        if q_column - q_row == col - row and q_row != row:
            # print("diag conflict1 ", row, q_row)
            return False

    # check other diagonal
    for q_row, q_column in enumerate(columns):
        if ((size - q_column) - q_row
            == (size - col) - row) and q_row != row:
            # print("diag conflict2 ",  row, q_row)
            return False
    return True


def display():
    for row in range(len(columns)):
        for column in range(size):
            if column == columns[row]:
                print('♛', end=' ')
            else:
                print(' .', end=' ')
        print()


def every_option():
    for i in range(8):
        columns[0] = i
        for j in range(8):
            columns[1] = j
            for k in range(8):
                columns[2] = k
                for l in range(8):
                    columns[3] = l
                    for m in range(8):
                        columns[4] = m
                        for n in range(8):
                            columns[5] = n
                            for o in range(8):
                                columns[6] = o
                                for p in range(8):
                                    columns[7] = p
                                    is_solution = True
                                    for queen_row, queen_column in enumerate(columns):
                                        t = next_row_is_safe(queen_column, queen_row)
                                        if not t:
                                            is_solution = False
                                    if is_solution:
                                        display()
                                        print(columns)
                                        return


number_of_moves = 0
number_of_iterations = 0
def british_museum():
    global number_of_moves
    global number_of_iterations
    while (True):
        for i in range(size):
            number_of_moves += 1
            columns[i] = random.randint(0, size - 1)
        is_solution = True
        for queen_row, queen_column in enumerate(columns):
            t = next_row_is_safe(queen_column, queen_row)
            if not t:

                is_solution = False
        number_of_iterations += 1
        if is_solution:
            # display()
            # print(columns)
            return



tot_num_iterations = 0
tot_num_moves = 0
min_iterations = 5000000000
max_iterations = 0
min_moves = 5000000000
max_moves = 0
for i in range(100):
    print(i)
    number_of_iterations = 0
    number_of_moves = 0
    british_museum()
    if number_of_iterations > max_iterations:
        max_iterations = number_of_iterations
    if number_of_iterations < min_iterations:
        min_iterations = number_of_iterations
    if number_of_moves > max_moves:
        max_moves = number_of_moves
    if number_of_moves < min_moves:
        min_moves = number_of_moves
    tot_num_moves += number_of_moves
    tot_num_iterations += number_of_iterations

print("number of moves " + str(tot_num_iterations/100))
print("number of iterations " + str(tot_num_moves/100))
print("min moves: " + str(min_moves))
print("max moves: " + str(max_moves))
print("min iterations: " + str(min_iterations))
print("max iterations: " + str(max_iterations))
