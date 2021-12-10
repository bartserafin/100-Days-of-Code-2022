############### Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
## Dealer must draw a card if he has < 17 points

import random
import art


def draw_cards(list_of_cards):
    card1 = list_of_cards[random.randint(0, len(list_of_cards) - 1)]
    card2 = list_of_cards[random.randint(0, len(list_of_cards) - 1)]
    return [card1, card2]


def draw_next_card(list_of_cards):
    card = list_of_cards[random.randint(0, len(list_of_cards) - 1)]
    return card


def count_score(cards):
    score = sum(cards)
    return score


def check_ace(cards, score):
    if cards[-1] == 11 and score > 10:
        cards[-1] = 1


def the_winner_is(score1, score2):
    if score1 > score2:
        return '*** You win! ***\n'
    elif score1 == score2:
        return '----> Tie! <----\n'
    else:
        return "): You loose! :(\n"


def game():
    print(art.logo)
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    keepGoing = True

    while keepGoing:
        should_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n").lower()
        if should_continue == 'y':
            player_cards = draw_cards(deck)
            player_score = count_score(player_cards)

            computer_cards = draw_cards(deck)
            computer_score = count_score(computer_cards)

            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Computer first card: {computer_cards[0]}")

            next_card = ''
            while next_card != 'n':

                next_card = input("Type 'y' to get another card, type 'n' to pass:\n").lower()
                if next_card == 'y':

                    # check if the drawn card is an ace, and count as 1 or 11
                    player_cards.append(draw_next_card(deck))
                    check_ace(player_cards, player_score)

                    player_score = count_score(player_cards)
                    print(f"Your cards: {player_cards}, current score: {player_score}")

                    # check if player_score is above 21
                    if player_score > 21:
                        print("Your current score is above 21. You loose.\n")
                        game()

                # next_card == 'n', computer draws cards until it has at least 17 points
                elif next_card == 'n':
                    while computer_score < 17:
                        computer_cards.append(draw_next_card(deck))

                        # check if the drawn card is an ace, and count as 1 or 11
                        check_ace(computer_cards, computer_score)

                        computer_score = count_score(computer_cards)

                        # check if computer_score is above 21
                        if computer_score > 21:
                            print(f"Your cards: {player_cards}, current score: {player_score},\n"
                                  f"Dealer cards: {computer_cards}, Dealer score: {computer_score}.\n"
                                  f"You win!\n")
                            game()

                    # draw winner
                    print(f"Your cards: {player_cards}, current score: {player_score},\n"
                          f"Dealer cards: {computer_cards}, Dealer score: {computer_score}.")

                    print(the_winner_is(player_score, computer_score))
                    game()


                # next_card != 'n' nor 'y'
                else:
                    print("Invalid option. Goodbye.")
                    game()

        elif should_continue == 'n':
            print("Goodbye")
            keepGoing = False

        else:
            print("Invalid option. Goodbye.")
            keepGoing = False
    exit()

game()
