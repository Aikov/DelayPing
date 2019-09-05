import tkinter as tk

from Tool import *

InputWindow = tk.Tk()
InputWindow.geometry('500x200')
InputWindow.title('Input')
InputWindow.configure(bg='#0084ff')
EntryLocal = tk.Entry(InputWindow, bg='#e42bff')
EntryLocal.place(x=60, y=40)
string = tk.StringVar()
string.set('<-input local ip here')
LocalLabel = tk.Label(InputWindow, textvariable=string
                      , bg='#0084ff', fg='black',
                      font=('Arial', 12))
LocalLabel.place(x=240, y=40)

EntryCloud = tk.Entry(InputWindow, bg='#e43bff')
InputWindow.mainloop()


def my_exit():
    error_log.close()
    exit()


def confirm():
    global Local_ip, Cloud_ip
    Local_ip = EntryLocal.get()
    Cloud_ip = EntryCloud.get()
    return
