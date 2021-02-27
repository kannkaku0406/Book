file = 'C:/Users/user/Desktop/Answer.txt'
answer = input('What is your favorite color ?: ')
with open(file, 'w', encoding = 'utf-8') as f:
    f.write(answer)