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
window.configure(bg="Champaign")

window.bind("<Escape>", lambda event: window.destroy())
window.bind("<Button-1>", toggle_seconds)

main_frame = tk.Frame(
    window,
    bg="Champaign"
)

top_frame = tk.Frame(
    main_frame,
    bg="Champaign"
)

center_frame = tk.Frame(
    main_frame,
    bg="Champaign"
)

bottom_frame = tk.Frame(
    main_frame,
    bg="Champaign"
)

main_frame.pack(fill="both", expand=True)

top_frame.pack(fill="x", pady=(35, 0))
center_frame.pack(fill="both", expand=True)
bottom_frame.pack(fill="x", pady=(0, 25))

greeting_label = tk.Label(
    top_frame,
    text="",
    font=("Arial", 30),
    fg="DarkGreen",
    bg="Champaign",
)

clock_label = tk.Label(
    center_frame,
    text="",
    font=("Arial", 120),
    fg="DarkGreen",
    bg="Champaign",
)

instruction_label = tk.Label(
    bottom_frame,
    text="Tap to hide or show seconds",
    font=("Arial", 16),
    fg="dark slate gray",
    bg="Champaign",
)

greeting_label.pack()
clock_label.pack(expand=True)
instruction_label.pack()


update_clock()

window.mainloop()