def solveNQueens(n: int):
    board = [list("." * n) for i in range(n)]
    result = []
    helper(n, board, 0, result)
    return result

def helper(size, board, column, result):
    if column >= size:
        answer = ["".join(x) for x in board]
        result.append(list(answer))
    
    for row in range(size):
        if isValid(size, board, row, column):
            board[row][column] = "Q"
            partial = ["".join(x) for x in board]
            print(f'{row} {column}')
            print(partial)
            helper(size, board, column + 1, result)
            board[row][column] = "."

def isValid(size, board, row, column):
    # Check the row
    if 'Q' in board[row]:
        return False
    
    # Check the column
    for i in range(size):
        if board[row][i] == 'Q':
            return False
    row_val = row
    column_val = column
    # Check the diagnols
    # Upper Left Diagnol
    while row > -1 and column > -1:
        if board[row][column] == 'Q':
            return False
        row -= 1
        column -= 1
        
    row = row_val
    column = column_val
    # Upper Right Diagnol
    while row > -1 and column < size:
        if board[row][column] == 'Q':
            return False
        row -= 1
        column += 1
        
    
    row = row_val
    column = column_val
    # Lower Left Diagnol
    while row < size and column > -1:
        if board[row][column] == 'Q':
            return False
        row += 1
        column -= 1
    
    row = row_val
    column = column_val
    # Lower Right Diagnol
    while row < size and column < size:
        if board[row][column] == 'Q':
            return False
        row += 1
        column += 1
    
    return True

test = [list("." * 4) for i in range(4)]
test[0][0] = "Q"
print(isValid(4, test, 3, 1))

print(solveNQueens(4))