# DAY 15 COFFEE MACHINE

# REQUIREMENTS
# 1. Print report (resources left)
# 2. Check resources
# 3. Process coins and returns change
# 4. Check if transaction successful
# 5. Make coffee with emoji
# 6. Refill resources

# Example

# What would you like (espresso/latte/cappuccino): report

# water
# milk
# coffee
# money
# What would you like (espresso/latte/cappuccino):

# What would you like (espresso/latte/cappuccino): latte

# please insert coins
# how many quarters?:
# how many dimes?:
# how many nickles?:
# how many pennies?:

# Here is {change} in change.
# Here is your latte emoji Enjoy!

# Sorry, that's not enough money. Your money is refunded.

# What would you like (espresso/latte/cappuccino):cappuccino
# Sorry there is not enough water.

# What would you like (espresso/latte/cappuccino): refill

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins_inserted = {
    'penny': 0,
    'nickel': 0,
    'dime': 0,
    'quarter': 0
}

coins_inside_the_machine = {
    'penny': 0,
    'nickel': 0,
    'dime': 0,
    'quarter': 0
}

coins = {
    'penny': 0.01,
    'nickel': 0.05,
    'dime': 0.1,
    'quarter': 0.25
}


def report(status, coins_inside):
    for key, value in status.items():
        print(f"{key} : {value}")

    money = 0
    for key, value in coins_inside.items():
        money += value * coins[key]
    print(f"Money: ${money}")


def refill():
    resources['water'] = 300
    resources['milk'] = 200
    resources['coffee'] = 100


def make_espresso():
    espresso_cost = MENU['espresso']['cost']
    print(f"Your coffee costs ${espresso_cost}")
    if check_resources('espresso'):
        if handle_coins(espresso_cost):
            print("\n\t ----- Here's your espresso. ☕. Enjoy! -----\n")


def make_latte():
    latte_cost = MENU['latte']['cost']
    print(f"Your coffee costs ${latte_cost}")
    if check_resources('latte'):
        if handle_coins(latte_cost):
            print("\n\t ----- Here's your latte. ☕. Enjoy! -----\n")


def make_cappuccino():
    cappuccino_cost = MENU['cappuccino']['cost']
    print(f"Your coffee costs ${cappuccino_cost}")
    if check_resources('cappuccino'):
        if handle_coins(cappuccino_cost):
            print("\n\t ----- Here's your cappuccino. ☕. Enjoy! -----\n")


def check_resources(product_name):
    for key, value in MENU[product_name]['ingredients'].items():
        if value > resources[key]:
            print(f"Sorry, there is not enough {key}. Please refill the machine.")
            return False
        else:
            resources[key] -= value
    return True


def handle_change(money):
    for key, value in coins.items():
        if money > value:
            number_of_coins = money // value    # what if there isn't any coins with this value?
            coins_inside_the_machine[key] -= number_of_coins
            # This uses greedy algorithms, maybe wrong choice for this project?
            # Consider option where required coins to give change is not sufficient (less than 0 left in the machine)

            sum_of_change = number_of_coins * value
            if sum_of_change == money:
                return True


def handle_coins(cost):
    print("Please insert coins.")
    money_given = 0

    while money_given < cost:
        for key in coins.keys():
            coins_inserted[key] += int(input(f"How many {key}?: "))

        for key in coins_inserted.keys():
            money_given += coins_inserted[key] * coins[key]
        if money_given < cost:
            print("Sorry, that's not enough money. Your money is refunded.")
            for key in coins_inserted.keys():
                coins_inserted[key] = 0
                money_given = 0

    # Update the coins inside the machine
    for key in coins_inserted.keys():
        coins_inside_the_machine[key] += coins_inserted[key]

    # Handle the change
    if money_given > cost:
        change = money_given - cost
        if handle_change(change):   # Updates coins in the machine after change is given
            print(f"Thank you so much. Here is your ${change} in change.")
            return True
    else:   # money_given == cost
        print("Thank you so much.")
        return True


while True:
    choice = input("What would you like (espresso/latte/cappuccino)"
                   " or to check the machine, type 'report' or type 'refill' to refill the resources: ").lower()
    if choice == 'report':
        report(resources, coins_inside_the_machine)
    elif choice == 'refill':
        refill()
    elif choice == 'espresso':
        make_espresso()
    elif choice == 'latte':
        make_latte()
    elif choice == 'cappuccino':
        make_cappuccino()
    else:
        print("Invalid option")
