    # DAY 3

    # if else
# height = int(input("Height: "))
# if height > 120:
#     print("You can enter.")
# else:
#     print("You cannot enter.")

    # nested conditions
# height = int(input("Height: "))
# age = int(input("Age: "))
#
# if height > 120:
#     if age > 18:
#         print("You can enter and pay a $12 ticket.")
#     elif age > 12:
#         print("You can enter and pay $7 ticket")
#     elif age < 12:
#         print("You can enter and pay $5 ticket.")
# else:
#     print("You cannot enter.")

    # multiple if
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
#
# if height >= 120:
#     print("You can ride!")
#     age = int(input("What is your age?"))
#     if age < 12:
#         print("Child tickets are $5.")
#         bill += 5
#     elif age <= 18:
#         print("Youth tickets are $7.")
#         bill += 7
#     else:   # age > 18
#         print("Adult tickets are $12.")
#         bill += 12
#
#     # Ask for photos
#     photo = input("Do you want a photo taken? Y or No. ")
#     if photo == "Y":
#         bill += 3
#
#     print(f"Your bill is {bill}.")
# else:
#     print("You need to grow taller.")

    # Logical operators AND, OR, NOT
if height >= 120:
    print("You can ride!")
    age = int(input("What is your age?"))
    if age < 12:
        print("Child tickets are $5.")
        bill += 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill += 7
    elif age >= 45 and age <= 55:
        print("You are in your middle-age crisis. You can ride for free.")
    else:
        print("Adult tickets are $12.")
        bill += 12


    # Ask for photos
    photo = input("Do you want a photo taken? Y or No. ")
    if photo == "Y":
        bill += 3

    print(f"Your bill is {bill}.")
else:
    print("You need to grow taller.")