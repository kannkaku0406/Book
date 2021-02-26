list = ['The', 'fox', 'jumped', 'over', 'the', 'fence', '.']
#a = list[-2]
#b = list.pop(-1)
list[-1] = list[-2] + list.pop(-1)
result = ' '.join(list)
print(result)