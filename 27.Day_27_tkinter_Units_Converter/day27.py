# DAY 27

# *arg: Many Positional Arguments
def add(*args):
    # args are provided as a tuple, hence we can index
    print(args[0])
    sum_up = 0
    for n in args:
        sum_up += n
    return sum_up


# print(add(5, 3, 2, 4))


# *kwargs: Many Keyword Arguments
def calculate(n, **kwargs):
    # kwargs are provided as dict, we can access key,value paris
    print(kwargs['add'])
    n += kwargs['add']
    n *= kwargs['multiply']
    return n


# print(calculate(2, add=3, multiply=5))

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs['make']
        self.model = kwargs['model']

        # we can use .get method, so it doesnt crash if the object doesnt fill all the attributes when initiated
        self.year = kwargs.get('year')
        self.color = kwargs.get('color')


my_car = Car(make='Nissan', model='GT-R')
# print(my_car.make)  # Nissan
# print(my_car.model) # GT-R
# print(my_car.year)  # this gives None as there is no year= when creating the object my_Car
# print(my_car.color) # this gives None as there is no color= when creating the object my_Car

######################################

# ---- tkinter ---- #

######################################

import tkinter

window = tkinter.Tk()
window.title('GUI Program')
window.minsize(width=500, height=300)
# padding
window.config(padx=20, pady=20)

#### Label ###
my_label = tkinter.Label(text='This is a label.', font=('Arial', 12, 'bold'))
my_label.grid(column=0, row=0)
# my_label.place(x=100, y=50)
# place the label in the window 'bottom', default == center
# expand == True, the label takes the max dimensions in a window


#### Buttons ####

# Event listener
def button_clicked():
    new_text = input_window.get()
    my_label.config(text=new_text)


button = tkinter.Button(text='CLICK ME!', command=button_clicked)
button.config(padx=10, pady=10)
button.grid(column=1, row=1)

new_button = tkinter.Button(text='CLICK ME!', command=button_clicked)
new_button.config(padx=10, pady=10)
new_button.grid(column=2, row=0)


#### Entry ####

input_window = tkinter.Entry(width=10)
input_window.grid(column=3, row=2)

# while True:
window.mainloop()
