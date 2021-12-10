def prime_checker(number):
    div_numbers = []
    for el in range(2, number):
        div_numbers.append(el)
    if number > 1:
        for num in div_numbers:
            if number % num == 0:
                print("It's not a prime number.")
                break
        else:
            print("It's a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)