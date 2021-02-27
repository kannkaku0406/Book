def dfs(board, depth, x, y, k):
    if depth == k:
        print(k)
        return True
    if not(0 <= x < H) or not(0 <= y < W) or board[x][y] == '.':
        return False
    board[x][y] = '.'
    if dfs(board, depth+1, x+1, y, k) or dfs(board, depth+1, x-1, y, k) or dfs(board, depth+1, x, y+1, k) or dfs(board, depth+1, x, y-1, k):
        print(x+1, y+1)
        return True
    board[x][y] = '#'
H, W = map(int, input().split())
board = [list(input()) for i in range(H)]
k = 0
for i in range(H):
    for j in range(W):
        if board[i][j] == '#':
            k += 1
for i in range(H):
    for j in range(W):
        dfs(board, 0, i, j, k)