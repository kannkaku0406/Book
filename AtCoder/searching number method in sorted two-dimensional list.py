def findTheInteger(T, n):
    record = search(T, n, [0,0])
    if record == None:
        print('No')
    else:
        print(record[0]+1, len(T[0])-record[1])
def search(T, n, record):
    if T == [[]]:
        return None
    target = T[0][-1]
    if target == n:
        return record
    elif target < n:
        record[0] += 1
        return search(T[1:], n, record)
    else:
        record[1] += 1
        return search([l[:-1] for l in T], n, record)
T = [[1,4,7,11,15],
     [2,5,8,12,19],
     [3,6,9,16,22],
     [10,13,14,17,24],
     [18,21,23,26,30]]
n = 21
findTheInteger(T, n)