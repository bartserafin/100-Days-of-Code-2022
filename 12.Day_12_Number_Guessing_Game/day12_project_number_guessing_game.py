import random
import day12_project_art


def greet_user():
    print(day12_project_art.logo)
    print("Welcome to the Number Guessing Game!\n"
          "I'm thinking of a number between 1 and 100.\n")

    number = random.randint(1, 100)

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()
    if difficulty == 'easy':
        game(10, number)
    elif difficulty == 'hard':
        game(5, number)
    else:
        print("Invalid option. Game Over.")


def game(attempts, number):
    # Game loop
    keepGoing = True

    while keepGoing:
        if attempts != 0:
            print(f"You have {attempts} remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess > number:
                print("Too high.\nGuess again.")
                attempts -= 1

            elif guess < number:
                print("Too low.\nGuess again.")
                attempts -= 1

            else:
                print(f"You got it! The number was {number}.")
                should_continue = input("Play again? 'y', 'n': ")
                if should_continue == 'y':
                    greet_user()
                else:
                    keepGoing = False
        else:
            print(f"You have run out of guesses. The number was {number}.")
            should_continue = input("Play again? 'y', 'n': ")
            if should_continue == 'y':
                greet_user()
            else:
                keepGoing = False

    print("Goodbye.")

greet_user()

