age = input("What is your current age?")

years_max = 90

years_left = years_max - int(age)
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left.")