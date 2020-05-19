### display board ###
def display_brd(brd):
    row_num = 0
    column_num = 0

    for rows in brd:
        for columns in rows:
            print(columns, end=" ")
            column_num += 1
            if column_num == 3 or column_num == 6:
                print("|", end=" ")
        # for new line
        print('')
        row_num += 1
        column_num = 0
        if row_num == 3 or row_num == 6:
            print("---------------------")


### isFull ###
def isFull(board):
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                return False
    return True


### first Empty ###
def findEmpty(board):
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                return (y, x)


### possible to place ###
def possible(board, x, y, num):
    for i in range(9):
        # check in row
        if board[y][i] == num and i != x:
            return False
        # check in column
        if board[i][x] == num and i != y:
            return False
    boxX = x // 3
    boxY = y // 3
    # check in box
    for j in range(boxY*3, (boxY+1)*3):
        for k in range(boxX*3, (boxX+1)*3):
            if board[j][k] == num and (j, k) != (y, x):
                return False
    return True


### autosolve with backtracking ###
def autosolve(board):

    findSwitch = True
    emptyList = []
    while not isFull(board):
        if findSwitch:
            emptyList.append(findEmpty(board))
        (y, x) = emptyList[-1]
        prevNum = board[y][x]
        num = prevNum + 1
        if num == 10:
            board[y][x] = 0
            emptyList.pop(-1)
            findSwitch = False
        while num < 10:
            if possible(board, x, y, num):
                board[y][x] = num
                findSwitch = True
                break
            if num == 9:
                board[y][x] = 0
                emptyList.pop(-1)
                findSwitch = False
            num += 1


if __name__ == '__main__':
    board = [  # VRY HRD 04
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 3, 6, 8, 4, 0, 0],
        [7, 0, 0, 0, 1, 0, 9, 0, 0],
        [1, 0, 0, 0, 0, 9, 5, 0, 8],
        [0, 3, 6, 0, 0, 0, 7, 9, 0],
        [8, 0, 9, 7, 0, 0, 0, 0, 2],
        [0, 0, 4, 0, 9, 0, 0, 0, 5],
        [0, 0, 1, 2, 5, 6, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 1, 0]
    ]
    display_brd(board)
    autosolve(board)
    print('\n\n')
    display_brd(board)
