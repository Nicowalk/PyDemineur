"""Main file that contain the game loop"""
from board import create_board, print_board, print_board_in_game
from actions import action_selection, case_selection, reveal_case
from utilities import is_already_revealed, is_end_of_game

# Size of the board
NUMBER_OF_ROWS = 4
NUMBER_OF_COLUMNS = 4

# Create the game board
board, list_of_mines = create_board(NUMBER_OF_ROWS, NUMBER_OF_COLUMNS)

print_board(board, list_of_mines)
# Game data : revealed cases and annotated cases (each case is either : not revealed or revealed;
# An annotated case is always a not revealed case)
revealed_cases = []
annotated_cases = []

# Condition of the end of game. True when a mine is clicked OR all the mines are
GAME_FINISHED = False

# GAME LOOP
while not GAME_FINISHED:

    # Choose between select a case or annotate a case
    ACTION_CHOICE = action_selection()

    # Select the row and column of the board
    row_selection, col_selection = case_selection(NUMBER_OF_ROWS, NUMBER_OF_COLUMNS)

    CASE_TYPE = 0

    # Reveal a case
    if ACTION_CHOICE == 0:
        # check if the case was already revealed
        if is_already_revealed(row_selection, col_selection, revealed_cases):
            print("You already clicked this case")
        else:
            # return either 1 if the case was a mine or 0 if not
            CASE_TYPE = reveal_case(
                row_selection,
                col_selection,
                board,
                list_of_mines,
                revealed_cases,
            )

    # Annotate a case
    if ACTION_CHOICE == 1:
        # Check if the case was not already revealed
        if (row_selection, col_selection) in revealed_cases:
            print("Case already revealed")
        else:
            # Check if the case was not already annotated
            if (row_selection, col_selection) in annotated_cases:
                print("Case already annotated")
            else:
                # Add the case position to the list of annotated cases
                annotated_cases.append((row_selection, col_selection))

    # Show the game board updated
    print_board_in_game(board, list_of_mines, revealed_cases, annotated_cases)

    # Check if the game is win or lose
    if is_end_of_game(
        NUMBER_OF_ROWS, NUMBER_OF_COLUMNS, len(list_of_mines), len(revealed_cases)
    ):
        print("WINNER")
        GAME_FINISHED = True

    if CASE_TYPE == 1:
        print("LOSER")
        GAME_FINISHED = True

print("GAME OVER")
