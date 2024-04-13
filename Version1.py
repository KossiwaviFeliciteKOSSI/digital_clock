from tkinter import Label, Tk
import time
windows = Tk()
windows.title("My  digital clock")
windows.geometry("390x150")
windows.resizable(0, 0)
text_font = ("Arial", 68, "bold")
background = "#FF64C4"
foreground = "#363529"
border_width = 25
label = Label(windows, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)
def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)
digital_clock()
windows.mainloop()
