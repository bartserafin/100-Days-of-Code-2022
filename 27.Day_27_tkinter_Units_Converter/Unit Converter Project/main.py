import tkinter

# create a mile to km converter
# 1 mile = 1.6 km


window = tkinter.Tk()
window.title('Units Converter')
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

# Entries
entry_one = tkinter.Entry(width=20)
entry_one.insert(tkinter.END, string="Insert miles here.")
entry_one.grid(column=1, row=0)

# Labels
label_miles = tkinter.Label(text='Miles', font=('Courier', 8, 'bold'))
label_miles.grid(column=2, row=0)

label_is_equal = tkinter.Label(text='is equal to', font=('Courier', 8, 'bold'))
label_is_equal.grid(column=0, row=1)

label_calculate = tkinter.Label(text=0, font=('Courier', 8, 'bold'))
label_calculate.grid(column=1, row=1)


label_km = tkinter.Label(text='km', font=('Courier', 8, 'bold'))
label_km.grid(column=2, row=1)


# Event listener
def miles_to_km():
    unit_to_convert = entry_one.get()
    label_calculate.config(text=round(float(unit_to_convert) * 1.609, 2))


# Buttons
button = tkinter.Button(text='Calculate', command=miles_to_km)
button.config(padx=5, pady=5)
button.grid(column=1, row=2)










# while True:
window.mainloop()
