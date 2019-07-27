import unittest
import copy
from blackjack import Player, initialize_game, get_decks, deal, win_check, over_check
from cards import Card


class Test_Funds(unittest.TestCase):
    def test_player(self):

        # Get money test
        money_amt = 750
        test_player = Player(money_amt)
        self.assertEqual(test_player.get_money(), money_amt)

        # Loss test
        money_amt -= 25
        test_player.lose_bet(25)
        self.assertEqual(test_player.get_money(), money_amt)

        # Win test
        money_amt += 50
        test_player.win_bet(50)
        self.assertEqual(test_player.get_money(), money_amt)


class Test_Deck_Methods(unittest.TestCase):
    def test_deal(self):

        # Test Setup
        initialize_game()
        local_deck = copy.deepcopy(get_decks("G"))

        # Player Deal
        deal("P")
        self.assertEqual(local_deck[0], get_decks("P")[0])

        # Dealer Deal
        deal("D")
        self.assertEqual(local_deck[1], get_decks("D")[0])


class Status_Checks(unittest.TestCase):
    def test_win_check(self):
        self.assertEqual(win_check(12, 13), "Loss")
        self.assertEqual(win_check(13, 13), "Push")
        self.assertEqual(win_check(21, 18), "Win")
        self.assertEqual(win_check(22, 18), "Loss")

    def test_over_check(self):
        card_list = [
            Card("5", "Hearts", 5),
            Card("6", "Spades", 6),
            Card("King", "Spades", 10),
            Card("Ace", "Spades", (1, 11)),
        ]
        card_list2 = [Card("5", "Hearts", 5), Card("6", "Spades", 6)]

        self.assertEqual(over_check(card_list, 21), False)
        self.assertEqual(over_check(card_list, 32), True)

        self.assertEqual(over_check(card_list2, 11), True)
        self.assertEqual(over_check(card_list2, 10), False)
