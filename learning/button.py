from tkinter import *
from tkinter import messagebox

window = Tk()

window.geometry("200x200")

def displayMessage():
    messagebox.showinfo("Hello", "Red button clicked")

b1 = Button(window, text="Red", command=displayMessage, activeforeground="red", activebackground="pink", pady=10)

b1.pack(side=LEFT)

window.mainloop()