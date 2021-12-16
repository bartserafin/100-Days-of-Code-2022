
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Write the rest of your code below this line 👇
number = random.randint(1,2)
if number == 1:
    print("Heads")
else:
    print("Tails")