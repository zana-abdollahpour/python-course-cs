from random import shuffle


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cards = [Card(value, suit)
                      for suit in Deck.suits for value in Deck.values]

    def __repr__(self): return f"Deck of {self.count()} cards"

    def __iter__(self): return iter(self.cards)

    def _deal(self, num):
        count = self.count()
        if counts == 0:
            raise ValueError("All cards have been dealt")
        actual = min([count, num])
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def count(self): return len(self.cards)

    def shuffle(self):
        if (self.count() != 52):
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self

    def deal_card(self): return self._deal(1)[0]

    def deal_hand(self, hand_size): return self._deal(hand_size)


d = Deck()

# print(d.cards)
# print(d.count())
# print(d)

for card in d:
    print(card)
