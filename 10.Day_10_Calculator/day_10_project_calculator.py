import day_10_project_art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator():
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
    num1 = float(input("What's the first number?: "))

    keep_going = True

    while keep_going:

        for key in operations.keys():
            print(key)

        operation_symbol = input("Pick an operation form the line above: ")

        num2 = float(input("What's the next number?: "))

        for key, values in operations.items():
            if operation_symbol == key:
                answer = operations[key](num1, num2)
                print(f"{num1} {operation_symbol} {num2} = {answer}")

        should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'e' to exit or type 'n'"
                                f" to start a new calculation: ").lower()

        if should_continue == "e":
            print("Goodbye")
            keep_going = False
        elif should_continue == 'n':
            calculator()
        elif should_continue == 'y':
            num1 = answer
        else:
            print("Invalid input.")
            keep_going = False


print(day_10_project_art.logo)
calculator()