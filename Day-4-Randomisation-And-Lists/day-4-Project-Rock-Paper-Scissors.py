import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Ask player for a move
move = [rock, paper, scissors]
player = move[int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))]
# Random computer move
computer = move[random.randint(0,2)]
# Print moves
print(f"{player} \n Computer chose:\n{computer}")
# Declare a winner
if player == move[0]:                 # Player picks Rock
    if computer == move[0]:
        print("It's a tie.")
    elif computer == move[1]:
        print("You loose.")
    else:
        print("You win.")
elif player == move[1]:               # Player picks Paper
    if computer == move[0]:
        print("You win.")
    elif computer == move[1]:
        print("It's a tie.")
    else:
        print("You loose.")
elif player == move[3]:               # Player picks Scissors
    if computer == move[0]:
        print("You loose.")
    elif computer == move[1]:
        print("You win.")
    else:
        print("It's a tie.")
else:                                 # Invalid option
    print("Invalid number. You loose.")
