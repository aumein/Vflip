import pandas as pd
import random
# -------------------------------------------------------------------------------------------------------------------
# IMPORTANT NOTE
# This is based off of the game "Voltorb Flip", a mini-game that is found in Pokemon HeartGold and SoulSilver, which
# was originally programmed in JavaScript. This was created for the express purpose of learning Python, and is NOT
# an original concept. As I am submitting this for the AP Computer Science Principals exam, I feel it is necessary to
# give credit to Nintendo and the developers of Pokemon HG/SS as the original creators of this game, and encourage you
# to support the original games.
#
# RULES
# The 5x5 grid has various values ranging from 0 - 3. Each column and row is labeled with the amount of 'bomb' (0
# tiles) and the amount of points (sum of all numbered values). Through coordinate guesses, the player must find all of
# the numbered tiles without hitting any of the 'bomb' tiles. The score is the product of all numbered tiles, so the
# game is concluded once the player has either hit a 0 tile, or has successfully hit all 2 and 3 numbered tiles.
# -------------------------------------------------------------------------------------------------------------------
# Just a few definitions to make
# SCORE CHECK - Game will continue until score is met


def check(x):
    rows_by_lists = game_grid.to_numpy().tolist()
    product = 1
    for n in range(0, 4):
        for ele in rows_by_lists[n]:
            if ele == 0:
                product = product
            else:
                product = product * ele
    if product == x:
        return False
    else:
        return True


def set_up():
    for index in range(0, 4):
        for col_num in range(1, 5):
            game_grid.loc[index, "col "+str(col_num)] = random.randint(0, 3)


#  OF BOMBS IN ROW
def b_sum_col(x):
    my_list = grid3[x]
    count = 0
    for element in my_list:
        if element == 0:
            count = count + 1
    return count


# OF BOMBS IN COL
def b_sum_row(x):
    my_list = grid4[x]
    count = 0
    for element in my_list:
        if element == 0:
            count = count + 1
    return count


# EMPTY GRID - EDIT TO SHOW GAME BOARD VALUES
empty = pd.DataFrame({'1': ['?', '?', '?', '?', '?'],
                      '2': ['?', '?', '?', '?', '?'],
                      '3': ['?', '?', '?', '?', '?'],
                      '4': ['?', '?', '?', '?', '?'],
                      '5': ['?', '?', '?', '?', '?']})


# GAME GRID - TAKE VALUES FROM THIS DF  ------------------------------------------------------------------------------
game_grid = pd.DataFrame({'col 1': [0, 0, 0, 0, 0],
                          'col 2': [0, 0, 0, 0, 0],
                          'col 3': [0, 0, 0, 0, 0],
                          'col 4': [0, 0, 0, 0, 0],
                          'col 5': [0, 0, 0, 0, 0]})


# RANDOMIZE GAME_GRID
set_up()

# --------------------------------------------------------------------------------------------------------------------
# CREATING THE "UI" AND BOARD FOR PLAYER
# rename columns and indexes to placeholders // HONESTLY NOT NEEDED LOL
grid2 = game_grid.rename(index={0: "c1", 1: 'c2', 2: 'c3', 3: 'c4', 4: 'c5'},
                         columns={'col 1': '1', 'col 2': '2', 'col 3': '3', 'col 4': '4', 'col 5': '5'})

# SUM OF POINTS
sum_row = grid2.sum(axis=1).to_numpy()
sum_column = grid2.sum(axis=0).to_numpy()

# TRANSPOSE FOR GRID 3
grid3 = grid2.transpose().to_numpy()
grid4 = grid2.to_numpy()


# GAME BOARD FOR THE PLAYER!!!!!
board = []


# UPDATE BOARD ARRANGEMENT
def update(arr):
    arr = empty.rename(index={0: str(sum_row.item(0)) + "P " + str(b_sum_row(0)) + "B",
                                1: str(sum_row.item(1)) + "P " + str(b_sum_row(1)) + "B",
                                2: str(sum_row.item(2)) + "P " + str(b_sum_row(2)) + "B",
                                3: str(sum_row.item(3)) + "P " + str(b_sum_row(3)) + "B",
                                4: str(sum_row.item(4)) + "P " + str(b_sum_row(4)) + "B"},
                       columns={'1': str(sum_column.item(0)) + "P " + str(b_sum_col(0)) + "B",
                                '2': str(sum_column.item(1)) + "P " + str(b_sum_col(1)) + "B",
                                '3': str(sum_column.item(2)) + "P " + str(b_sum_col(2)) + "B",
                                '4': str(sum_column.item(3)) + "P " + str(b_sum_col(3)) + "B",
                                '5': str(sum_column.item(4)) + "P " + str(b_sum_col(4)) + "B"})
    return arr


# -------------------------------------------------------------------------------------------------------------------
# GAME PLAY
total = 1
while check(total):
    board = update(board)
    print(board)
    # Making a guess
    row = int(input("Which row do you want to check? (1 - 5)")) - 1
    column = input("which column do you want to check? (1 - 5)")
    guess = int(game_grid.loc[row, "col "+column])

    # Using the guess / updating the game board
    total = total * guess
    empty.iloc[row, empty.columns.get_loc(column)] = guess

    if guess == 0:
        print("You hit a bomb! Game over!")
        ans = input("Play again? (Y/N)")
        if ans.capitalize() == "Y":
            continue
        else:
            break
    else:
        print("You got a "+str(guess)+"!")
        print("Your score is now "+str(total))

print("Thanks for playing!")
