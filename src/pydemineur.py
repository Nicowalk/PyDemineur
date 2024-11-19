#define the size of the board with 2 positives integers
board_columns = 4
board_rows = 5

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

print(board)


