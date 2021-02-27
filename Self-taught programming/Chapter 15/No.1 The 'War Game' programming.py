import random
class Player:
    def __init__(self, name, deck):
        self.name = name
        self.win = 0
        self.deck = deck
    def card(self):
        return self.deck.card_drawing()

class Card:
    deck = []
    marks = ['♠', '♦', '♡', '♧']
    def __init__(self):
        self.dr = 0
        for mark in Card.marks:
            for i in range(1, 14):
                self.deck.append((mark, i))

    def card_drawing(self):
        car = random.choice(self.deck)
        self.deck.remove(car)
        return car

def war_game():
    p1name = input('player1 の名前:')
    p2name = input('player2 の名前:')
    deck = Card()
    player1 = Player(p1name, deck)
    player2 = Player(p2name, deck)
    print(player1.name + ' のカード' + ' :　' + player2.name + '　のカード')

    for counter in range(1, 50):
        p1c = player1.card()
        p2c = player2.card()
        space = len(player1.name) + 7 - (len(str(counter)) + 5 + len(p1c[0]) + len(str(p1c[1])))
        if space < 0:
            space = 0
        print(str(counter) + '回戦　　' + str(p1c[0]) + str(p1c[1]) + ' ' * space +  ':　　' + str(p2c[0]) + str(p2c[1]))
        if p1c[1] > p2c[1]:
                player1.win += 1
        elif p1c[1] < p2c[1]:
                player2.win += 1
        elif p1c[1] == p2c[1]:
                player1.deck.dr += 1
        if player1.deck.deck == []:
                break

    print(player1.name + ' の勝ち数：　' + str(player1.win) + '　'
          + player2.name + 'の勝ち数：　' + str(player2.win) + '　引き分け数：　'
          + str(player1.deck.dr))
    if player1.win > player2.win:
        print(player1.name + 'の勝ちです!')
    elif player1.win < player2.win:
        print(player2.name + 'の勝ちです!')
    elif player1.win == player2.win:
        print('引き分けです！')

while True:
    response = input('qで終了、それ以外のキーでPLAY!:')
    if response == 'q':
        break
    war_game()