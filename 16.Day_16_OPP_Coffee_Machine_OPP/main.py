# DAY 16

# So far we used procedural programming
# Now let's do Coffee Machine using Object Oriented Programming

# Class ->> Objects
# Objects has attributes and methods
# Attribute is a fancier variable
# Method is a fancier function

# Turtle Graphics

# from turtle import Turtle, Screen
#
# # create an object from class Turtle from Module turtle
# timmy = Turtle()
# # print(timmy)  # prints a location of timmy in computers memory
# my_screen = Screen()
#
#
# # access attributes for object my_screen
# # print(my_screen.canvwidth)
#
# # access methods
# timmy.shape('turtle')
# timmy.color('red')
# timmy.forward(100)
# my_screen.exitonclick()

###################################
# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
#
# table.align = 'l'
#
# print(table)

######################################

# -------------- Coffee Machine OOP -------------------

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create MENU
MENU = Menu()
operation = CoffeeMaker()
transaction = MoneyMachine()

keep_going = True

while keep_going:
    choice = input(f"​What would you like? {MENU.get_items()}: ")
    if choice == "off":
        keep_going = False
    elif choice == "report":
        operation.report()
        transaction.report()
    else:
        drink = MENU.find_drink(choice)

        if operation.is_resource_sufficient(drink):
            if transaction.make_payment(drink.cost):
                operation.make_coffee(drink)
