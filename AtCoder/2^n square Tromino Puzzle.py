def filling_with_tromino(n, rMiss, cMiss):
    tile = [[-1 for i in range(2**n)] for j in range(2**n)]
    merge_algo(tile, n, rMiss, cMiss, 0, 0, 0)
    print_tile(tile)
def merge_algo(tile, n, rMiss, cMiss, rOrigin, cOrigin, mark):
    quadMiss = 2*(rMiss >= 2**(n-1))+(cMiss >= 2**(n-1))
    basicSquare = [(0, 0), (0, 1), (1, 0), (1, 1)]
    if n == 1:
        basicSquare.pop(quadMiss)
        for i, j in basicSquare:
            tile[rOrigin+i][cOrigin+j] = mark
        mark += 1
        return mark
    for i in range(4):
        if i == quadMiss:
            continue
        tile[rOrigin+basicSquare[i][0]+2**(n-1)-1][cOrigin+basicSquare[i][1]+2**(n-1)-1] = mark
    mark += 1
    for i in range(4):
        newrOrigin = rOrigin+basicSquare[i][0]*2**(n-1)
        newcOrigin = cOrigin+basicSquare[i][1]*2**(n-1)
        if i == quadMiss:
            mark = merge_algo(tile, n-1, rMiss%2**(n-1), cMiss%2**(n-1), newrOrigin, newcOrigin, mark)
        else:
            if basicSquare[i][0] == 0:
                newrMiss = 2**(n-1)-1
            else:
                newrMiss = 0
            if basicSquare[i][1] == 0:
                newcMiss = 2**(n-1)-1
            else: 
                newcMiss = 0
            mark = merge_algo(tile, n-1, newrMiss, newcMiss, newrOrigin, newcOrigin, mark)
    return mark
def print_tile(tile):
    for i in range(len(tile)):
        row = ''
        for j in range(len(tile[i])):
            if tile[i][j] != -1:
                row += chr(tile[i][j]+ord('A'))
            else:
                row += ' '
        print(row)
filling_with_tromino(3, 4, 6)