columns = []
size = 8
import random



def next_row_is_how_safe(col, row):
    num_of_conflicts = 0
    # check column
    for q_row, q_column in enumerate(columns):
        if col == q_column and q_row != row:
            # print("straight line conflict ", row, q_row)
            num_of_conflicts += 1

    # check diagonal
    for q_row, q_column in enumerate(columns):
        if q_column - q_row == col - row and q_row != row:
            # print("diag conflict1 ", row, q_row)
            num_of_conflicts += 1

    # check other diagonal
    for q_row, q_column in enumerate(columns):
        if ((size - q_column) - q_row
            == (size - col) - row) and q_row != row:
            # print("diag conflict2 ",  row, q_row)
            num_of_conflicts += 1
    return num_of_conflicts


def place_n_queens(size):
    columns.clear()
    row = 0
    while row < size:
        column = random.randrange(0, size)
        columns.append(column)
        row += 1


"""Now, we can print the result with a simple loop:"""


def display():
    for row in range(len(columns)):
        for column in range(size):
            if column == columns[row]:
                print('♛', end=' ')
            else:
                print(' .', end=' ')
        print()


number_of_moves = 0  # where do I change this so it counts the number of Queen moves?
number_of_iterations = 0
done = False


def solve():
    global done
    global number_of_iterations
    global number_of_moves
    number_of_moves = 0  # where do I change this so it counts the number of Queen moves?
    number_of_iterations = 0
    done = False
    same = 1
    prev_con = 1000
    num_tot_conflicts = 100
    while num_tot_conflicts > 0:
        curr_row = random.randint(0, size - 1)  # find a rand col to iterate through, find where's best to place queen in row
        # print("checking row: ", currRow)
        # print(curr_row)
        column = 0
        num_conflicts = size + 1
        end_column = 0
        number_of_iterations += 1
        number_of_moves += 1
        while column < size:

            curr_conflicts = next_row_is_how_safe(column, curr_row)
            if curr_conflicts < num_conflicts:
                end_column = column
                num_conflicts = curr_conflicts
            column += 1
        columns[curr_row] = end_column
        num_tot_conflicts = 0
        for queen_row, queen_column in enumerate(columns):
            num_tot_conflicts += next_row_is_how_safe(queen_column, queen_row)
        if num_tot_conflicts == prev_con:
            same += 1
            if same >= size*8:
                return
        elif num_tot_conflicts == 0:
            done = True
            return

        else:
            same = 0
            prev_con = num_tot_conflicts


# i = 0
# while i < 100:
#
#
#     col_copy = columns.copy()
#     while True:
#         solve()
#         if done:
#             i += 1
#             break
#
#         columns = col_copy.copy()


tot_num_iterations = 0
tot_num_moves = 0
min_iterations = 5000000000
max_iterations = 0
min_moves = 5000000000
max_moves = 0
for i in range(100):
    number_of_iterations = 0
    number_of_moves = 0
    while True:

        place_n_queens(size)
        solve()
        if done:
            display()
            print()
            break
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

print("number of moves " + str(tot_num_moves/100))
print("number of iterations " + str(tot_num_iterations/100))
print("min moves: " + str(min_moves))
print("max moves: " + str(max_moves))
print("min iterations: " + str(min_iterations))
print("max iterations: " + str(max_iterations))

