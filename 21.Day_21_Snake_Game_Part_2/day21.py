# Class Inheritance
class Animal:
    # Variable instances
    counter = 2

    # Initializer
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):
    def __init__(self):
        # Inherit everything (both attributes and methods) from Upper Class Animal
        super().__init__()
        self.legs = 0

    def swim(self):
        print("Move in water.")

    def breathe(self):
        super().breathe()
        print("doing this underwater.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.counter)


class Dog:
    def __init__(self):
        self.temperament = "loyal"

    def bark(self):
        print("Woof, woof!")


class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.is_a_good_boy = True

    def bark(self):
        super().bark()
        print("Greetings, good sir. How do you do?")

        
# Slicing lists and dicts
