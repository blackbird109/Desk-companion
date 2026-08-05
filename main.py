# -*- coding: utf-8 -*-

import tkinter as tk
from datetime import datetime
from modules.weather import get_weather
from modules.countdown import get_next_event
from modules.messages import get_daily_message
from modules.settings import *

SHOW_SECONDS = True

# Theme
BG = "#000000"
TEXT = "#7B1FA2"
ACCENT = "#32CD32"
PINK = "#FF6B6B"


def toggle_seconds(event):
    global SHOW_SECONDS
    SHOW_SECONDS = not SHOW_SECONDS


def update_clock():
    now = datetime.now()
    hour = now.hour

    # Weather
    try:
        weather = get_weather()
        weather_text = f'{weather["temperature"]}\n{weather["condition"]}'
    except Exception as e:
        weather_text = f"Weather unavailable\nError: {e}"

    # Countdown
    try:
        event = get_next_event()
        countdown_text = f'{event["name"]}\n{event["days"]}'
    except Exception as e:
        countdown_text = f"Event unavailable\nError: {e}"

    # Message
    try:
        message = get_daily_message()
    except Exception as e:
        message = f"Message unavailable Error: {e}"

    # Greeting
    if 4 <= hour < 12:
        greeting = f"Good Morning!"
    elif 12 <= hour < 16:
        greeting = f"Good Afternoon!"
    elif 16 <= hour < 21:
        greeting = f"Good Evening!"
    else:
        greeting = f"Good Night"  
    
    greeting = f"{greeting}, {USER_NAME}!"


    # Clock
    if SHOW_SECONDS:
        current_time = now.strftime("%I:%M:%S %p")
    else:
        current_time = now.strftime("%I:%M %p")

    greeting_label.config(text=greeting)
    weather_label.config(text=weather_text)
    countdown_label.config(text=countdown_text)
    message_label.config(text=message)
    clock_label.config(text=current_time)

    window.after(1000, update_clock)


# Window
window = tk.Tk()
SCREEN_WIDTH = window.winfo_screenwidth()
SCREEN_HEIGHT = window.winfo_screenheight()
if SCREEN_HEIGHT <= 600:
    GREETING_SIZE = 24
    CLOCK_SIZE = 84
    TITLE_SIZE = 14
    TEXT_SIZE = 14
    INSTRUCTION_SIZE = 10
    TOP_PADDING = 10
    BOTTOM_PADDING = 5
else:
    GREETING_SIZE = 32
    CLOCK_SIZE = 120
    TITLE_SIZE = 18
    TEXT_SIZE = 18
    INSTRUCTION_SIZE = 16
    TOP_PADDING = 40
    BOTTOM_PADDING = 30


window.title("TIK TOCK DOC")
window.attributes("-fullscreen", True)
window.configure(bg=BG)

window.bind("<Escape>", lambda event: window.destroy())
window.bind("<Button-1>", toggle_seconds)


# Frames
main_frame = tk.Frame(window, bg=BG)
top_frame = tk.Frame(main_frame, bg=BG)
center_frame = tk.Frame(main_frame, bg=BG)
bottom_frame = tk.Frame(main_frame, bg=BG)




# Labels

greeting_label = tk.Label(
    top_frame,
    text="",
    font=("comfortaa", GREETING_SIZE),
    fg=TEXT,
    bg=BG
)

weather_label = tk.Label(
    center_frame,
    text="",
    font=("comfortaa", TEXT_SIZE),
    fg=PINK,
    bg=BG
)

countdown_title = tk.Label(
    center_frame,
    text="Looking Forward",
    font=("comfortaa", TITLE_SIZE),
    fg=TEXT,
    bg=BG
)

countdown_label = tk.Label(
    center_frame,
    text="",
    font=("comfortaa", TEXT_SIZE),
    fg=ACCENT,
    bg=BG
)

message_label = tk.Label(
    center_frame,
    text="",
    font=("comfortaa", TEXT_SIZE),
    fg=PINK,
    bg=BG,
    wraplength=500,
    justify="center"
)

clock_label = tk.Label(
    center_frame,
    text="",
    font=("comfortaa", CLOCK_SIZE),
    fg=ACCENT,
    bg=BG
)

instruction_label = tk.Label(
    bottom_frame,
    text="Tap to hide or show seconds",
    font=("comfortaa", INSTRUCTION_SIZE),
    fg=PINK,
    bg=BG
)


# Place labels
# Pack frames
main_frame.pack(fill="both", expand=True)

top_frame.pack(
    fill="x",
    pady=(TOP_PADDING, 0)
)

center_frame.pack(
    fill="both",
    expand=True
)

bottom_frame.pack(
    fill="x",
    pady=(0, BOTTOM_PADDING)
)
# Place labels
greeting_label.pack(pady=(0, 20))
weather_label.pack(pady=10)
clock_label.pack(expand=True)
countdown_title.pack()
countdown_label.pack(pady=(0, 20))
message_label.pack(pady=20)
instruction_label.pack()


update_clock()

window.mainloop()

#hello