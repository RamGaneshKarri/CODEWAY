from tkinter import *
from tkinter import messagebox
ws = Tk()
ws.geometry('600x450+600+200')
ws.title('Todo-list')
ws.config(bg='aqua')
ws.resizable(width=False, height=False)
frame = Frame(ws)
frame.pack(pady=10)
ws.mainloop()