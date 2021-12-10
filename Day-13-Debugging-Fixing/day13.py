    # DAY 13
# Describe the problem
# If you can't explain the code, you wont be able to find bugs

# It might prove useful for learning, to try and reproduce the bug on purpose

############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:   # i does not reach 20, because range(1, 20) will reach 19
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) # randint produces start, stop included, hence the 6 is out of range for dice_imgs
# and starts from 1, not from 0
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994: # missing argument == 1994
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")  # f"" string

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))  #  incorrect use of ==
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# https://pythontutor.com/visualize.html#mode=edit
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item) # out of loop, appending only the last item
#   print(b_list)

# mutate([1,2,3,5,8,13])

# Remember to take a break
# Looking at a code won't tell you the solution on it's own
# Google Stackoverflow
# Run your code after every small change in a code
# Talk to a duck
# Talk to to a friend
