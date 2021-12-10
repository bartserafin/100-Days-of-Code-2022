# DAY 8

# function with inputs
def greet():
    print("Hello")
    print("Howday")
    print("heya")


# greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Howday {name}")
    print(f"heya {name}")


# greet_with_name("Bart")

# positional and keyword arguments
def greet_with(name, location):
    print(f"Hello {name}, from {location}")


greet_with("Bart", "Poland")
greet_with(location="Poland", name="Bart")


def greet_with(name="Bart", location="Europe"):
    print(f"Hello {name}, from {location}")


greet_with()
