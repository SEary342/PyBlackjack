import unittest
import copy
from cards import Card, build_deck, shuffle


class Test_Card_Methods(unittest.TestCase):
    card_list = [
        Card("5", "Hearts", 5),
        Card("6", "Spades", 6),
        Card("King", "Spades", 10),
    ]

    def test_card_reps(self):
        test_card = Card("5", "Hearts", 5)
        self.assertEqual(str(test_card), "5 of Hearts")

    def test_string_cards(self):
        self.assertEqual(
            Card.string_cards(Test_Card_Methods.card_list),
            "5 of Hearts, 6 of Spades, King of Spades (Total: 21)",
        )
        self.assertEqual(
            Card.string_cards(Test_Card_Methods.card_list, True),
            "(Hidden), 6 of Spades, King of Spades (Total: 16)",
        )
        self.assertEqual(
            Card.string_cards(Test_Card_Methods.card_list, True, False),
            "(Hidden), 6 of Spades, King of Spades",
        )

    def test_card_value(self):

        # Test non-Ace
        self.assertEqual(Card.cards_value(Test_Card_Methods.card_list), 21)

        # Test Ace
        card_list2 = [Card("5", "Hearts", 5), Card("Ace", "Hearts", (1, 11))]
        self.assertEqual(Card.cards_value(card_list2), 16)

        # Push the total over 21 with Ace == 11
        card_list2.append(Card("King", "Hearts", 10))
        self.assertEqual(Card.cards_value(card_list2), 16)


class Test_Deck_Build_Methods(unittest.TestCase):
    def test_deck_build(self):
        local_deck = build_deck()
        self.assertEqual(len(local_deck), 52)

    def test_shuffle(self):
        local_deck = build_deck()
        orig_deck = copy.deepcopy(local_deck)
        new_deck = shuffle(local_deck)
        self.assertCountEqual(orig_deck, new_deck)
