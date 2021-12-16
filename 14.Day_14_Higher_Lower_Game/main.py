import random
import art
from game_data import data
import replit


def pick_person():
    return data[random.randint(0, len(data) - 1)]


def check_people(person1, person2):
    if person1["follower_count"] >= person2["follower_count"]:
        return 'A'
    else:
        return 'B'


def game(score, option_A):

    keepGoing = True

    while keepGoing:
        option_B = pick_person()

        while option_B == option_A:
            option_B = pick_person()

        replit.clear()
        print(art.logo)
        if score != 0:
          print(f"You are right. Current score: {score}")
        print(f"Compare A: {option_A['name']}, a {option_A['description']}, from {option_A['country']}")
        print(art.vs)
        print(f"Compare B: {option_B['name']}, a {option_B['description']}, from {option_B['country']}")

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        correct_answer = check_people(option_A, option_B)

        if guess == correct_answer:
            score += 1
            game(score, option_B)
        else:
            print(art.logo)
            print(f"Sorry, that's wrong. Your final score is {score}.")
            should_continue = input("Do you want to play again? Type 'y' or 'n': ").lower()
            if should_continue != 'y':
                print("Goodbye :D")
                # why this doesnt work?
                # keepGoing = False
                exit()
            else:
                game(0, pick_person())


game(0, pick_person())