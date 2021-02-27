def minimum_path(x, i, r):
    if i%2 == 0:
        if abs(i) <= 4 or abs(r) <= 4:
            return x + 1
        return x + 2
    else:
        return min(minimum_path(x+1, i+1, r+1), minimum_path(x+1, i-1, r-1))
a, b = map(int, input().split())
c, d = map(int, input().split())
x = 0
if abs(a-c) + abs(b-d) <= 3:
    if a == c and b == d:
        pass
    else:
        x = 1
else:
    i = (c+d-a-b)
    r = (c-d-a+b)
    x = minimum_path(x, i, r)
print(x)