import tkinter as tk 
from datetime import datetime


window = tk.Tk()
window.title("TIK TOCK DOC")
window.attributes("-fullscreen", True)
window.configure(bg="Cornsilk")
window.bind("<Escape>", lambda event: window.destroy())


def update_clock():
    current_time = datetime.now().strftime("%I:%M:%S %p")
    clock_label.config(text=current_time)
    window.after(1000, update_clock)



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

