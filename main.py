from random import choice
from art import logo


def card_picker():
    """Picks a random card from the cards list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = choice(cards)
    return random_card


def add_card(card_list):
    """checks the card if it's an ace and do some logic before it adds to the card list"""
    card_to_add = int(card_picker())
    if card_to_add == 11 and sum(card_list) > 10:
        card_to_add = 1

    return card_to_add


def card_check(card_list):
    """Checks the sum of the cards to know if you hit black jack, went over, or is good to add"""
    if sum(card_list) == 21:
        print("Black Jack! You Won!")
        return False
    elif sum(card_list) > 21:
        print("You went over 21. You Lose..")
        return False
    else:
        return True


def dealer_card_check(card_list):
    """checks the dealers sum of cards and goes through the condition"""
    while sum(card_list) < 17:
        card_list.append(card_picker())
    if sum(card_list) == 21:
        print("Dealer hit Black Jack! You lose..")
        return False
    elif sum(card_list) > 21:
        print(f"Dealer's card: {card_list}")
        print("Dealer went over 21. You Won!..")
        return False
    else:
        return True


def first_cards(card_list):
    """adds two random cards to the card list"""
    for first_two_cards in range(2):
        random_card = card_picker()
        if random_card == 11 and sum(card_list) > 10:
            random_card = 1
        card_list.append(random_card)


def compare(player_score, dealer_score):
    """compares user cards against dealer cards and determine who wins"""
    if dealer_card_check(dealer_score):

        if sum(player_score) == sum(dealer_score):
            print(f"Dealer's cards: {dealer_score}")
            print("It's a Tie!!!")
        elif sum(player_score) > sum(dealer_score):
            print(f"Dealer's cards: {dealer_score}")
            print("You beat the dealer! You won!")
        else:
            print(f"Dealer's cards: {dealer_score}")
            print("The Dealer beat you! You Lose..")


def black_jack():
    """activate and starts the game"""
    player_cards = []
    dealer_cards = []

    first_cards(player_cards)
    first_cards(dealer_cards)

    print(f"Your first two cards: {player_cards}")
    print(f"Dealer's first two cards: {dealer_cards[0]}, #")

    pick_card_again = True

    while pick_card_again:

        if not card_check(player_cards):
            pick_card_again = False

        if pick_card_again:

            if input("Do you want to add another card? type 'y' for Yes and 'n' for No: ") == "y":
                player_cards.append(add_card(player_cards))
                print(f"Your card at hand:{player_cards}")
                pick_card_again = card_check(player_cards)
            else:
                pick_card_again = False
                compare(player_cards, dealer_cards)


print(logo)
print("Welcome! Let's Play Black Jack!")


play_again = True

while play_again:

    black_jack()

    if input("Would you like to play again? Type 'y' for Yes and 'n' for no: ") == 'n':
        print("Thank you for playing Black Jack!")
        play_again = False
