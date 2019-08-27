from collections import Counter

card_value = dict((str(i), i) for i in range(2, 10))
card_value['T'] = 10
card_value['J'] = 11
card_value['Q'] = 12
card_value['K'] = 13
card_value['A'] = 14


class Card:
    def __init__(self, card):
        self.value = card_value[card[0]]
        self.suit = card[1]
        self.card = card

    def __repr__(self):
        return self.card


class Hand:
    def __init__(self, cards):
        self.cards = []
        for c in cards:
            self.cards.append(Card(c))
        self.cards = sorted(self.cards, key=lambda x:(-x.value, x.suit))
        self._rank()

    def _flush(self):
        suits = set()
        for c in self.cards:
            suits.add(c.suit)
        return len(suits) == 1

    def _straight(self):
        return all(self.cards[i].value - self.cards[i+1].value == 1 for i in range(4))

    def _rank(self):
        _straight = self._straight()
        _flush = self._flush()
        if _straight:
            self.keys = [self.cards[0].value]
            if _flush:
                self.rank = 9
            else:
                self.rank = 5
            return

        if _flush:
            self.keys = [c.value for c in self.cards]
            self.rank = 6
            return

        counter = Counter()
        for c in self.cards:
            counter[c.value] += 1

        counter = sorted(counter.items(), key=lambda x: (x[1], x[0]), reverse=True)
        self.keys = [c[0] for c in counter]
        if counter[0][1] == 4:
            self.rank = 8
        elif counter[0][1] == 3:
            if counter[1][1] == 2:
                self.rank = 7
            else:
                self.rank = 4
        elif counter[0][1] == 2:
            if counter[1][1] == 2:
                self.rank = 3
            else:
                self.rank = 2
        else:
            self.rank = 1

    def __gt__(self, other):
        if self.rank > other.rank:
            return True
        if self.rank == other.rank:
            for k1, k2 in zip(self.keys, other.keys):
                if k1 == k2:
                    continue
                else:
                    return k1 > k2
        return False



if __name__ == '__main__':
    with open('p054_poker.txt', 'r') as f:
        res = 0
        for line in f.readlines():
            cards = line.split(' ')
            if Hand(cards[:5]) > Hand(cards[5:]):
                res += 1
    print(res)
