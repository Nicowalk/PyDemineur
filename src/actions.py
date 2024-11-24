"""Module providing functions related to user inputs and actions."""

from utilities import is_there_a_mine, reveal_neighbor_0_cells


def reveal_cell(
    row_selection,
    column_selection,
    board,
    list_of_mines,
    cells_revealed,
) -> bool:
    """
    Reveal the cell that is selected.

    Parameters
    ----------
    row_selection : int
        Selected row by the user.
    column_selection : int
        Selected column by the user.
    board : list of list of int
        2D list containing integers with the number of mines around each cell.
    list_of_mines : list of tuple of int
        List of positions (row, col) of the mines.
    cells_revealed : list of tuple of int
        List of the positions (row, col) of revealed cells.

    Returns
    -------
    bool
        True if the cell contains a mine, False if it doesn't.
    """

    # check if the revealed cell contain a mine
    if is_there_a_mine(row_selection, column_selection, list_of_mines):
        # If the revealed cell is a mine return 1
        return 1

    # If the cell is not a mine and the integer value stored in the board at this position
    # is 0, reveals all the group of cell that also contain a 0, else, just add the cell
    # to the list of revealed cells
    if board[row_selection][column_selection] == 0:
        reveal_neighbor_0_cells(
            row_selection,
            column_selection,
            board,
            cells_revealed,
        )
    else:
        cells_revealed.append((row_selection, column_selection))
    # If the revealed cell is not a mine return 0
    return 0


def action_selection():
    """
    The user selects to annotate or select a cell to reveal.

    Returns
    -------
    int
        User selection, 0 to reveal a cell, 1 to annotate a cell.
    """

    select_or_annotate = -1
    # while the input is not 0 or 1
    while select_or_annotate not in (0, 1):
        print("0 to reveal a cell, 1 to annotate")
        select_or_annotate = int(input())

    return select_or_annotate


def cell_selection(number_of_rows, number_of_columns):
    """
    The user selects a cell.

    Parameters
    ----------
    number_of_rows : int
        Number of rows of the board.
    number_of_columns : int
        Number of columns of the board.

    Returns
    -------
    tuple
        The row number and column number selected by the user.
    """

    row_selection = -1
    while not 0 <= row_selection < number_of_rows:
        print("Select the row between 0 and " + str(number_of_rows - 1))
        row_selection = int(input())

    # The user select a column number while it is valid
    col_selection = -1
    while not 0 <= col_selection < number_of_columns:
        print("Select the column between 0 and " + str(number_of_columns - 1))
        col_selection = int(input())

    return row_selection, col_selection
