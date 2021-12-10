import day_9_project_art
import replit

print(day_9_project_art.logo)
print("Welcome to the secret auction program.")

buyers = {}

keepGoing = True
while keepGoing:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    buyers[name] = bid

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if should_continue == 'no':
        keepGoing = False
    
    replit.clear()  # only works in replit.com

max_bid = 0
max_name = ''
for name, bid in buyers.items():
    print(f"{name} bid ${bid}")
    if bid > max_bid:
        max_bid = bid
        max_name = name

print(f"The winner is {max_name} with a bid of {max_bid}")






