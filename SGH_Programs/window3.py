from tkinter import *
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import filedialog as fd
from ocr_test import check
import tkinter as tk
from ginger_post import main1
import os
from PIL import ImageTk,Image
import re

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

lbl = Label(window, text="Click below to Import File")
lbl.place(x=560,y=1)
def clicked():
    #file = filedialog.askopenfilename()
    filename = fd.askopenfilename()
    txt.delete("1.0", "end-1c")
    #print(filename)
    li=check(filename)
    txt.insert(tk.END,li)


def checked():
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
                txt.tag_config("red", foreground="red")
                txt2.tag_config("green", foreground="green")
                txt.insert(tk.END, str(ol[i]), "red")
                txt.insert(tk.END, " ")
                txt2.insert(tk.END, str(fl[i]), "green")
                txt2.insert(tk.END, " ")

    colorize(og, fg)


btn = Button(window, text="Import",command=clicked)
btn.place(x=600,y=35)

#lbl = Label(window, text="Click below button to convert imported file to normal Text file")
#lbl.place(x=540,y=50)
#btn = Button(window, text="Convert")
#btn.place(x=540,y=72)

lbl = Label(window, text="From Imported file:")
lbl.place(x=570,y=70)

txt = scrolledtext.ScrolledText(window,width=135, height=13,bg='black',font="Arial,bold",foreground="white",insertbackground="white")
txt.place(x=60,y=100)

#lbl = Label(window, text="Click Below button TO check error if any and to make It correct")
#lbl.place(x=540,y=365)

btn = Button(window, text="click here For Text Check",command=checked)
btn.place(x=570,y=350)

lbl = Label(window, text="corrected Text")
lbl.place(x=600,y=390)

txt2 = scrolledtext.ScrolledText(window,width=135, height=13,bg='black',font="Arial,bold",foreground="white",insertbackground="white")
txt2.place(x=60,y=420)

img1 = ImageTk.PhotoImage(Image.open(r'home2.png'))


def home():
    window.destroy()
    os.system('python primary_window.py')
btn = Button(window, text="Home", command=home, image=img1)
btn.place(x=390,y=25)


window.mainloop()