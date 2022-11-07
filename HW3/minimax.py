import copy
import numpy as np
import random
from termcolor import colored  # can be taken out if you don't like it...

# # # # # # # # # # # # # # global values  # # # # # # # # # # # # # #
ROW_COUNT = 6
COLUMN_COUNT = 7

RED_CHAR = colored('X', 'red')  # RED_CHAR = 'X'
BLUE_CHAR = colored('O', 'blue')  # BLUE_CHAR = 'O'

EMPTY = 0
RED_INT = 1
BLUE_INT = 2


# # # # # # # # # # # # # # functions definitions # # # # # # # # # # # # # #

def create_board():
    """creat empty board for new game"""
    board = np.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)
    return board


def drop_chip(board, row, col, chip):
    """place a chip (red or BLUE) in a certain position in board"""
    board[row][col] = chip


def is_valid_location(board, col):
    """check if a given column in the board has a room for extra dropped chip"""
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):
    """assuming column is available to drop the chip,
    the function returns the lowest empty row  """
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    """print current board with all chips put in so far"""
    # print(np.flip(board, 0))
    print(" 1 2 3 4 5 6 7 \n" "|" + np.array2string(np.flip(np.flip(board, 1)))
          .replace("[", "").replace("]", "").replace(" ", "|").replace("0", "_")
          .replace("1", RED_CHAR).replace("2", BLUE_CHAR).replace("\n", "|\n") + "|")

amount_of_wins = 0
def game_is_won(board, chip):
    """check if current board contain a sequence of 4-in-a-row of in the board
     for the player that play with "chip"  """
    global amount_of_wins
    amount_of_wins = 0
    winner = False
    winning_Sequence = np.array([chip, chip, chip, chip])
    # Check horizontal sequences
    for r in range(ROW_COUNT):
        if "".join(list(map(str, winning_Sequence))) in "".join(list(map(str, board[r, :]))):
            amount_of_wins += 1
            winner = True
    # Check vertical sequences
    for c in range(COLUMN_COUNT):
        if "".join(list(map(str, winning_Sequence))) in "".join(list(map(str, board[:, c]))):
            amount_of_wins += 1
            winner = True
    # Check positively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, winning_Sequence))) in "".join(list(map(str, board.diagonal(offset)))):
            amount_of_wins += 1
            winner = True
    # Check negatively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, winning_Sequence))) in "".join(list(map(str, np.flip(board, 1).diagonal(offset)))):
            amount_of_wins += 1
            winner = True
    return winner


def board_tot(curr_board, chip):
    total = 0
    """check if current board contain a sequence of 4-in-a-row of in the board
     for the player that play with "chip"  """
    if game_is_won(curr_board, chip):
        total += 500
    if amount_of_wins > 1:
        total += 500

    for t in range(4):
        sequence = np.array([chip, chip, chip, chip])
        sequence[t] = 0
        is_double_trap = 200
        three = goodies(curr_board, sequence, is_double_trap)
        if abs(three / is_double_trap) > 1:
            total += 600
        total += three

    sequence = np.array([0, chip, chip, chip, 0])
    total += goodies(curr_board, sequence, 500)

    for t in range(4):
        for j in range(4):
            sequence = np.array([chip, chip, chip, chip])
            if t != j:
                sequence[t] = 0
                sequence[j] = 0
            else:
                continue
            # print("sequence is " + str(sequence[0]) + str(sequence[1]) + str(sequence[2]) + str(sequence[3]))
            total += goodies(curr_board, sequence, 30)

    other_chip = other_color(chip)
    sequence = np.array([0, other_chip, other_chip, other_chip, 0])
    both_side_trap = goodies(curr_board, sequence, -400) # 01110
    total += both_side_trap
    sequence = np.array([0, 0, other_chip, other_chip, 0])
    both_side_trap = goodies(curr_board, sequence, -400)  # 01110
    sequence = np.array([0, other_chip, other_chip, 0, 0])
    both_side_trap = goodies(curr_board, sequence, -400)


    for t in range(4):
        sequence1 = np.array([other_chip, other_chip, other_chip, other_chip])
        sequence1[t] = 0
        is_double_trap = -150
        op_three = goodies(curr_board, sequence, is_double_trap)
        if abs(op_three/is_double_trap) > 1:
            total -= 10000
        total += op_three
        for j in range(4):
            sequence2 = np.array([other_chip, other_chip, other_chip, other_chip])
            if t != j:
                sequence2[t] = 0
                sequence2[j] = 0
            else:
                continue
            op_two = goodies(curr_board, sequence, -20)
            total += op_two

    if game_is_won(curr_board, other_chip):#check if oppenent will win in these situations
        total -= 300
    if amount_of_wins > 1:
        total -= 300
    return total


goodie_calls = 0


def goodies(curr_board, sequence, reward):
    total = 0
    global goodie_calls
    goodie_calls += 1
    for r in range(ROW_COUNT):
        if "".join(list(map(str, sequence))) in "".join(list(map(str, curr_board[r, :]))):
            total += reward
    # Check vertical sequences
    for c in range(COLUMN_COUNT):
        if "".join(list(map(str, sequence))) in "".join(list(map(str, curr_board[:, c]))):
            total += reward
    # Check positively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, sequence))) in "".join(list(map(str, curr_board.diagonal(offset)))):
            total += reward
    # Check negatively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, sequence))) in "".join(list(map(str, np.flip(curr_board, 1).diagonal(offset)))):
            total += reward
    return total


