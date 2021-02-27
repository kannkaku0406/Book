from collections import deque
def research(x, y, l, h, w):
    area = 0
    coast = 0
    d = deque()
    d.append([x, y])
    while d:
        v = d.popleft()
        if not(0 <= v[0] < h) or not(0 <= v[1] < w) or l[v[0]][v[1]] == '.':
            coast += 1
        elif l[v[0]][v[1]] == '$':
            pass
        elif l[v[0]][v[1]] == '#':
            area += 1
            d.append([v[0]+1, v[1]])
            d.append([v[0]-1, v[1]])
            d.append([v[0], v[1]+1])
            d.append([v[0], v[1]-1])
            l[v[0]][v[1]] = '$'
    return [area, coast]
def solve(l, h, w):
    islands = []
    for i in range(h):
        for j in range(w):
            if l[i][j] == '#':
                islands.append(research(i, j, l, h, w))
    for island in sorted(islands, reverse=True):
        print(island[0], island[1])
h, w = map(int, input().split())
l = []
for _ in range(h):
    l.append(list(input()))
solve(l, h, w)