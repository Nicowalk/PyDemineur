import random

def create_board(board_rows, board_columns):
    #INPUTS define the size of the board with 2 positives integers
        #board_rows : integer between 1 and 100
        #board_columns : integer between 1 and 100
    #OUTPUTS
        #board : list of list (2D) containing integers with the number of mine around each case
        #list_of_mines : list of positions of the mines 
    max_size_board  = 100

    #100% coverage on board size
    if board_columns < 1 :
        print("error number of column is not valid")
    if board_rows < 1 :
        print("error number of rows is not valid")
    if not board_columns.is_integer():
        print("error number of columns is not an integer")
    if not board_rows.is_integer():
        print("error number of rows is not an integer")
    if board_columns >max_size_board :
        print("error number of columns is too large (over " + max_size_board + ")")
    if board_rows > max_size_board:
        print("error number of rows is too large (over " + max_size_board + ")")


    #initialize the board with 0
    #board[row_number][column_number]
    board = [[0 for i in range(board_columns)] for j in range(board_rows)]

    #place the mine randomly with a probability of 0.1
    probability_of_mine = 0.1
    list_of_mines = []

    for i in range(board_columns):
        for j in range(board_rows):
            if(random.random() < probability_of_mine):
                list_of_mines.append((j, i))
            else:
                pass

    #add the count of the number of mine around each case by adding 1 around each mine when we are not at the edge of the board
    for mine_position in list_of_mines:
        if mine_position[0] != 0:
            if mine_position[1] != 0:
                board[mine_position[0]-1][mine_position[1]-1] += 1
            board[mine_position[0]-1][mine_position[1]] += 1
            if mine_position[1] != board_columns-1:
                board[mine_position[0]-1][mine_position[1]+1] += 1
        if mine_position[1] != 0:
            board[mine_position[0]][mine_position[1]-1] += 1
        if mine_position[1] != board_columns-1:
            board[mine_position[0]][mine_position[1]+1] += 1
        if mine_position[0] != board_rows-1:
            if mine_position[1] != 0:
                board[mine_position[0]+1][mine_position[1]-1] += 1
            board[mine_position[0]+1][mine_position[1]] += 1
            if mine_position[1] != board_columns-1:
                board[mine_position[0]+1][mine_position[1]+1] += 1
    return board, list_of_mines

#Print the board revealed with values and mines. Also print the mines position. Used for debug
def print_board(board, list_of_mines):
    #INPUTS
        #board : 2D array of the board with integer that represent the number of mine around each case
        #list of mines : list of positions (row,col) of the mines
    board_to_print = board
    for mine_position in list_of_mines:
        board_to_print[mine_position[0]][mine_position[1]] = 'X'
    
    for row in board_to_print:
        for col in row:
            print(str(col) + ' ', end = '')
        print()
    
    print()
    print(list_of_mines)

#Print the game board in the terminal
def print_board_in_game(board, list_of_mines, list_of_revealed_cases, list_annotated_cases):
    #INPUTS
        #board : 2D array of the board with integer that represent the number of mine around each case
        #list of mines : list of positions (row,col) of the mines
        #list_of_revealed_cases : list of the positions (row,col) of revealed cases
        #list_annotated_cases : list of the positions (row,col) of the annotated cases
    
    #create board_to_print that contains X for the location of the mine and an integer that represent the number of mine around the case
    board_to_print = board
    for mine_position in list_of_mines:
        board_to_print[mine_position[0]][mine_position[1]] = 'X'

    temp_board = []

    #Fill temp_board with "°" if cell is annotated, "*" is cell is not revealed. Else, the value of board_to_print
    for row in range(len(board_to_print)):
        new_row = []
        for col in range(len(board_to_print[0])):
            #If the cell is revealed
            if (row, col) in list_of_revealed_cases:
                new_row.append(board_to_print[row][col])
            else:
                #If the cell is annotated
                if (row, col) in list_annotated_cases:
                    new_row.append("°")
                #If the cell is not revealed
                else:
                    new_row.append("*")
        temp_board.append(new_row)

    board_to_print = temp_board

    #Add a space at the end of each caracter for readability
    for row in board_to_print:
        for col in row:
            print(str(col) + ' ', end = '')
        print()
    
    print()