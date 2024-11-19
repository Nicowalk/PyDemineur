from utilities import *

def reveal_case(row_selection, column_selection, board, list_of_mines, cases_revealed):

    if is_already_revealed(row_selection, column_selection, cases_revealed)==True:
        print("You already clicked this case")
    else:
        
        if(board[row_selection][column_selection]==0):
            reveal_neighbor_0_cases(row_selection, column_selection, board, cases_revealed)
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

def action_selection():
    print("0 to select, 1 to annotate")
    select_or_annotate = -1
    while (select_or_annotate != 0 | select_or_annotate !=1):
        select_or_annotate = int(input())
        print("Not valid")

    return select_or_annotate
