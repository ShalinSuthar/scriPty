from tkinter import *
from tkinter import scrolledtext
from PIL import ImageTk,Image
from tkinter import Menu
import tkinter as tk
from ginger_post import main1
from voice_input_shalin import take_inp
import os
import pyaudio
def escape_ansi(line):
    ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    return ansi_escape.sub('', line)


window = Tk()

window.title("ScriPty-Come Write")
window.geometry('1350x720')
window.config(bg='gray30')

menubar = Menu(window)
file = Menu(menubar, tearoff=0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as...")
file.add_command(label="Close")

file.add_separator()

file.add_command(label="Exit", command=window.quit)

menubar.add_cascade(label="File", menu=file)
edit = Menu(menubar, tearoff=0)
edit.add_command(label="Undo")
edit.add_command(label="Redo")

edit.add_separator()

edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")
edit.add_command(label="Select All")

menubar.add_cascade(label="Edit", menu=edit)
set = Menu(menubar, tearoff=0)
set.add_command(label="About")
menubar.add_cascade(label="Set", menu=set)
window.config(menu=menubar)

img = ImageTk.PhotoImage(Image.open(r'record.jpg'))
img1 = ImageTk.PhotoImage(Image.open(r'home2.png'))


lbl = Label(window, text="Click here for voice Input")
lbl.place(x=350, y=25)


txt = scrolledtext.ScrolledText(window,width=135, height=13,bg='black',font="Arial", fg="white")
txt.place(x=60, y=95)

lbl = Label(window, text="Corrected Text")
lbl.place(x=600, y=390)

txt2 = scrolledtext.ScrolledText(window, width=135, height=13, bg='black',font="Arial", fg="white")
txt2.place(x=60, y=420)



def clicked():
    lbl = Label(window, text="Listening...")
    lbl.place(x=850, y=25)
    ip=take_inp()
    s = ""
    for i in range(0, len(ip)):
        s = s + str(ip[i])
    print(s)

    txt.insert(tk.END,s)
    txt.insert(tk.END," ")

def clicked2():
    line = txt.get("1.0", "end-1c")
    li = main1(line)
    og = escape_ansi(str(li[0]))
    fg = escape_ansi(str(li[1]))

    def colorize(og, fg):
        txt.delete("1.0", "end-1c")
        txt2.delete("1.0", "end-1c")
        ol = og.split(" ")
        fl = fg.split(" ")

        for i in range(0, len(ol)):
            if (ol[i] == fl[i]):
                # txt2-->black,txt-->black
                txt.insert(tk.END, str(ol[i]))
                txt.insert(tk.END, " ")
                txt2.insert(tk.END, str(fl[i]))
                txt2.insert(tk.END, " ")

            else:
                # txt2-->green,txt-->red
                txt.tag_config("red", foreground="deep pink")
                txt2.tag_config("green", foreground="olivedrab1")
                txt.insert(tk.END, str(ol[i]), "red")
                txt.insert(tk.END, " ")
                txt2.insert(tk.END, str(fl[i]), "green")
                txt2.insert(tk.END, " ")

    colorize(og, fg)


btn = Button(window,command=clicked,image=img,compound='left', border=0,bg='royalblue2')
btn.place(x=540, y=1)

btn2 = Button(window, text="Click here For Text Check")
btn2.place(x=570, y=350)

def clicked():
    window.destroy()
    os.system('python primary_window.py')
btn = Button(window, text="Home", command=clicked, image=img1)
btn.place(x=270,y=25)


window.mainloop()
