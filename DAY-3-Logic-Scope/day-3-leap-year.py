year = int(input("What year do tou want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")