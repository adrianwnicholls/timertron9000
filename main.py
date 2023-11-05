import datetime as dt
from tkinter import *
import winsound

# Constants
RED = '#FF1E00'
PALE_BLUE = '#E8F9FD'
GREEN = '#59CE8F'
BLACK = '#000000'
FONT_NAME = "Courier"
REPS = 10  # Number of reps to do each exercise for.
REP_LENGTH = 20  # Number of seconds to do a single rep for.
EXERCISES = ["Flexion passive", "Flexion Active", "Tip passive", "Tip active", "Hook", "Fist"]
exercise = 0
rep = 0
timer = None


# --------------------------Start timer ----------------------------------------
def start_timer():
    global exercise_label
    global exercise
    global rep
    start_button.config(text="Pause", command=pause_timer)
    if exercise < len(EXERCISES):
        exercise_label.config(text=f"Exercise:{EXERCISES[exercise]} ")
        exercise += 1
        rep += 1
        count_down(REP_LENGTH)
    else:
        now = dt.datetime.now()
        exercise_label.config(text=f"Exercise finished at {now.hour}:{now.minute} ")
        rep_count_label.config(text="")
        countdown_label.config(text=f"LOG the time! ")



def pause_timer():
    window.after_cancel(timer)
    countdown_label.config(text=f"Countdown:paused")
    start_button.config(text="Resume", command=continue_timer)


def continue_timer():
    start_button.config(text="Pause", command=pause_timer)
    count_down(REP_LENGTH)


# --------------------------Reset timer ----------------------------------------
def reset_timer():
    window.after_cancel(timer)
    countdown_label.config(text="")
    exercise_label.config(text="")
    rep_count_label.config(text="")
    start_button.config(text="Start", command=start_timer)
    global rep
    rep = 0
    global exercise
    exercise = 0


# -------------------------- Countdown mechanism ----------------------------------------
def count_down(count):
    if count > 9:
        countdown_label.config(text=f"Countdown: {count}")
    else:
        countdown_label.config(text=f"Countdown:  {count}")
    global rep
    global timer
    rep_count_label.config(text=f"Rep: {rep} of {REPS}")
    if count == 0:
        winsound.Beep(1500, 250)
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    elif rep < REPS:
        rep += 1
        timer = window.after(1000, count_down, REP_LENGTH)
    else:
        winsound.Beep(1500, 250)

        rep = 0
        start_timer()


# -------------------------- UI -------------------------------------------

window = Tk()
window.title("Timertron 9000")
window.config(padx=100, pady=50, bg=PALE_BLUE)

title_label = Label(text="Timertron 9000", fg=GREEN, bg=PALE_BLUE, font=(FONT_NAME, 60))
title_label.grid(column=1, row=0)

countdown_label = Label(text="", fg=RED, bg=PALE_BLUE, font=(FONT_NAME, 40))
countdown_label.grid(column=1, row=3)

exercise_label = Label(text="", fg=GREEN, bg=PALE_BLUE, font=(FONT_NAME, 40))
exercise_label.grid(column=1, row=1)

rep_count_label = Label(text="", fg=RED, bg=PALE_BLUE, font=(FONT_NAME, 40))
rep_count_label.grid(column=1, row=2)

start_button = Button(text="Start", highlightthickness=0, command=start_timer, fg=RED, bg=PALE_BLUE,
                      font=(FONT_NAME, 20))
start_button.grid(column=0, row=4)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer, fg=RED, bg=PALE_BLUE,
                      font=(FONT_NAME, 20))
reset_button.grid(column=2, row=4)

window.mainloop()
