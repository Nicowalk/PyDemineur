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

def reveal_neighbor_0_cases(row_selection, column_selection, board, cases_revealed):
    rows = len(board)
    cols = len(board[1])

    if (row_selection < 0 or row_selection >= rows or 
        column_selection < 0 or column_selection >= cols or
        (row_selection, column_selection) in cases_revealed):
        return

    if board[row_selection][column_selection] != 0:
        return
    else:
        cases_revealed.append((row_selection, column_selection))

    directions = [(-1, -1), (-1, 0), (-1, 1), 
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    # Recursive call
    for dr, dc in directions:
        reveal_neighbor_0_cases(row_selection + dr, column_selection + dc, board, cases_revealed)