def other_color(color):
    if color == RED_INT:
        return BLUE_INT
    return RED_INT


def get_valid_locations(board):
    valid_locations = []
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations


def MoveRandom(board, color):
    valid_locations = get_valid_locations(board)
    column = random.choice(
        valid_locations)  # you can replace with input if you like... -- line updated with Gilad's code-- thanks!
    row = get_next_open_row(board, column)
    drop_chip(board, row, column, color)


minimaxCalls = 0


def minimax(cboard, d, a, b, player, chip):
    global minimaxCalls
    minimaxCalls += 1
    if d == 0:  # or done?
        col_at_maxi = get_valid_locations(cboard)[0]
        maxi = -1000
        for loc in get_valid_locations(cboard):
            tmp = copy.deepcopy(cboard)
            drop_chip(tmp, get_next_open_row(tmp, loc), loc, chip)
            curr = board_tot(tmp, chip)
            if curr > maxi:
                maxi = curr
                col_at_maxi = loc

        # print("max here is " + str(maxi) + " at loc " + str(col_at_maxi))
        ans = [int(maxi), int(col_at_maxi)]
        return ans

    if player:
        maxi = -1000
        col_at_maxi = 0
        for loc in get_valid_locations(cboard):
            tmp = copy.deepcopy(cboard)
            drop_chip(tmp, get_next_open_row(tmp, loc), loc, chip)
            check = minimax(tmp, d - 1, a, b, False, chip)
            if check[0] >= maxi:
                maxi = check[0]
                col_at_maxi = check[1]
            # print("min is " + str(maxi) + " and b is " + str(b))
            a = max(a, check[0])
            if b <= a:
                # print("pruned!")
                ans = [int(maxi), int(col_at_maxi)]
                return ans
        ans = [int(maxi), int(col_at_maxi)]
        return ans
    else:
        mini = 1000
        col_at_mini = 0
        for loc in get_valid_locations(cboard):
            # check if you or opponent would win w a particular move
            tmp = copy.deepcopy(cboard)
            drop_chip(tmp, get_next_open_row(tmp, loc), loc, other_color(chip))
            check = minimax(tmp, d - 1, a, b, True, chip)
            if check[0] <= mini:
                mini = check[0]
                col_at_mini = check[1]
            # print("min is " + str(mini) + " and a is " + str(a))
            b = min(b, check[0])
            if b <= a:
                # print("pruned!")
                ans = [int(mini), int(col_at_mini)]
                return ans
                # break
        ans = [int(mini), int(col_at_mini)]
        return ans


def MoveWLogic(cboard, color, turn):
    if turn == 0:
        rand = random.randint(3, 5)
        drop_chip(cboard, get_next_open_row(cboard, rand), rand, color)
        return
    valid_locations = get_valid_locations(cboard)
    for loc in valid_locations:
        tmp = copy.deepcopy(cboard)
        drop_chip(tmp, get_next_open_row(tmp, loc), loc, color)
        if game_is_won(tmp, color):
            drop_chip(cboard, get_next_open_row(cboard, loc), loc, color)
            return True

    for loc in valid_locations:
        tmp = copy.deepcopy(cboard)
        drop_chip(tmp, get_next_open_row(tmp, loc), loc, other_color(color))
        if game_is_won(tmp, other_color(color)):
            drop_chip(cboard, get_next_open_row(cboard, loc), loc, color)
            return False

    ans = minimax(cboard, 0, -10000, 10000, True, color)
    drop_chip(cboard, get_next_open_row(cboard, ans[1]), ans[1], color)
    return True



# # # # # # # # # # # # # # main execution of the game # # # # # # # # # # # # # #
def play():
    turn = 0

    game_over = False

    while not game_over:
        if turn % 2 == 1:
            # MoveRandom(board, RED_INT)
            col = int(input("RED please choose a column(1-7): "))
            while col > 7 or col < 1:
                col = int(input("Invalid column, pick a valid one: "))
            while not is_valid_location(board, col - 1):
                col = int(input("Column is full. pick another one..."))
            col -= 1

            row = get_next_open_row(board, col)
            drop_chip(board, row, col, RED_INT)

        if turn % 2 == 0 and not game_over:
            MoveWLogic(board, BLUE_INT, turn)
            print_board(board)

        if game_is_won(board, RED_INT):
            game_over = True
            print_board(board)
            print(colored("Red wins!", 'red'))
            return 2
        if game_is_won(board, BLUE_INT):
            game_over = True
            print_board(board)
            print(colored("Blue wins!", 'blue'))
            return 1
        if len(get_valid_locations(board)) == 0:
            game_over = True
            print(colored("Draw!", 'blue'))
            return 0
        turn += 1


blue = 0
red = 0
tie = 0
board = create_board()
print_board(board)
for i in range(10):
    board = create_board()
    j = play()
    if j == 1:
        blue += 1
    elif j == 2:
        red += 1
    else:
        tie += 1
print("red: " + str(red))
print("blue: " + str(blue))
print("tie: " + str(tie))
