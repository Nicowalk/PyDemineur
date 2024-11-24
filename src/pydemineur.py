"""Main file that contains the game loop for Minesweeper."""

from board import create_board, print_board_in_game, print_board
from actions import action_selection, cell_selection, reveal_cell
from utilities import is_already_revealed, is_end_of_game


def game_run(number_of_rows=4, number_of_columns=4):
    """
    Main function to run the Minesweeper game loop.
    """

    print("GAME START")
    # Create the game board
    board, list_of_mines = create_board(number_of_rows, number_of_columns)

    # Game data: revealed cells and annotated cells
    revealed_cells = []
    annotated_cells = []
    print_board_in_game(board, revealed_cells, annotated_cells)

    # Condition of the end of the game
    game_finished = False
    result = False  # True if win, False if lose

    # GAME LOOP
    while not game_finished:

        # Choose between selecting a cell or annotating a cell
        action_choice = action_selection()

        # Select the row and column of the board
        row_selection, col_selection = cell_selection(number_of_rows, number_of_columns)

        cell_type = 0

        # Reveal a cell
        if action_choice == 0:
            # Check if the cell was already revealed
            if is_already_revealed(row_selection, col_selection, revealed_cells):
                print("You already clicked this cell.")
            else:
                # Return 1 if the cell was a mine, or 0 otherwise
                cell_type = reveal_cell(
                    row_selection,
                    col_selection,
                    board,
                    list_of_mines,
                    revealed_cells,
                )

        # Annotate a cell
        elif action_choice == 1:
            # Check if the cell is already revealed or annotated
            if (row_selection, col_selection) in revealed_cells:
                print("cell already revealed.")
            elif (row_selection, col_selection) in annotated_cells:
                print("cell already annotated.")
            else:
                # Add the cell to the annotated cells list
                annotated_cells.append((row_selection, col_selection))

        # Update and display the game board
        print_board_in_game(board, revealed_cells, annotated_cells)

        # Check if the game is won or lost
        if is_end_of_game(
            number_of_rows, number_of_columns, len(list_of_mines), len(revealed_cells)
        ):
            print_board(board, list_of_mines)
            print("WINNER")
            game_finished = True
            result = 1

        if cell_type == 1:
            print("YOU HIT A MINE !")
            print_board(board, list_of_mines)
            print("LOSER")
            game_finished = True
            result = 0

    print("GAME OVER")
    return result


if __name__ == "__main__":
    game_run(10, 10)
