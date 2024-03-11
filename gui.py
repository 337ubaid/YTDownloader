import tkinter as tk

windows = tk.Tk()
windows.geometry('200x100')

number = 0

def addNumbers():
    global number 
    number += 1
    print(number)

button_add = tk.Button(windows, 
                   text='Click me!',
                   command=addNumbers)
button_add.pack()

windows.mainloop()