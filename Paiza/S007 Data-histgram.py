s = input()
l = [0]*26
multiplier = 1
first = -1
for i in range(len(s)):
    if (0 <= ord(s[i])-ord('a') < 26):
        if first != -1:
            multiplier *= int(s[first:i])
            l.append(int(s[first:i]))
            first = -1
            l[ord(s[i])-ord('a')] += multiplier
            multiplier /= l.pop()
        else:
            l[ord(s[i])-ord('a')] += multiplier
    elif s[i] == '(':
        multiplier *= int(s[first:i])
        l.append(int(s[first:i]))
        first = -1
    elif s[i] == ')':
        multiplier /= l.pop()
    else:
        if first == -1:
            first = i
for i in range(26):
    print(chr(ord('a')+i), int(l[i]))