from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
cycle = 0
checkmarks = 0
timer = ""

# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    global checkmarks
    global cycle
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmarks = 0
    checkmark_label.config(text="")
    cycle = 0


# ---------------------------- TIMER MECHANISM --------------------------- #


def start_timer():
    global cycle
    global checkmarks
    cycle = cycle + 1
    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if cycle % 2 == 0:
        if cycle % 8 == 0:
            count_down(long_break)
            timer_label.config(text="Break", fg=RED)
        else:
            count_down(short_break)
            timer_label.config(text="Break", fg=PINK)
        checkmarks += 1
        checkmark_label.config(text=checkmarks * "✔")
    else:
        count_down(work)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(seconds):
    minute = seconds / 60
    minute = int(minute)
    second = seconds % 60
    if second < 10:
        second = f"0{second}"
    if minute < 10:
        minute = f"0{minute}"
    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if seconds > 0:
        global timer
        timer = window.after(1000, count_down, seconds - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
checkmark_label = Label(font=(FONT_NAME, 10, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)
checkmark_label.grid(column=1, row=3)
start_button = Button(text="start", font=(FONT_NAME, 10), command=start_timer)
reset_button = Button(text="reset", font=(FONT_NAME, 10), command=reset)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


window.mainloop()
