import random

def create_board(board_rows, board_columns):
    #INPUTS
        #define the size of the board with 2 positives integers
            #board_rows : integer between 1 and 1000
            #board_columns : integer between 1 and 1000
    #OUTPUTS
        #board : list of list (2D) containing integers with the number of mine around each case
        #list_of_mines : list of positions of the mines 

    #100% coverage on board size
    if board_columns < 1 :
        print("error number of column is not valid")
    if board_rows < 1 :
        print("error number of rows is not valid")
    if not board_columns.is_integer():
        print("error number of columns is not an integer")
    if not board_rows.is_integer():
        print("error number of rows is not an integer")
    if board_columns >1000 :
        print("error number of columns is too large (over 1000)")
    if board_rows > 1000:
        print("error number of rows is too large (over 1000)")


    #initialize the board with 0
    #board[row_number][column_number]
    board = [[0 for i in range(board_columns)] for j in range(board_rows)]

    #place the mine randomly
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

def print_board(board, list_of_mines):
    board_to_print = board
    for mine_position in list_of_mines:
        board_to_print[mine_position[0]][mine_position[1]] = 'X'
    
    for row in board_to_print:
        for col in row:
            print(str(col) + ' ', end = '')
        print()
    
    print()
    print(list_of_mines)

def print_board_in_game(board, list_of_mines, list_of_revealed_cases):
    board_to_print = board
    for mine_position in list_of_mines:
        board_to_print[mine_position[0]][mine_position[1]] = 'X'
    
    board_to_print = [
        [board_to_print[row][col] if (row, col) in list_of_revealed_cases else "*" for col in range(len(board_to_print[0]))]
        for row in range(len(board_to_print))
    ]

    for row in board_to_print:
        for col in row:
            print(str(col) + ' ', end = '')
        print()
    
    print()
    print(list_of_mines)



board, list_of_mines = create_board(10,10)
print_board(board, list_of_mines)
cases_revealed = []
#Action : clic a case

def is_there_a_mine(row_selection, column_selection, list_of_mines):
    for mine_position in list_of_mines:
        if (row_selection,column_selection) == mine_position:
            return True
    return False

def is_already_revealed(row_selection, column_selection,cases_revealed):
    for case_position in cases_revealed:
        if case_position == (row_selection,column_selection):
            return True
    return False


def perform_action(row_selection, column_selection, board, list_of_mines, cases_revealed):

    if is_already_revealed(row_selection, column_selection, cases_revealed)==True:
        print("You already clicked this case")
    else:
        cases_revealed.append((row_selection,column_selection))
        if(is_there_a_mine(row_selection,column_selection,list_of_mines)):
            return True
        else:
            return False

def case_selection():
    print("Select the row")
    row_selection = int(input())
    print("Select the column")
    col_selection = int(input())
    return row_selection, col_selection

 
is_game_finished = False
while not is_game_finished:
    row_selection,col_selection = case_selection()
    is_game_finished = perform_action(row_selection,col_selection,board,list_of_mines, cases_revealed)
    print_board_in_game(board, list_of_mines, cases_revealed)

print("You lost")