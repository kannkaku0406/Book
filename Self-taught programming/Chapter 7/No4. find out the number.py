answers = ['2', '3', '14']
while True:
    players_guess = input('数字を入力')
    if players_guess == 'q':
        break
    else:
        try:
            i = int(players_guess)
            if players_guess in answers:
                print('正解')
                break
            else:
                print('不正解')
        except ValueError:
            print('数字を入力するか、qで終了します')
