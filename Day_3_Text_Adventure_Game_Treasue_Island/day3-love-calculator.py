print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

# TRUE
count_true = 0
count_true += name1.count("t")
count_true += name2.count("t")
count_true += name1.count("r")
count_true += name2.count("r")
count_true += name1.count("u")
count_true += name2.count("u")
count_true += name1.count("e")
count_true += name2.count("e")

# LOVE
count_love = 0
count_love += name1.count("l")
count_love += name2.count("l")
count_love += name1.count("o")
count_love += name2.count("o")
count_love += name1.count("v")
count_love += name2.count("v")
count_love += name1.count("e")
count_love += name2.count("e")

score = int(str(count_true) + str(count_love))

if score < 10 or score > 90:
    print(f"Your score is {score}, you will go together like coke and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
