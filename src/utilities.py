"""Module providing useful functions to check validity of variables."""


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
    row_selection, column_selection, list_of_cells_revealed
) -> bool:
    """
    Check if the cell has already been revealed.

    Parameters
    ----------
    row_selection : int
        Row selected by the user.
    column_selection : int
        Column selected by the user.
    list_of_cells_revealed : list of tuple of int
        List of positions (row, col) of the cells revealed in the board.

    Returns
    -------
    bool
        True if the cell has already been revealed, False if it is not.
    """

    for cell_position in list_of_cells_revealed:
        if cell_position == (row_selection, column_selection):
            return True
    return False


def reveal_neighbor_0_cells(
    row_selection,
    column_selection,
    board,
    cells_revealed,
):
    """
    Reveal the group of neighboring cells with a value of 0.

    Parameters
    ----------
    row_selection : int
        Row selected by the user.
    column_selection : int
        Column selected by the user.
    board : list of list of int
        2D list containing integers with the number of mines around each cell.
    cells_revealed : list of tuple of int
        List of positions (row, col) of the cells revealed in the board.
    """
    number_of_rows = len(board)
    number_of_columns = len(board[0])

    # stop if the position select is outside the board
    if (
        row_selection < 0
        or row_selection >= number_of_rows
        or column_selection < 0
        or column_selection >= number_of_columns
        or (row_selection, column_selection) in cells_revealed
    ):
        return

    # stop if the value is not 0,  else, the position is added to the list of revealed cells
    if board[row_selection][column_selection] != 0:
        return

    cells_revealed.append((row_selection, column_selection))

    # List of the directions to check the neighbor cells (only top, right, bot, left; not diagonal)
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    # Recursive call of the fonctions in the directions specified in the list directions
    for direction_row, direction_col in directions:
        reveal_neighbor_0_cells(
            row_selection + direction_row,
            column_selection + direction_col,
            board,
            cells_revealed,
        )


def is_end_of_game(
    number_of_rows, number_of_columns, number_of_mines, number_of_revealed_cells
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
    number_of_revealed_cells : int
        Number of cells that the player has found during the game.

    Returns
    -------
    bool
        True if the player has found all the cells and finished the game, else False.
    """

    # the numeber of remaining cells to find is the total number of cells minus the number
    # of cells with a mine minus the number of cells we have already found
    number_of_remaining_cells_to_find = (
        number_of_columns * number_of_rows - number_of_revealed_cells - number_of_mines
    )
    if number_of_remaining_cells_to_find == 0:
        return 1

    return 0


def check_board_dimensions(board_rows, board_columns, max_size_board=100) -> bool:
    """
    Check the validity of board dimensions.

    Parameters
    ----------
    board_rows : int
        Number of rows of the board.
    board_columns : int
        Number of columns of the board.
    max_size_board : int, optional
        Maximum allowed size for the board (default is 100).

    Returns
    -------
    bool
        True if the dimensions are valid, False otherwise.
    """
    errors = []

    if board_columns < 1:
        errors.append("error: number of columns is not valid")
    if board_rows < 1:
        errors.append("error: number of rows is not valid")
    if not isinstance(board_columns, int):
        errors.append("error: number of columns is not an integer")
    if not isinstance(board_rows, int):
        errors.append("error: number of rows is not an integer")
    if board_columns > max_size_board:
        errors.append(f"error: number of columns is too large (over {max_size_board})")
    if board_rows > max_size_board:
        errors.append(f"error: number of rows is too large (over {max_size_board})")

    if errors:
        for error in errors:
            print(error)
        return False

    return True
