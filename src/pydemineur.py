import random

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

for rows in range(board_rows):
    print(board[rows])

#place the mine randomly
probability_of_mine = 0.1
list_of_mines = []

for i in range(board_columns):
    for j in range(board_rows):
        if(random.random() < probability_of_mine):
            list_of_mines.append((j, i))
        else:
            pass
print(list_of_mines)

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


for rows in range(board_rows):
    print(board[rows])


