import tkinter as tk
from datetime import datetime
from weather import get_weather
from countdown import get_next_event
from messages import get_daily_message

USER_NAME = "Layla Coletti"
SHOW_SECONDS = True

# Coffee Shop Theme
BG = "#000000"          # 
TEXT = "#473367"        # 
ACCENT = "#92be46"      # 
PINK = "#fb7462"


def toggle_seconds(event):
    global SHOW_SECONDS
    SHOW_SECONDS = not SHOW_SECONDS


def update_clock():
    now = datetime.now()
    hour = now.hour

    weather = get_weather()
    event = get_next_event()
    print("EVENT:", event)
    message = get_daily_message()

    # Greeting
    if 4 <= hour < 12:
        greeting = f"Good Morning, {USER_NAME}! "
    elif 12 <= hour < 16:
        greeting = f"Good Afternoon, {USER_NAME}! "
    elif 16 <= hour < 21:
        greeting = f"Good Evening, {USER_NAME}! "
    else:
        greeting = f"Good Night, {USER_NAME}! "

    # Clock
    if SHOW_SECONDS:
        current_time = now.strftime("%I:%M:%S %p")
    else:
        current_time = now.strftime("%I:%M %p")

    greeting_label.config(text=greeting)

    weather_label.config(
        text=f'{weather["temperature"]}\n{weather["condition"]}'
    )

    # Countdown
    countdown_text = f'{event["name"]}\n{event["days"]}'

    countdown_label.config(
        text=countdown_text
    )
    
    message_label.config(text=message)
    clock_label.config(text=current_time)

    window.after(1000, update_clock)


window = tk.Tk()

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

main_frame.pack(fill="both", expand=True)

top_frame.pack(fill="x", pady=(40, 0))
center_frame.pack(fill="both", expand=True)
bottom_frame.pack(fill="x", pady=(0, 30))

# Greeting
greeting_label = tk.Label(
    top_frame,
    text="",
    font=("Arial Rounded MT Bold", 32),
    fg=TEXT,
    bg=BG
)

# Weather
weather_label = tk.Label(
    center_frame,
    text="",
    font=("Arial Rounded MT Bold", 18),
    fg=TEXT,
    bg=BG
)

# Countdown
countdown_title = tk.Label(
    center_frame,
    text="Looking Forward",
    font=("Arial Rounded MT Bold", 18),
    fg=TEXT,
    bg=BG
)

countdown_label = tk.Label(
    center_frame,
    text="",
    font=("Arial Rounded MT Bold", 20),
    fg=ACCENT,
    bg=BG
)

# Daily Message
message_label = tk.Label(
    center_frame,
    text="",
    font=("Arial Rounded MT Bold", 18),
    fg=PINK,
    bg=BG,
    wraplength=500,
    justify="center"
)

# Clock
clock_label = tk.Label(
    center_frame,
    text="",
    font=("Arial Rounded MT Bold", 120),
    fg=ACCENT,
    bg=BG
)

# Instructions
instruction_label = tk.Label(
    bottom_frame,
    text="Tap to hide or show seconds",
    font=("Arial Rounded MT Bold", 16),
    fg=PINK,
    bg=BG
)

# Pack everything
greeting_label.pack(pady=(0, 20))
weather_label.pack(pady=10)
clock_label.pack(expand=True)
countdown_title.pack()
countdown_label.pack(pady=(0, 20))
message_label.pack(pady=20)
instruction_label.pack()

update_clock()

window.mainloop()


#:)