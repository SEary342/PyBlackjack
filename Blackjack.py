from Cards import build_deck

GAME_DECK = []
PLAYER_CARDS = []
DEALER_CARDS = []
PLAYER = None


class Player:
    def __init__(self, money):
        self.money = money

    def win_bet(self, bet):
        self.money = self.money + bet

    def lose_bet(self, bet):
        self.money = self.money + bet

    def get_money(self):
        return self.money


def player_turn():
    pass


def computer_turn():
    pass


def game_loop():
    initialize_game()
    initial_deal()

    # Returns player win status
    return True


def turn_loop():
    pass


def initial_deal():
    for num in range(0, 2):
        PLAYER_CARDS.append(GAME_DECK.pop(0))
        DEALER_CARDS.append(GAME_DECK.pop(0))


def deal():
    pass


def win_check() -> bool:
    pass


def initialize_game():
    global GAME_DECK, PLAYER_CARDS, DEALER_CARDS
    GAME_DECK = build_deck()
    PLAYER_CARDS = []
    DEALER_CARDS = []


def main():
    global PLAYER
    PLAYER = Player(500)

    while True:
        print(f"You have ${PLAYER.get_money}")
        print(f"How much would you like to bet?")
        # TODO: implement input system here
        bet = 20
        win_loss = game_loop()

        if win_loss:
            PLAYER.win_bet(bet)
            status = "Won"
        else:
            PLAYER.lose_bet(bet)
            status = "Lost"

        print(f"Game Over! You {status}!")
        print(f"You have ${PLAYER.get_money} remaining")
        print(f"Play again? Y/N")
        # TODO: implement input system here
        break


if __name__ == "__main__":
    main()
