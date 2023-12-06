from tkinter import *

window = Tk()

# pack()
# red_button = Button(window, text = "Red", fg = "red")
# red_button.pack(side=LEFT)

# grid()
# name = Label(window, text="Name").grid(row=0, column=0)
# e1 = Entry(window).grid(row=0, column=1)

# password = Label(window, text="Password").grid(row=1, column=0)
# e2 = Entry(window).grid(row=1, column=1)

# submit = Button(window, text="Submit").grid(row=2, column=0)

window.geometry("400x250")
name = Label(window, text="Name").place(x=30, y=50)
password = Label(window, text="Email").place(x=30, y=75)
email = Label(window, text="Password").place(x=30, y=100)

e1 = Entry(window).place(x = 95, y = 50)  
e2 = Entry(window).place(x = 95, y = 75)  
e3 = Entry(window).place(x = 95, y = 100)  



window.mainloop()