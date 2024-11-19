#Check if there is a mine in the selected position
def is_there_a_mine(row_selection, column_selection, list_of_mines):
    #INPUTS
        # row_selection : integer, row selected by the user
        # column_selection : integer, column selected by the user
        # list_of_mines : list of positions (row,col) of the mines in the board
    #OUTPUTS
        #boolean : 1 if there is a mine, 0 if there is not
    
    for mine_position in list_of_mines:
        if (row_selection,column_selection) == mine_position:
            return True
    return False

#Check if the case has already been revealed
def is_already_revealed(row_selection, column_selection, list_of_cases_revealed):
    #INPUTS
        # row_selection : integer, row selected by the user
        # column_selection : integer, column selected by the user
        # list_of_cases_revealed : list of positions (row,col) of the cases revealed in the board
    #OUTPUTS
        #boolean : 1 if there is the case has already been revealed, 0 if there it is not

    for case_position in list_of_cases_revealed:
        if case_position == (row_selection,column_selection):
            return True
    return False

#Reveal the group of neighboring case with a value of 0
def reveal_neighbor_0_cases(row_selection, column_selection, number_of_rows, number_of_columns, board, cases_revealed):
    #INPUT
        # row_selection : integer, row selected by the user
        # column_selection : integer, column selected by the user
        # number_of_rows : integer, number of rows of the board
        # number_of_columns : integer, number of columns of the board
        # board : list of list (2D) containing integers with the number of mine around each case
        # cases_revealed : list of positions (row,col) of the cases revealed in the board

    #stop if the position select is outside the board
    if (row_selection < 0 or row_selection >= number_of_rows or 
        column_selection < 0 or column_selection >= number_of_columns or
        (row_selection, column_selection) in cases_revealed):
        return

    #stop if the value is not 0,  else, the position is added to the list of revealed cases
    if board[row_selection][column_selection] != 0:
        return
    else:
        cases_revealed.append((row_selection, column_selection))

    #List of the directions to check the neighbor cases (only top, right, bot, left; not diagonal)
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    
    # Recursive call of the fonctions in the directions specified in the list directions
    for direction_row, direction_col in directions:
        reveal_neighbor_0_cases(row_selection + direction_row, column_selection + direction_col, board, cases_revealed)

#Check if the player has completed the game
def is_end_of_game(number_of_rows, number_of_columns, number_of_mines, number_of_revealed_cases):
    #INPUTS
        #number_of_rows: integer, number of rows of the game board
        #number_of_columns: integer, number of columns of the game board
        #number_of_mines: integer, number of mines in the game
        #number_of_revealed_cases: integer, number of cases that the player has found during the party
    #OUTPUTS
        #boulean, 1 if the player has found all the cases and finish the game, else 0

    #the numeber of remaining cases to find is the total number of cases minus the number of cases with a mine minus the number of cases we have already found
    number_of_remaining_cases_to_find = number_of_columns*number_of_rows-number_of_revealed_cases-number_of_mines
    if(number_of_remaining_cases_to_find == 0):
        return 1
    else:
        return 0