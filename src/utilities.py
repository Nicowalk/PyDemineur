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