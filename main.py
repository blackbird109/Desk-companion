import tkinter as tk
from datetime import datetime
from weather import get_weather

USER_NAME = "Layla Coletti"
SHOW_SECONDS = True

# Coffee Shop Theme
BG = "#3B2418"          # dark coffee brown
TEXT = "#FFF1D0"        # warm cream
ACCENT = "#C68B59"      # caramel
GRAY = "#D3BFA6"


def toggle_seconds(event):
    global SHOW_SECONDS
    SHOW_SECONDS = not SHOW_SECONDS


def update_clock():
    current_hour = datetime.now().hour
    weather = get_weather()

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

    weather_label.config(
        text=f'{weather["temperature"]}\n{weather["condition"]}'
    )

    clock_label.config(text=current_time)

    window.after(1000, update_clock)


window = tk.Tk()

window.title("TIK TOCK DOC")
window.attributes("-fullscreen", True)
window.configure(bg=BG)

window.bind("<Escape>", lambda event: window.destroy())
window.bind("<Button-1>", toggle_seconds)


# Frames
main_frame = tk.Frame(
    window,
    bg=BG
)

top_frame = tk.Frame(
    main_frame,
    bg=BG
)

center_frame = tk.Frame(
    main_frame,
    bg=BG
)

bottom_frame = tk.Frame(
    main_frame,
    bg=BG
)


main_frame.pack(fill="both", expand=True)

top_frame.pack(fill="x", pady=(40, 0))
center_frame.pack(fill="both", expand=True)
bottom_frame.pack(fill="x", pady=(0, 30))


# Greeting
greeting_label = tk.Label(
    top_frame,
    text="",
    font=("Georgia", 32),
    fg=TEXT,
    bg=BG
)


# Weather
weather_label = tk.Label(
    center_frame,
    text="",
    font=("Georgia", 18),
    fg=TEXT,
    bg=BG
)


# Clock
clock_label = tk.Label(
    center_frame,
    text="",
    font=("Georgia", 120),
    fg=ACCENT,
    bg=BG
)


# Instructions
instruction_label = tk.Label(
    bottom_frame,
    text="Tap to hide or show seconds",
    font=("Georgia", 16),
    fg=GRAY,
    bg=BG
)


# Put everything on screen
greeting_label.pack()

weather_label.pack()

clock_label.pack(expand=True)

instruction_label.pack()


update_clock()

window.mainloop()