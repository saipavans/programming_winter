import random

class Card:

    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank

    def __lt__(self, other):
        if self.suite < other.suite:
            return True
        elif self.suite == other.suite and self.rank < other.rank:
            return True
        else:
             False

    def __str__(self):
        return ("Card(Suite/Rank): " + str(self.suite) + "/" + str(self.rank))

class Deck:

    cards = []

    def sort(self):
        self.cards.sort()

    def __init__(self):
        for suite in range(1,5):
            for rank in range(1,14):
                self.cards.append(Card(suite, rank))

    def __str__(self):
        res = ""
        for card in self.cards:
            res += str(card)
        return res

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_hands(self, no_of_hands, no_of_cards):
        hands = []
        for hand_index in range(no_of_cards):
            hand = Hand("Hand" + str(hand_index+1))
            for card_index in range(no_of_cards):
                hand.cards.append(self.cards.pop())
            hands.append(hand)
        return hands

class Hand(Deck):

    def __init__(self, label):
        self.cards = []
        self.label = label




def main():
    deck = Deck()
    print(str(deck))
    deck.shuffle()
    print(str(deck))
    hands = deck.deal_hands(4,5)
    for hand in hands:
        print(hand)


if __name__ == '__main__':
    main()