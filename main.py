from tkinter import *

"""A writer's block solution that deletes the text after 10 seconds of no change."""

# Colors
DARK = "#222831"
MID = "#393E46"
BLUE = "#00ADB5"
WHITE = "#EEEEEE"

timer = None
reps = 0


def start():
    """Starts the count-down for 10 seconds"""
    start_button.grid_forget()
    text.grid(column=0, row=1)
    text.focus()
    window.after(1000, get_first)


def get_first():
    """Gets the contents of the textbox"""
    seconds = 10 - reps
    counter.config(text=f"Counter: {seconds}")
    prior = text.get("1.0", END)
    window.after(1000, lambda: compare(prior))


def compare(prior):
    """Compares the contents from get_first to those taken a second later. If they change, the timer resets.
    If not, the countdown proceeds. If it reaches 0, the textbox deletes all typed text."""
    after = text.get("1.0", END)
    if prior == after:
        global reps
        reps += 1
        seconds = 10 - reps
        counter.config(text=f"Counter: {seconds}")
        if reps == 10:
            text.delete("1.0", END)
            reps = 0
            get_first()
        else:
            get_first()
    else:
        reps = 0
        get_first()


# Window
window = Tk()
window.minsize(400, 400)
window.config(pady=20, padx=20, background=DARK)

# Label and Buttons
header = Label(text="Writer's Block Solution", fg=WHITE, bg=DARK, font=("georgia", 20, "bold"), pady=20)
header.grid(column=0, row=0, columnspan=3)

counter = Label(text="", fg=WHITE, bg=DARK, font=("georgia", 20, "bold"), pady=20)
counter.grid(column=0, row=3, columnspan=3)

start_button = Button(text="Start", bg=MID, fg=BLUE, font=("georgia", 12, "bold"), command=start)
start_button.grid(column=0, row=2, padx=20, pady=20, columnspan=3)
# Text
text = Text(wrap="word", font=("georgia", 12, "normal"))

window.mainloop()
