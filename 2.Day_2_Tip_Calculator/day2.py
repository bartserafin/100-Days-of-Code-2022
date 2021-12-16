
# DAY 2
    # Data Types

        # String
# indexing  string
# word = 'Hello'
# [start:stop:step]
# [::] from beginning to the end
# print(word[0])
# print(word[::])
# print(word[::-1])
# print(word[:-1:2])

#         # Integer
# print("123" + "345")
# print(123 + 345)
# # this is an integer, you can use _ to make it easier to read
# print(123_345_678)
#
#         # Float
# print(123.345)
#
#         # Boolean
# print(True)
# print(False)

    # Type Error, Type Checking, Type Conversion
# print(type("123"))
# print(type(123))
# print(type(123.456))
# print(type(True))
#
# print(type(str(123)))
# print(type(float("123.123")))

    # Sum up digits in a two digit number
# two_digit_number = input("Type a two digit number: ")
# a = two_digit_number[0]
# b = two_digit_number[1]
# c = int(a) + int(b)
# print(c)

    # Math operators
# PEMDAS from left to right
# Parentheses ()
# Exponents **
# Multiplication *
# Division /
# Addition +
# Subtraction -

# print(3 + 5)
# print(3 - 5)
# print(3 * 5)
# print(3 / 5)
# print(3 ** 5)
# print(3 // 5) # floor division
# print(3 % 5) # module
#
# print(3 * 3 + 3 / 3 - 3) # 9 + 1 - 3 = 7.0

        # Round numbers
# round( number / number, decimal points)
# print(round(8 / 3, 2))

        # f strings and syntax sugar
# score = 1
# score += 1
# print(f"Your score is {score}.")