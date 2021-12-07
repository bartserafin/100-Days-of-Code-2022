print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


#Write your code below this line
small = 15
medium = 20
large = 25
peperoni_small = 3
peperoni_large = 3
cheese = 1

total = 0

if size == "S":
    total += small
elif size == "M":
    total += medium
elif size == "L":
    total += large
if add_pepperoni == "Y":
    if size == "S":
        total += peperoni_small
    elif size == "M" or size == "L":
        total += peperoni_large
if extra_cheese == "Y":
    total += cheese

print(f"Your final bill is: ${total}.")
