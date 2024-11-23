"""Module providing functions to create and print the game board."""

import random
from utilities import check_board_dimensions


def create_board(board_rows: int, board_columns: int) -> tuple:
    """
    Create a game board with the specified number of rows and columns.

    Parameters
    ----------
    board_rows : int
        Number of rows in the board. Must be between 1 and 100.
    board_columns : int
        Number of columns in the board. Must be between 1 and 100.

    Returns
    -------
    tuple
        A tuple containing:

        - **board** (*list of list of int*):
          A 2D list where each cell contains the number of mines around it.
        - **list_of_mines** (*list of tuple of int*):
          A list of positions (row, col) of all mines on the board.
    """

    max_size_board = 100

    # check validity of board dimensions
    if not check_board_dimensions(board_rows, board_columns, max_size_board):
        # Handle invalid dimensions (e.g., raise an exception or exit)
        raise ValueError("Invalid board dimensions")

    # initialize the board with 0
    # board[row_number][column_number]
    board = [[0 for i in range(board_columns)] for j in range(board_rows)]

    # place the mine randomly with a probability of 0.1
    probability_of_mine = 0.1
    list_of_mines = []

    for i in range(board_columns):
        for j in range(board_rows):
            if random.random() < probability_of_mine:
                list_of_mines.append((j, i))
            else:
                pass

    # add the count of the number of mine around each case by adding 1 around each mine
    # when we are not at the edge of the board
    for mine_position in list_of_mines:
        row, col = mine_position
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < board_rows and 0 <= new_col < board_columns:
                    board[new_row][new_col] += 1
    return board, list_of_mines


def print_board(board, list_of_mines):
    """
    Print the board with values and mines for debugging purposes.

    Parameters
    ----------
    board : list of list of int
        2D array of the board with integers that represent the number of mines around each case.
    list_of_mines : list of tuple of int
        List of positions (row, col) of the mines.
    """

    board_to_print = board
    for mine_position in list_of_mines:
        board_to_print[mine_position[0]][mine_position[1]] = "X"

    for row in board_to_print:
        for col in row:
            print(str(col) + " ", end="")
        print()

    print()
    print(list_of_mines)


def print_board_in_game(
    board, list_of_mines, list_of_revealed_cases, list_annotated_cases
):
    """
    Print the game board in the terminal.

    Parameters
    ----------
    board : list of list of int
        2D array of the board with integers that represent the number of mines around each case.
    list_of_mines : list of tuple of int
        List of positions (row, col) of the mines.
    list_of_revealed_cases : list of tuple of int
        List of the positions (row, col) of revealed cases.
    list_annotated_cases : list of tuple of int
        List of the positions (row, col) of the annotated cases.
    """

    # create board_to_print that contains X for the location of the mine and an integer that
    # represent the number of mine around the case
    board_to_print = board
    for mine_position in list_of_mines:
        board_to_print[mine_position[0]][mine_position[1]] = "X"

    temp_board = []

    # Fill temp_board with "°" if cell is annotated, "*" if cell is not revealed.
    # Else, the value of board_to_print
    for row_index, row in enumerate(board_to_print):
        new_row = []
        for col_index, cell in enumerate(row):
            # If the cell is revealed
            if (row_index, col_index) in list_of_revealed_cases:
                new_row.append(cell)
            else:
                # If the cell is annotated
                if (row_index, col_index) in list_annotated_cases:
                    new_row.append("°")
                # If the cell is not revealed
                else:
                    new_row.append("*")
        temp_board.append(new_row)

    board_to_print = temp_board

    # Add a space at the end of each caracter for readability
    for row in board_to_print:
        for col in row:
            print(str(col) + " ", end="")
        print()

    print()
