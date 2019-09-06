import tkinter as tk

from Tool import *

InputWindow = tk.Tk()
InputWindow.geometry('500x200')
InputWindow.title('Input')
InputWindow.configure(bg='black')

EntryLocal = tk.Entry(InputWindow, bg='yellow', fg='black')
EntryLocal.place(x=80, y=40)

string = tk.StringVar()
string.set('<-input local ip here')
LocalLabel = tk.Label(InputWindow, textvariable=string
                      , bg='black', fg='yellow',
                      font=('Arial', 12))
LocalLabel.place(x=300, y=40)

EntryCloud = tk.Entry(InputWindow, bg='yellow', fg='black')
EntryCloud.place(x=300, y=80)

string_2 = tk.StringVar()
string_2.set('input cloud ip here->')
CloudLabel = tk.Label(InputWindow, textvariable=string_2
                      , bg='black', fg='yellow',
                      font=('Arial', 12))
CloudLabel.place(x=80, y=80)


def my_exit():
    error_log.close()
    exit()


def confirm():
    global Local_ip, Cloud_ip
    Local_ip = EntryLocal.get()
    Cloud_ip = EntryCloud.get()
    InputWindow.destroy()
    return


ConfirmButton = tk.Button(InputWindow, text='Confirm', bg='yellow', font=('Arial', 14), command=confirm, width=10,
                          height=1)
ConfirmButton.place(x=90, y=120)

ExitButton = tk.Button(InputWindow, text='Exit', bg='yellow', font=('Arial', 14), command=my_exit, width=10,
                       height=1)
ExitButton.place(x=310, y=120)
InputWindow.mainloop()
# TODO:Finish the button
