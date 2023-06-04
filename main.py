from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
NEW_GREEN = "#B9F8D3"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
FONT = (FONT_NAME, 25, "bold")
COLOR = "white"
BUTTON_FONT = (FONT_NAME, 10, "bold")
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global reps
    reps = 0
    timer_label.config(text="TIMER")
    check_mark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    # Using dynamic typing where we are changing a same variable form int to str and vice-versa
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        global reps
        marks = ""
        # making variable for better understanding
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


# window
window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

# canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_pic)
timer_text = canvas.create_text(100, 130, text="00:00", font=FONT, fill=COLOR)
canvas.grid(column=1, row=2)


# Timer label
timer_label = Label(text="TIMER", font=(
    "Times New Roman", 30, "bold"), fg=GREEN, bg=YELLOW)
# fg->foreground
timer_label.grid(column=1, row=0)

# Start button

start_button = Button(text="Start", font=BUTTON_FONT,
                      activebackground=GREEN, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)

# Reset button
reset_button = Button(text="Reset", font=BUTTON_FONT,
                      activebackground=GREEN, highlightthickness=0, command=reset)
reset_button.grid(column=2, row=3)

# Check marks
check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=4)


window.mainloop()
