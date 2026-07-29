import tkinter as tk 


from datetime import datetime

window = tk.Tk()

window.title("Desk Companion")


current_time = datetime.now().strtime("%I:%M %p")


clock_lable = tk.Lable(window, text=current_time)

clock_lable.pack(padx=40, pady=40)


window.mainloop()
