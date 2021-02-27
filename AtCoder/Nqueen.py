def noConflicts(board, current):
    for i in range(current):
        if (board[i] == board[current]):
            return False
        if (current-i == abs(board[current]-board[i])):
            return False
    return True
def rQueen(board, current, size):
    if current == size:
        return True
    else:
        for i in range(size):
            board[current] = i
            if noConflicts(board, current):
                found = rQueen(board, current+1, size)
                if found:
                    return True
    return False
def nQueen(N):
    board = [-1]*N
    rQueen(board, 0, N)
    print(board)
nQueen(4)