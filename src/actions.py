from utilities import *

#reveal the case that is selected
def reveal_case(row_selection, column_selection, number_of_rows, number_of_columns,board, list_of_mines, cases_revealed):
        #INPUTS
            #row_selection : selected row by the user
            #column_selection : selected column by the user
            #board : list of list (2D) containing integers with the number of mine around each case
            #list of mines : list of positions (row,col) of the mines
            #list_of_revealed_cases : list of the positions (row,col) of revealed cases
        #OUTPUTS
            #integer : 1 if the case contain a mine, 0 if it doesnt


        #check if the revealed case contain a mine
        if(is_there_a_mine(row_selection,column_selection,list_of_mines)):
            #If the revealed case is a mine return 1
            return 1
        else:
            #If the case is not a mine and the integer value stored in the board at this position is 0, reveals all the group of case that also contain a 0, else, just add the case to the list of revealed cases
            if(board[row_selection][column_selection]==0):
                reveal_neighbor_0_cases(row_selection, column_selection,number_of_rows, number_of_columns, board, cases_revealed)

            else:
                cases_revealed.append((row_selection,column_selection))
            #If the revealed case is not a mine return 0
            return 0


#The user select to annotate or select a case to reveal
def action_selection():
    #OUTPUTS
        #select_or_annotate : user selection, integer, 0 to reveal a case, 1 to annotate a case

    select_or_annotate = -1
    #while the input is not 0 or 1
    while (select_or_annotate != 0 and select_or_annotate !=1):
        print("0 to reveal a case, 1 to annotate")
        select_or_annotate = int(input())

    return select_or_annotate


#The user select a case
def case_selection(number_of_rows, number_of_columns):
    #INPUTS
        #number_of_rows : number of rows of the board, integer
        #number_of_columns : number of columns of the board, integer
    #OUTPUTS
        #row_selection : the row number selected by the user, integer
        #col_selection : the column number selected by the user, integer

    #The user select a row number while it is valid
    row_selection = -1
    while not (row_selection>=0 and row_selection<number_of_rows):
        print("Select the row between 0 and " + str(number_of_rows-1))
        row_selection = int(input())
    
    #The user select a column number while it is valid
    col_selection = -1
    while not(col_selection>=0 and col_selection<number_of_columns):
        print("Select the column between 0 and " + str(number_of_columns-1))
        col_selection = int(input())

    return row_selection, col_selection