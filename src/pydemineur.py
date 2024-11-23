"""Main file that contains the game loop for Minesweeper."""

from board import create_board, print_board_in_game
from actions import action_selection, case_selection, reveal_case
from utilities import is_already_revealed, is_end_of_game


def game_run(number_of_rows=4, number_of_columns=4):
    """
    Main function to run the Minesweeper game loop.
    """

    print("GAME START")
    # Create the game board
    board, list_of_mines = create_board(number_of_rows, number_of_columns)

    # Game data: revealed cases and annotated cases
    revealed_cases = []
    annotated_cases = []
    print_board_in_game(board, list_of_mines, revealed_cases, annotated_cases)

    # Condition of the end of the game
    game_finished = False
    result = False  # True if win, False if lose

    # GAME LOOP
    while not game_finished:

        # Choose between selecting a case or annotating a case
        action_choice = action_selection()

        # Select the row and column of the board
        row_selection, col_selection = case_selection(number_of_rows, number_of_columns)

        case_type = 0

        # Reveal a case
        if action_choice == 0:
            # Check if the case was already revealed
            if is_already_revealed(row_selection, col_selection, revealed_cases):
                print("You already clicked this case.")
            else:
                # Return 1 if the case was a mine, or 0 otherwise
                case_type = reveal_case(
                    row_selection,
                    col_selection,
                    board,
                    list_of_mines,
                    revealed_cases,
                )

        # Annotate a case
        elif action_choice == 1:
            # Check if the case is already revealed or annotated
            if (row_selection, col_selection) in revealed_cases:
                print("Case already revealed.")
            elif (row_selection, col_selection) in annotated_cases:
                print("Case already annotated.")
            else:
                # Add the case to the annotated cases list
                annotated_cases.append((row_selection, col_selection))

        # Update and display the game board
        print_board_in_game(board, list_of_mines, revealed_cases, annotated_cases)

        # Check if the game is won or lost
        if is_end_of_game(
            number_of_rows, number_of_columns, len(list_of_mines), len(revealed_cases)
        ):
            print("WINNER")
            game_finished = True
            result = 1

        if case_type == 1:
            print("LOSER")
            game_finished = True
            result = 0

    print("GAME OVER")
    return result


if __name__ == "__main__":
    game_run(10, 10)
