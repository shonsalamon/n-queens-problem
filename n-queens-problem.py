#checking if the list "partial" represents a legal board
def legal(partial, i):
    lst_queens = []
    for lst in partial:
        if "Q" in lst:
            lst_queens.append(lst.index("Q"))
        else:
            break 
    y = len(lst_queens)
    if i in lst_queens:
        return False

    a,b = y-1,i-1
    while a >= 0 and b >= 0:
        if partial[a][b] == "Q":
            return False
        a,b = a-1,b-1
    a,b = y-1,i+1
    while a >= 0 and b < len(partial[0]):
        if partial[a][b] == "Q":
            return False
        a,b = a-1,b+1
    return True

#checking number of legal boards size nxn    
def queens(n):
    board = [[' ' for i in range(n)] for j in range(n)]
    count = check(board,n)
    return count
#recursive function: checking if board is legal
def check(board,n):
    counter = 0
    for i in range(len(board)):
        flag = legal(board,i)
        if  flag:
            if  n == 1:
                counter += 1
                break
            else:
                board[len(board)-n][i] = 'Q'
                counter += check(board,n-1)
                board[len(board)-n][i] = ' '
    return counter 


#Boolean: returns if it is legal to locate queen in board[row][col]
def legal_dragons(board, row, col):
    if board[row][col] == 'D':
        return False

    a,b = row-1,col
    while a >= 0:
        if board[a][b] == 'D':
            break 
        if board[a][b] == 'Q' :
            return False
        a = a-1 

    a,b = row-1,col-1
    while a >= 0 and b >= 0:
        if board[a][b] == 'D':
            break 
        if board[a][b] == 'Q' :
            return False
        a,b = a-1, b-1

    a,b = row, col-1
    while b >= 0:
        if board[a][b] == 'D':
            break 
        if board[a][b] == 'Q' :
            return False
        b = b-1

    a,b = row+1,col-1
    while a < len(board) and b >= 0:
        if board[a][b] == 'D':
            break 
        if board[a][b] == 'Q' :
            return False
        a,b = a+1,b-1

    return True 

    
def queens_dragons(board):
    return queens_dragons_rec(len(board), 0, 0, board)


#counting the number of legal options to locate n queen in board
def queens_dragons_rec(remaining, row, col, board):
    counter = 0
    if remaining == 1 and row == col == len(board)-1 and legal_dragons(board, row, col):
        return 1
    if row == len(board)-1 == col:
        return 0
    if legal_dragons(board, row, col):
        if remaining == 1 :
            counter += 1
        else:
            board[row][col] = 'Q'
            if row < len(board)-1:
                counter += queens_dragons_rec(remaining-1, row+1, col, board)
            else:
                counter += queens_dragons_rec(remaining-1, 0, col+1, board)
            board[row][col] = ' '
    if row < len(board)-1:
        counter += queens_dragons_rec(remaining, row+1, col, board)
    else:
        counter += queens_dragons_rec(remaining, 0, col+1, board)
    return counter 
        
