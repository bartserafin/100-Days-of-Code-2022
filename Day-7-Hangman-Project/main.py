# DAY 7 - HANGMAN GAME!

import random
import hangman_art
import hangman_words
from replit import clear

word_list = hangman_words.word_list
picked_word = list(random.choice(word_list))
blanks = []
guesses = []
lives = 6
keepGoing = True

for letter in picked_word:
    blanks += "_"

print(hangman_art.logo)
print(f"Psst, The solution is {picked_word}.")

while keepGoing:

    if blanks != picked_word:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha():
            print("This is not a letter. Try again")
            continue

        clear()  # only works on replit.com

        if guesses != []:
            print(f"So far you guessed: {guesses}")

        if guess in guesses:
            print(f"You already guessed {guess}. Try another one.")
            continue
        else:
            guesses.append(guess)

        for idx in range(len(picked_word)):
            if picked_word[idx] == guess:
                blanks[idx] = guess
        print(f"{' '.join(blanks)}")

        if guess not in picked_word:
            print(f"You guessed {guess}, that's not in the word. You loose a life.")
            lives -= 1
            if lives == 0:
                print(hangman_art.stages[lives])
                print(f"You lost. The word was {picked_word}.")
                keepGoing = False

    if blanks == picked_word:
        print(blanks)
        print("You win!")
        keepGoing = False

    print(hangman_art.stages[lives])
