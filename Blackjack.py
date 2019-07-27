from cards import build_deck, Card

GAME_DECK = []
PLAYER_CARDS = []
DEALER_CARDS = []
PLAYER = None


class Player:
    def __init__(self, money: int):
        self.money = money

    def win_bet(self, bet: int):
        self.money = self.money + bet

    def lose_bet(self, bet: int):
        self.money = self.money - bet

    def get_money(self):
        return self.money


def main():
    global PLAYER
    PLAYER = Player(500)

    while True:
        print(f"You have ${PLAYER.get_money()}")
        bet = bet_request()

        win_loss = game()

        if win_loss == "Win":
            PLAYER.win_bet(bet)
            status = "Won"
        elif win_loss == "Push":
            status = "Tied"
        elif win_loss == "Loss":
            PLAYER.lose_bet(bet)
            status = "Lost"
        else:
            raise NotImplementedError

        print(f"Game Over! You {status}!")
        print(f"You have ${PLAYER.get_money()} remaining")
        if PLAYER.get_money() == 0:
            print("You ran out of money!")
            print("Thanks for playing!")
            break

        cont_game = ""
        while cont_game not in ("y", "n"):
            cont_game = input(f"Play again? Y/N ").lower()
        if cont_game == "n":
            break
        elif cont_game == "y":
            cont_game == ""
            continue
        else:
            raise NotImplementedError


def bet_request():
    while True:
        input_val = input("How much would you like to bet? ")
        try:
            bet_amt = int(input_val)
            if bet_amt > 0 and bet_amt <= PLAYER.get_money():
                return bet_amt
            elif bet_amt > PLAYER.get_money():
                raise Exception
            else:
                raise ValueError

        except Exception:
            print(
                "Please make a bet less than or equal to your current amount of money."
            )
            print(f"You currently have ${PLAYER.get_money()}")
            continue

        except ValueError:
            print(
                f"You entered '{input_val}'. This is not a valid positive whole number."
            )
            print("Please try again.")
            continue


def game():
    initialize_game()
    initial_deal()
    player_score = player_turn()
    dealer_score = dealer_turn(player_score)
    return win_check(player_score, dealer_score)


def initialize_game():
    global GAME_DECK, PLAYER_CARDS, DEALER_CARDS
    GAME_DECK = build_deck()
    PLAYER_CARDS = []
    DEALER_CARDS = []


def initial_deal():
    for num in range(0, 2):
        deal("D")
        deal("P")


def player_turn():
    while over_check(PLAYER_CARDS, 21):
        print(f"Dealer shows: {Card.string_cards(DEALER_CARDS, True)}")
        print(f"You have: {Card.string_cards(PLAYER_CARDS)}")
        hit_status = ""
        while hit_status not in ("y", "n"):
            hit_status = input(f"Hit? Y/N ").lower()
        if hit_status == "y":
            deal("P")
        else:
            break
    return Card.cards_value(PLAYER_CARDS)


def dealer_turn(player_score: int):
    print(f"Dealer shows: {Card.string_cards(DEALER_CARDS)}")
    min_score = 17
    if player_score < 17:
        min_score = player_score
    while over_check(DEALER_CARDS, min_score):
        deal("D")
        print(f"Dealer shows: {Card.string_cards(DEALER_CARDS)}")
    return Card.cards_value(DEALER_CARDS)


def over_check(card_list: int, threshold_num: int) -> bool:
    return Card.cards_value(card_list) <= threshold_num


def deal(destination: str):
    if destination == "P":
        PLAYER_CARDS.append(GAME_DECK.pop(0))
    elif destination == "D":
        DEALER_CARDS.append(GAME_DECK.pop(0))
    else:
        raise NotImplementedError


def win_check(player_score: int, dealer_score: int) -> str:
    if player_score > 21:
        return "Loss"
    else:
        if dealer_score > 21:
            return "Win"
        elif player_score > dealer_score:
            return "Win"
        elif player_score == dealer_score:
            return "Push"
        else:
            return "Loss"


def get_decks(type: str):
    if type == "G":
        return GAME_DECK
    elif type == "P":
        return PLAYER_CARDS
    elif type == "D":
        return DEALER_CARDS


if __name__ == "__main__":
    main()
