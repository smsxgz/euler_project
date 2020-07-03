from random import shuffle, randint
from collections import Counter


class Monopoly:
    def __init__(self):
        self.board = dict()
        self.board['go'] = 0
        self.board['jail'] = 10
        self.board['c1'] = 11
        self.board['e3'] = 24
        self.board['h2'] = 39
        self.board['r1'] = 5

        self.cc = [2, 17, 33]
        self.ch = [7, 22, 36]
        self.g2j = 30

        self.next_r = {7: 15, 22: 25, 36: 5}
        self.next_u = {7: 12, 22: 28, 36: 12}

        self.cc_cards = ['go', 'jail'] + ['nothing' for _ in range(14)]
        self.ch_cards = [
            'go', 'jail', 'c1', 'e3', 'h2', 'r1', 'next_r', 'next_r', 'next_u',
            'go_back'
        ] + ['nothing' for _ in range(6)]

        self.loc = 0
        self.double_count = 0

    def reset(self):
        shuffle(self.cc_cards)
        shuffle(self.ch_cards)
        self.loc = 0

    def cc_step(self, loc):
        card = self.cc_cards.pop(0)
        self.cc_cards.append(card)
        if card == 'nothing':
            self.loc = loc
        else:
            self.loc = self.board[card]

    def ch_step(self, loc):
        card = self.ch_cards.pop(0)
        self.ch_cards.append(card)
        if card == 'nothing':
            self.loc = loc
        elif card == 'next_r':
            self.loc = self.next_r[loc]
        elif card == 'next_u':
            self.loc = self.next_u[loc]
        elif card == 'go_back':
            self.loc = loc - 3
            if self.loc in self.cc:
                self.cc_step(self.loc)
        else:
            self.loc = self.board[card]

    def step(self, dices):
        d1, d2 = dices
        if d1 == d2:
            self.double_count += 1
        else:
            self.double_count = 0

        if self.double_count == 3:
            self.loc = self.board['jail']
            self.double_count = 0

        loc = (self.loc + d1 + d2) % 40
        if loc in self.cc:
            self.cc_step(loc)

        elif loc in self.ch:
            self.ch_step(loc)

        elif loc == self.g2j:
            self.loc = self.board['jail']

        else:
            self.loc = loc

        return self.loc


def simulation(side=6, n=1000, step=1000):
    env = Monopoly()
    counter = Counter()

    total = 0
    for _ in range(n):
        env.reset()
        for s in range(step):
            dices = [randint(1, side), randint(1, side)]
            loc = env.step(dices)
            if s > step // 2 and s % 100 == 0:
                counter[loc] += 1
                total += 1
    for loc, c in counter.most_common(5):
        print(loc, c / total)


if __name__ == '__main__':
    simulation(side=6, n=100000)
