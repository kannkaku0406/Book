def judge(n, miss):
    for m in miss:
        if [m[0]+1, m[1]] in miss or [m[0]-1, m[1]] in miss or [m[0], m[1]+1] in miss or [m[0], m[1]-1] in miss:
            return True
    missQuad = {}
    for i in range(4):
        missQuad[i] = False
    for m in miss:
        quad = 2*(m[0] >= 2**(n-1)) + (m[1] >= 2**(n-1))
        if missQuad[quad]:
            return False
        missQuad[quad] = True
    return True
print(judge(3, [[7,1], [0,1], [1,6], [4,5]]))