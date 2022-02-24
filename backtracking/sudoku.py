def solveSudoku(board):
    """
    Do not return anything, modify board in-place instead.
    """
    helper(board, 0, 0)

def helper(board, row, column):
    while board[row][column] != ".":
        column += 1

        if column == 9:
            column = 0
            row += 1

        if row == 9:
            return True
    
    # choose column
    
    for val in range(1, 10):
        if isValid(board, row, column, str(val)):
            board[row][column] = str(val)
            if helper(board, row, column):
                return True

    board[row][column] = "."
    return False


def isValid(board, row, column,  n):
    if n in board[row]:
        return False
    for i in range(len(board[0])):
        if n == board[i][column]:
            return False
    
    boxrow = row - row % 3
    boxcol = column - column % 3
    
    if checksquare(board, boxrow, boxcol, n):
        return True
    else:
        return False


def checksquare(board, row, col, val):
    for r in range(row, row+3):
        for c in range(col, col+3):
            if board[r][c] == val:
                return False
    return True
    

test_board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]


# solveSudoku(test_board)

# print(test_board)

# print(isValid(test_board, 0, 2, "1"))



def test():
    return (False and 
         True)


print(test())