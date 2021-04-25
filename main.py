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
repls = 0
my_timer = None
flag = 1


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    sh = ""
    sm = ""
    if count / 60 < 10:
        sh = "0"
    else:
        sh = ""

    if count % 60 < 10:
        sm = "0"
    else:
        sm = ""

    canvas.itemconfig(timer_text, text=f"{sh}{int(count / 60)}:{sm}{count % 60}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
    # else:
    #     return


def start_timer():
    global repls
    repls += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    tim = 0
    if (repls + 1) % 2 == 0 and repls > 1:
        get_txt = checkmark.cget("text") + " ✓"
        checkmark.config(text=get_txt, foreground=GREEN, font=("Comic Sans MS", 30, "bold"), bg=YELLOW)
    # else:
    #     label2.config(text="", font=("Comic Sans MS", 30, "bold"), bg=YELLOW)
    if repls % 8 == 0:
        timer_work.config(text="Long-Break", fg=RED)
        tim = long_break
    elif repls % 2 == 0:
        timer_work.config(text="Short-Break", fg=PINK)
        tim = short_break
    else:
        timer_work.config(text="Work", fg=GREEN)
        tim = work_sec

    count_down(tim)


def reset_timer():
    global repls
    repls = 0
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_work.config(text="Timer", fg=GREEN)
    checkmark.config(text="", foreground=GREEN, font=("Comic Sans MS", 30, "bold"), bg=YELLOW)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.minsize(width=400, height=350)

# , highlightthickness=0 #to change the border of the image/Canvas to zero

canvas = Canvas(width=200, height=224, bg=YELLOW)
window.config(padx=80, pady=50, bg=YELLOW)

# Heading
timer_work = Label(text="Timer", foreground=GREEN, font=("Comic Sans MS", 42, "bold"), )
timer_work.config(bg=YELLOW)
timer_work.grid(column=1, row=0)

# Adding Image via Canvas
img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=img)
timer_text = canvas.create_text(102, 130, text="00:00", font=("Comic Sans MS", 22, "normal"), fill="white")
canvas.grid(column=1, row=2)

# Adding the Buttons
calculate = Button(text="Start", command=start_timer, height=1, width=10, font=("Comic Sans MS", 10, "bold"))
calculate.grid(column=0, row=3)

calculate = Button(text="Reset", command=reset_timer, height=1, width=10, font=("Comic Sans MS", 10, "bold"))
calculate.grid(column=2, row=3)

checkmark = Label(text="", foreground=GREEN, font=("Comic Sans MS", 30, "bold"), bg=YELLOW)
checkmark.grid(column=1, row=4)
window.mainloop()
