import tkinter as tk 
from datetime import datetime

USER_NAME = "Layla Coletti"


window = tk.Tk()
window.title("TIK TOCK DOC")
window.attributes("-fullscreen", True)
window.configure(bg="Cornsilk")
window.bind("<Escape>", lambda event: window.destroy())


def update_clock():
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = f"Good morning, {USER_NAME}!"
    elif current_hour < 18:
        greeting = f"Good afternoon, {USER_NAME}!" 
    else:
        greeting = f"Good evening, {USER_NAME}!"
    current_time = datetime.now().strftime("%I:%M:%S %p")
    clock_label.config(text=current_time)
    window.after(1000, update_clock)
    greeting_label.config(text=greeting)
    greeting_label.pack(pady=(40,10))

greeting_label = tk.Label(
        window,
        text="",
        font=("Ariel", 50),
        fg="Dark Green",
        bg="Cornsilk"
    )
clock_label = tk.Label(
    window, 
    text="",
     font=("Ariel", 200),
     fg="Dark Green",
     bg="Cornsilk"
     )


clock_label.pack(expand=True)

update_clock()

window.mainloop()

