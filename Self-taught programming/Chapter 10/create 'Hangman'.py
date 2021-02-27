import random
ans_list = ['dog', 'cat', 'house', 'bird', 'horse', 'box', 'tree']
word = ans_list[random.randint(0, len(ans_list) - 1)]
def hangman(word):
    wrong = 0
    stage = ['',
             '___________            ',
             '|                      ',
             '|         |            ',
             '|         0            ',
             '|        /|\           ',
             '|        / \           ',
             '|                      ',
             ]
    rletters = list(word)
    board = ['_'] * len(word)
    while True:
        print('\n')
        ans = input('guess one character. :')
        if ans in rletters:
            index = rletters.index(ans)
            board[index] = ans
            rletters[index] = '_'
            print(''.join(board))
        else:
            print('It is not in the correct word.')
            wrong += 1
            print('\n'.join(stage[:wrong]))
            if wrong == len(stage):
                print('You are lost!\n The correct answer is {}!'.format(wordr))
                break
        if '_' not in board:
            print('You are winner!')
            print('The correct answer is {}!'.format(''.join(board)))
            break
hangman(word)