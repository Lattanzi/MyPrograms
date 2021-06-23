from tkinter import *
from tkinter import messagebox

tk = Tk()
tk.geometry("500x500")

def click_here():
    msg = messagebox.showinfo("Test", "Testing")

btn = Button(tk, text = "Click here", command = click_here)
btn.place(x=50, y=50)

tk.mainloop()
