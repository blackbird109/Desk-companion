import tkinter as tk
from datetime import datetime

USER_NAME = "Layla Coletti"
SHOW_SECONDS = True


def toggle_seconds(event):
    global SHOW_SECONDS
    SHOW_SECONDS = not SHOW_SECONDS


def update_clock():
    current_hour = datetime.now().hour

    if current_hour < 12:
        greeting = f"Good morning, {USER_NAME}!"
    elif current_hour < 18:
        greeting = f"Good afternoon, {USER_NAME}!"
    else:
        greeting = f"Good evening, {USER_NAME}!"

    if SHOW_SECONDS:
        current_time = datetime.now().strftime("%I:%M:%S %p")
    else:
        current_time = datetime.now().strftime("%I:%M %p")

    greeting_label.config(text=greeting)
    clock_label.config(text=current_time)

    window.after(1000, update_clock)


window = tk.Tk()
window.title("TIK TOCK DOC")
window.attributes("-fullscreen", True)
window.configure(bg="Cornsilk")

window.bind("<Escape>", lambda event: window.destroy())
window.bind("<Button-1>", toggle_seconds)

greeting_label = tk.Label(
    window,
    text="",
    font=("Arial", 50),
    fg="Dark Green",
    bg="Cornsilk",
)

clock_label = tk.Label(
    window,
    text="",
    font=("Arial", 200),
    fg="Dark Green",
    bg="Cornsilk",
)

instruction_lable = tk.Label(
    window,
    text=" Tap to hide or show sec",
    font=("Ariel", 16),
    fg="dark slate gray",
    bg="Cornsilk"
)
instruction_lable.pack(pady=(0, 30))
greeting_label.pack(pady=(40, 10))
clock_label.pack(expand=True)

update_clock()

window.mainloop()