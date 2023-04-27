from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 3
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    check.config(text="")
    canvas.itemconfig(time_counter, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)

        check.config(text="")
        countdown(long_break_sec)

    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        countdown(short_break_sec)

    else:
        countdown(work_sec)

        timer_label.config(text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------

def countdown(number):
    global timer

    minutes = number / 60
    minutes = math.floor(minutes)
    seconds = number % 60

    if seconds == 0:
        seconds = "00"

    elif seconds < 10:
        seconds = f"0{seconds}"

    if minutes == 0:
        minutes = "00"

    elif minutes < 10:
        minutes = f"0{minutes}"

    canvas.itemconfig(time_counter, text=f"{minutes}:{seconds}")
    if number > 0:
        number -= 1
        timer = window.after(1000, countdown, number)
    else:
        start_timer()
        mark = ""
        global reps
        work_session = math.floor(reps / 2)

        for item in range(work_session):
            mark += "✔"
        check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "normal"), bg=YELLOW)
start = Button(text="Start", command=start_timer)
reset = Button(text="Reset", command=reset_timer)
check = Label(text="", fg=GREEN, bg=YELLOW)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")

canvas.create_image(100, 112, image=tomato)
time_counter = canvas.create_text(100, 130, fill="white", text="00:00", font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start.grid(column=0, row=2)
reset.grid(column=2, row=2)
check.grid(column=1, row=4)

window.mainloop()
