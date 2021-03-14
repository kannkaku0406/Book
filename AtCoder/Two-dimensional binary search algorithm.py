def findTheInteger(T, n):
    if len(T) == 1 and len(T[0]) == 1:
        if T[0] == n:
            return [0, 0]
        else:
            return [-1, -1]
    else:
        r, c = len(T)//2, len(T[0])//2
        quads = [[l[:c] for l in T[:r]], [l[c:] for l in T[:r]], [l[:c] for l in T[r:]], [l[c:] for l in T[r:]]]
        if T[r][c] == n:
            return [r, c]
        elif T[r][c] > n:
            elim = 3
        else:
            elim = 0
        for i in range(4):
            if i == elim or len(quads[i]) == 0 or len(quads[i][0]) == 0:
                continue
            ans = findTheInteger(quads[i], n)
            if ans == [-1, -1] or ans == None:
                continue
            else:
                return [ans[0]+(i//2)*r, ans[1]+(i%2)*c]
T = [[1,4,7,11,15],
     [2,5,8,12,19],
     [3,6,9,16,22],
     [10,13,14,17,24],
     [18,21,23,26,30]]
n = 5
print(findTheInteger(T, n))