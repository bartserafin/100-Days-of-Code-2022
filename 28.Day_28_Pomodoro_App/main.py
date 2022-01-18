import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
# Pallet taken from https://colorhunt.co/
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text='Timer')
    canvas.itemconfig(timer_text, text='00:00')
    check_mark_label.config(text='')

    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_counter():

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # check for phase
    counter(work_sec)
    if reps % 8 == 0:
        counter(long_break_sec)
        timer_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        counter(short_break_sec)
        timer_label.config(text='Break', fg=PINK)
    else:
        counter(work_sec)
        timer_label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


# .after method for setting up countdown
def counter(count):
    global reps
    reps += 1

    count_min = count // 60
    count_sec = count % 60

    # format to 00:00
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, counter, count - 1)
    else:
        start_counter()
        mark = ''
        for _ in range(0, reps//2):
            mark += '✓'
        check_mark_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
# window setup
window = tkinter.Tk()
window.title('Pomodoro App')
window.config(padx=100, pady=25, bg=YELLOW)


# canvas setup
canvas = tkinter.Canvas(width=200, height=230, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 115, image=tomato_img)

timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


# labels
timer_label = tkinter.Label(text='Timer', font=(FONT_NAME, 40), highlightthickness=0)
timer_label.config(fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

check_mark_label = tkinter.Label(highlightthickness=0)
check_mark_label.config(fg=GREEN, bg=YELLOW)
check_mark_label.grid(column=1, row=3)


# buttons
start_button = tkinter.Button(text='Start', highlightthickness=0, command=start_counter)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


# while True
window.mainloop()