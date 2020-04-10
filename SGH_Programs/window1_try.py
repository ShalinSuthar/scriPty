from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import ttk
from tkinter import Menu
from PIL import ImageTk,Image
import pyttsx3
import re
from functools import partial
import sys
import urllib.parse
import urllib.request
from urllib.error import HTTPError
from urllib.error import URLError
import json
from ginger_post import main1
from PyDictionary import PyDictionary
from tkinter.filedialog import askopenfile,asksaveasfile
from spellchecker import SpellChecker

spell = SpellChecker()

dt=PyDictionary()




def escape_ansi(line):
    ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    return ansi_escape.sub('', line)



window = Tk()

window.title("ScriPty-Come Write")
window.geometry('1350x720')
window.config(bg='gray30')

img = ImageTk.PhotoImage(Image.open(r'write.jpg'))
img1 = ImageTk.PhotoImage(Image.open(r'home2.png'))

menubar = Menu(window)

def open_file():
    file = askopenfile(mode ='r', filetypes =[('Text Document', '.txt'),
             ('Word document','.docx')
             ])
    if file is not None:
        content = file.read()
        txt.insert(tk.END,content)

file = Menu(menubar, tearoff=0)
file.add_command(label="New")
file.add_command(label="Open",command=open_file)
'''
def save():
    files = [('Text Document', '.txt'),
             ('Word document','.docx')
             ]
    filename = asksaveasfile(mode='a+',filetypes=files, defaultextension=files)
    filename = open(filename,'w')
    sr = (txt2.get('1.0','end-1c'))
    #sr=escape_ansi(sr)
    #sr=str(sr)
    print(sr)
    filename.write(sr)
    filename.close()
'''
def save():
    window.filename =asksaveasfile(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    file=open(window.filename.name, 'w')
    file.writelines(txt2.get('1.0', tk.END))
    file.close()


file.add_command(label="Save",command=save)
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
help = Menu(menubar, tearoff=0)
help.add_command(label="About")
menubar.add_cascade(label="Help", menu=help)

window.config(menu=menubar)
line = tk.StringVar()

lbl = Label(window, image=img)
lbl.place(x=550, y=1)
txt = Text(window,width=135, height=13,insertbackground="white",font="Arial,BOLD,25",foreground="white", bg="black")
txt.place(x=60, y=75)

lbl = Label(window, text="Corrected Text",bg="Blue",fg="white")
lbl.place(x=600, y=390)

txt2 = Text(window, width=135, height=13,insertbackground="white",font="Arial,BOLD,25",foreground="white", bg="black")
txt2.place(x=60, y=420)

def clicked():
    line = txt.get("1.0","end-1c")
    li=main1(line)
    og = escape_ansi(str(li[0]))
    fg = escape_ansi(str(li[1]))

    def colorize(og, fg):
        txt.delete("1.0","end-1c")
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
                txt.insert(tk.END, str(ol[i]),"red")
                txt.insert(tk.END, " ")
                txt2.insert(tk.END, str(fl[i]),"green")
                txt2.insert(tk.END, " ")
    colorize(og,fg)


def select():
    ranges = txt2.tag_ranges(tk.SEL)
    if ranges:
        print('SELECTED Text is %r' % txt2.get(*ranges))
    else:
        print('NO Selected Text')
    word = txt2.get(*ranges)
    mean = (dt.meaning(word))
    if mean:
        messagebox.showinfo(word, mean)
    else:
        messagebox.showinfo(word, "no meaning found")



def spell_check():
    ranges = txt.tag_ranges(tk.SEL)
    if ranges:
        print('SELECTED Text is %r' % txt.get(*ranges))
    else:
        print('NO Selected Text')
    word = txt.get(*ranges)

    cor = spell.correction(word)
    candi = (spell.candidates(word))
    '''
    root=Tk()
    root.geometry('200x200')
    combo=ttk.Combobox(window,candi)
    combo.bind('<>',callfun)
    '''

    messagebox.showinfo(("correct spell: " + cor), candi)


window.bind('<Control-p>',lambda e: txt.after(20,spell_check(),e))
window.bind('<Control-m>', lambda e: txt2.after(20, select(), e))


btn = Button(window,text="Click here For Text Check",command=lambda: clicked())
btn.place(x=570, y=350)

def home():
    window.destroy()
    os.system('python primary_window.py')
btn = Button(window, text="Home", command=home,image=img1)
btn.place(x=470,y=11)


window.mainloop()
