def is_there_a_mine(row_selection, column_selection, list_of_mines) -> bool:
    """
    Check if there is a mine in the selected position.

    Parameters
    ----------
    row_selection : int
        Row selected by the user.
    column_selection : int
        Column selected by the user.
    list_of_mines : list of tuple of int
        List of positions (row, col) of the mines in the board.

    Returns
    -------
    bool
        True if there is a mine, False if there is not.
    """

    for mine_position in list_of_mines:
        if (row_selection, column_selection) == mine_position:
            return True
    return False


def is_already_revealed(
    row_selection, column_selection, list_of_cases_revealed
) -> bool:
    """
    Check if the case has already been revealed.

    Parameters
    ----------
    row_selection : int
        Row selected by the user.
    column_selection : int
        Column selected by the user.
    list_of_cases_revealed : list of tuple of int
        List of positions (row, col) of the cases revealed in the board.

    Returns
    -------
    bool
        True if the case has already been revealed, False if it is not.
    """

    for case_position in list_of_cases_revealed:
        if case_position == (row_selection, column_selection):
            return True
    return False


def reveal_neighbor_0_cases(
    row_selection,
    column_selection,
    number_of_rows,
    number_of_columns,
    board,
    cases_revealed,
):
    """
    Reveal the group of neighboring cases with a value of 0.

    Parameters
    ----------
    row_selection : int
        Row selected by the user.
    column_selection : int
        Column selected by the user.
    number_of_rows : int
        Number of rows of the board.
    number_of_columns : int
        Number of columns of the board.
    board : list of list of int
        2D list containing integers with the number of mines around each case.
    cases_revealed : list of tuple of int
        List of positions (row, col) of the cases revealed in the board.
    """

    # stop if the position select is outside the board
    if (
        row_selection < 0
        or row_selection >= number_of_rows
        or column_selection < 0
        or column_selection >= number_of_columns
        or (row_selection, column_selection) in cases_revealed
    ):
        return

    # stop if the value is not 0,  else, the position is added to the list of revealed cases
    if board[row_selection][column_selection] != 0:
        return
    else:
        cases_revealed.append((row_selection, column_selection))

    # List of the directions to check the neighbor cases (only top, right, bot, left; not diagonal)
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    # Recursive call of the fonctions in the directions specified in the list directions
    for direction_row, direction_col in directions:
        reveal_neighbor_0_cases(
            row_selection + direction_row,
            column_selection + direction_col,
            number_of_rows,
            number_of_columns,
            board,
            cases_revealed,
        )


def is_end_of_game(
    number_of_rows, number_of_columns, number_of_mines, number_of_revealed_cases
) -> bool:
    """
    Check if the player has completed the game.

    Parameters
    ----------
    number_of_rows : int
        Number of rows of the game board.
    number_of_columns : int
        Number of columns of the game board.
    number_of_mines : int
        Number of mines in the game.
    number_of_revealed_cases : int
        Number of cases that the player has found during the game.

    Returns
    -------
    bool
        True if the player has found all the cases and finished the game, else False.
    """

    # the numeber of remaining cases to find is the total number of cases minus the number of cases with a mine minus the number of cases we have already found
    number_of_remaining_cases_to_find = (
        number_of_columns * number_of_rows - number_of_revealed_cases - number_of_mines
    )
    if number_of_remaining_cases_to_find == 0:
        return 1
    else:
        return 0
