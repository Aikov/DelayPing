import time
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
LocalLabel = tk.Label(InputWindow, textvariable=string,
                      bg='black', fg='yellow',
                      font=('Arial', 12))
LocalLabel.place(x=300, y=40)

EntryCloud = tk.Entry(InputWindow, bg='yellow', fg='black')
EntryCloud.place(x=300, y=80)

string_2 = tk.StringVar()
string_2.set('input cloud ip here->')
CloudLabel = tk.Label(InputWindow, textvariable=string_2,
                      bg='black', fg='yellow',
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

Window = tk.Tk()
Window.configure(bg='black')
Window.geometry('500x200')
Window.title('Main')
string = tk.StringVar()
string_2 = tk.StringVar()
string_3 = tk.StringVar()


def calc():
    global Local_ip, Cloud_ip
    body = ping_result(Local_ip)
    delay1 = ''
    delay2 = ''
    if body[0]:
        delay1 = body[1]
        body = ping_result(Cloud_ip)
        if body[0]:
            delay2 = body[1]
        else:
            string_2.set('Error')
            time.sleep(5)
            my_exit()
    else:
        string.set('Error')
        time.sleep(5)
        my_exit()
    delta_delay = float(delay2) - float(delay1)
    if delta_delay < 0:
        pass
    else:
        string.set('Local Delay ' + delay1 + 'ms')
        string_2.set('Cloud Delay ' + delay2 + 'ms')
        string_3.set('Delta Delay ' + '%.2f' % delta_delay + 'ms')
    Window.after(1000, calc, )


def update():
    global Window
    while True:
        calc()


calc()
LocalLabel = tk.Label(master=Window, textvariable=string, bg='yellow', font=('Arial', 12), fg='black')
LocalLabel.place(x=100, y=30)
CloudLabel = tk.Label(master=Window, textvariable=string_2, bg='yellow', font=('Arial', 12), fg='black')
CloudLabel.place(x=150, y=60)
DeltaLabel = tk.Label(master=Window, textvariable=string_3, bg='yellow', font=('Arial', 12), fg='black')
DeltaLabel.place(x=200, y=90)
ExitButton = tk.Button(Window, text='Exit', bg='yellow', font=('Arial', 14), command=my_exit, width=10,
                       height=1)
ExitButton.place(x=310, y=120)
UpdateButton = tk.Button(Window, text='Update', bg='yellow', font=('Arial', 14), command=calc, width=10,
                         height=1)
UpdateButton.place(x=90, y=120)

Window.mainloop()
