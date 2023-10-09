import tkinter
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = ""


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    global reps
    reps = 0
    label_timer["text"] = "Timer"
    label_timer["fg"] = GREEN
    canvas.itemconfig(timer_text, text="00:00")
    label_checkmark["text"] = " "


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label_timer["text"] = "Break"
        label_timer["fg"] = RED
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label_timer["text"] = "Break"
        label_timer["fg"] = PINK
        count_down(short_break_sec)
    else:
        label_timer["text"] = "Work"
        label_timer["fg"] = GREEN
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if int(count_sec) < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = " "
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
        label_checkmark["text"] = mark


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_pic)

timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label_timer = tkinter.Label(text="Timer", font=(FONT_NAME, 40), fg=GREEN, bg=YELLOW)
label_timer.grid(column=1, row=0)

button_start = Button(text="Start", command=start_timer, highlightbackground=YELLOW)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", highlightbackground=YELLOW, command=reset)
button_reset.grid(column=2, row=2)

label_checkmark = tkinter.Label(bg=YELLOW, fg=GREEN)
label_checkmark.grid(column=1, row=3)

window.mainloop()
