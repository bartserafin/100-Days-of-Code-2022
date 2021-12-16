    # DAY 5
    # for loops
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)

    # for loops with range
for number in range(1,10): # 1-2-3...-10 not included
    print(number)

for number in range(1,11, 3): # start, stop, step
    print(number)

total = 0
for number in range(1,101):
    total += number
print(total)