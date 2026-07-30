import tkinter as tk 


from datetime import datetime

window = tk.Tk()

window.title("TIK TOCK DOC")


current_time = datetime.now().strftime("%I:%M %p")


clock_label = tk.Label(window, text=current_time)

clock_label.pack(padx=40, pady=40)


window.mainloop()
