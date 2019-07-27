import random

SUITS = ("Hearts", "Diamonds", "Clubs", "Spades")
RANKS = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")

RANK_VAL = {
    x: (int(x) if x.isdigit() else ((1, 11) if x == "Ace" else 10)) for x in RANKS
}


class Card:
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value

    def __repr__(self):
        return (
            f"{self.__class__.__name__}({self.rank!r}, {self.suit!r}, {self.value!r})"
        )

    def __str__(self):
        return f"{self.rank} of {self.suit}"


def build_deck():
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            deck.append(Card(rank, suit, RANK_VAL[rank]))
    return shuffle(deck)


def shuffle(deck):
    random.shuffle(deck)
    return deck


if __name__ == "__main__":
    deck = build_deck()
    print(deck)
    for item in deck:
        print(str(item))
    print(len(deck))
