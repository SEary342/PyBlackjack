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

    @staticmethod
    def string_cards(card_list, exclude_first=False, print_value=True):
        card_string = ""
        for i, card in enumerate(card_list):
            if exclude_first and i == 0:
                card_string = "(Hidden), "
                continue
            card_string = card_string + str(card) + ", "
        card_string = card_string[: len(card_string) - 2]

        if print_value:
            display_total = Card.cards_value(card_list)
            if exclude_first:
                display_total -= card_list[0].value
            card_string = card_string + f" (Total: {display_total})"

        return card_string

    @staticmethod
    def cards_value(card_list):
        ace_1 = None
        ace_11 = None
        card_sum = 0
        for card in card_list:
            if type(card.value) == tuple:
                ace_1 = card.value[0]
                ace_11 = card.value[1]
            else:
                card_sum = card_sum + card.value
        if ace_1 is not None:
            ace_1_sum = card_sum + ace_1
            ace_11_sum = card_sum + ace_11

            if ace_11_sum > 21:
                return ace_1_sum
            else:
                return ace_11_sum
        else:
            return card_sum


def build_deck():
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            deck.append(Card(rank, suit, RANK_VAL[rank]))
    return _shuffle(deck)


def _shuffle(deck):
    random.shuffle(deck)
    return deck
