import tkinter as tk

from Tool import *

InputWindow = tk.Tk()
InputWindow.geometry('200x500')
InputWindow.title('Input')
InputWindow.configure(bg='#0084ff')
EntryLocal = tk.Entry(InputWindow, bg='#e42bff')
EntryCloud = tk.Entry(InputWindow, bg='#e43bff')


def my_exit():
    error_log.close()
    exit()


def confirm():
    global Local_ip, Cloud_ip
    Local_ip = EntryLocal.get()
    Cloud_ip = EntryCloud.get()
    return
