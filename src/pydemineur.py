from board import *
from actions import *
from utilities import *

#Size of the board
number_of_rows = 20
number_of_columns = 20

#Create the game board
board, list_of_mines = create_board(number_of_rows,number_of_columns)

print_board(board, list_of_mines)
#Game data : revealed cases and annotated cases (each case is either : not revealed or revealed; An annotated case is always a not revealed case)
revealed_cases = []
annotated_cases = []

#Condition of the end of game. True when a mine is clicked OR all the mines are
is_game_finished = False

#GAME LOOP
while not is_game_finished:

    #Choose between select a case or annotate a case
    select_or_annotate = action_selection(number_of_rows, number_of_columns)

    #Select the row and column of the board
    row_selection,col_selection = case_selection()

    #Reveal a case
    if(select_or_annotate==0):
        #check if the case was already revealed
        if is_already_revealed(row_selection, col_selection, revealed_cases)==True:
            print("You already clicked this case")
        else:
            # return either 1 if the case was a mine or 0 if not
            case_type = reveal_case(row_selection,col_selection,board,list_of_mines, revealed_cases)

    #Annotate a case
    if(select_or_annotate==1):
        #Check if the case was not already revealed
        if (row_selection, col_selection) in revealed_cases:
            print("Case already revealed")
        else:
            #Check if the case was not already annotated
            if (row_selection, col_selection) in annotated_cases:
                print("Case already annotated")
            else:
                #Add the case position to the list of annotated cases
                annotated_cases.append((row_selection,col_selection))

    #Show the game board updated
    print_board_in_game(board, list_of_mines, revealed_cases, annotated_cases)

    #Check if the game is win or lose
    #TODO
    is_game_finished = case_type

print("You lost")