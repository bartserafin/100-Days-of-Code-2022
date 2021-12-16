    # DAY 4

    # RANDOM
# In Python, pseudorandom numbers are generated using Mersenne Twister algorithmic
import random

random_int = random.randint(1,10)   # random int 1 - 10 included
random_float = random.random()      # random 0.0 and 1.0 - excluded

# 0.00 - 4.999
range_float = random_float * 5      # 5 excluded

love_score = random.randint(1,100)
# print(f"Your love socre is {love_score}.")

    # LISTS
fruits = ["apple", "banana", "kiwi"]
# print(fruits[0])
# print(fruits[-1])

# replace apple with orange
fruits[0] = "orange"
# print(fruits)

# append a list, add to the end
fruits.append("tomato")

# .extend - adds new elements at the end of the list
fruits.extend(["one", "two", "three"])

# .insert - insert at index, element
fruits.insert(2, "sunflower")

# .remove - remove element
fruits.remove("orange")

# .pop - remove and item at given index and return it
fruits.pop(2)

# .clear - removes all items from a list, like del list[::]
# fruits.clear()

# .index - return index of an element
fruits.index("tomato")

# .count - return the number of times element appears
fruits.count("orange")

# .sort - sorts from a to z by default, (key=None, reverse=False)
fruits.sort()

# .reverse - reverses the elements of the list in place
fruits.reverse()

# .copy - return a shallow copy of the list
fruits_2 = fruits.copy()

    # NESTED LISTS - A TABLE
fruits_3 = ["Apples", "Grapes", "Peaches"]
vegetables = ["Spinach", "Tomatoes", "Potatoes"]
dirty_dozen = [fruits, vegetables]
