from tkinter import *
from PIL import ImageTk,Image
from nltk_dictionary import give_examples,give_syn,give_opposite
import os
from tkinter import Menu,ttk
from tkinter import scrolledtext
from methods_google_trans import Mytranslator
window = Tk()
import tkinter as tk
window.title("Dictionary")
window.geometry('1350x720')
window.config(bg='black')

#img = ImageTk.PhotoImage(Image.open(r'index.png'))
lbl=Label(window,height=40,width=70)
lbl.place(x=80,y=50)

lbl3=Label(window,text="Dictonary",width=22)
lbl3.place(x=220,y=90)

lbl3=Label(window,text="Enter the word here",width=22)
lbl3.place(x=220,y=210)

#lbl2=Label(window,height=160,width=200,bg="white")
#lbl2.place(x=60,y=300)
ent=Text(window,width=20,height=1)
ent.place(x=220,y=240)

#lbl4=Label(window,height=75,width=140,bg="gray")
#lbl4.place(x=360,y=1)

#lb5=Label(window, text="Synonyms",bg="black",fg="white")
#lb5.place(x=500,y=20)
#lb6=Label(window, text="Antonyms",bg="black",fg="white")
#lb6.place(x=800,y=20)
#lb7=Label(window, text="Examples",bg="black",fg="white")
#lb7.place(x=1100,y=20)

t1=Text(window,width=50,height=1, bg='gray85')
t1.place(x=120,y=390)
t2=Text(window,width=50,height=1, bg='gray85')
t2.place(x=120,y=470)
t3=Text(window,width=50,height=1, bg='gray85')
t3.place(x=120,y=550)

def clicked():
    word=StringVar()
    t1.delete("1.0", "end-1c")
    word=ent.get("1.0",'end-1c')
    s=give_syn(word)
    t1.insert(END,s)
def clicked1():
    word=StringVar()
    t2.delete("1.0", "end-1c")
    word=ent.get("1.0","end-1c")
    s=give_opposite(word)
    t2.insert(END,s)
def clicked2():
    word=StringVar()
    t3.delete("1.0","end-1c")
    word=ent.get("1.0","end-1c")
    s=str(give_examples(word))
    t3.insert(END,s)

bt1=Button(window,text="Click to Get synonyms",bg="gray",fg="black",command=lambda:clicked())
bt1.place(x=250,y=350)
bt2=Button(window,text="Click to Get opposites",bg="gray",fg="black",command=lambda:clicked1())
bt2.place(x=250,y=430)
bt3=Button(window,text="Click to Get examples",bg="gray",fg="black",command=lambda :clicked2())
bt3.place(x=250,y=510)

lbl10=Label(window,height=40,width=70)
lbl10.place(x=800,y=50)

lbl3=Label(window,text="Translator",width=22)
lbl3.place(x=940,y=90)

lbl3=Label(window,text="Enter the Text to Translate",width=22)
lbl3.place(x=940,y=210)

txt = scrolledtext.ScrolledText(window, width=35, height=5, bg='gray85',font="Arial", fg="black")
txt.place(x=890, y=260)

lbl3=Label(window,text="Source")
lbl3.place(x=890,y=370)
options =[
    "English",
    "Gujarati",
    "Hindi"
]
variable = StringVar(window)
variable.set(options[0])
sl = ttk.Combobox(window,values=options)
sl.set("English")
sl.place(x=880, y=390)



lbl3=Label(window,text="Destination")
lbl3.place(x=1125,y=370)
variable1 = StringVar(window)
variable1.set(options[0])
tl = ttk.Combobox(window,values=options,width=10)
tl.set("Hindi")
tl.place(x=1125, y=390)

def get():
    s=sl.get()
    t=tl.get()
    message=txt.get('1.0',tk.END)
    translator=Mytranslator()
    text=translator.run(txt=message,src=s,dest=t)
    txt2.delete('1.0',tk.END)
    txt2.insert(tk.END,text)

btn = Button(window, text="Translate",width=10,command=get)
btn.place(x=1020, y=380)

    


lbl3=Label(window,text="Translated Text",width=22)
lbl3.place(x=970,y=430)
txt2 = scrolledtext.ScrolledText(window, width=35, height=5, bg='gray85',font="Arial", fg="black")
txt2.place(x=890, y=460)

img1 = ImageTk.PhotoImage(Image.open(r'home2.png'))

def home():
    os.system('python primary_window.py')
    window.destroy()
btn = Button(window, text="Home", command=home, image=img1)
btn.place(x=670,y=15)

window.mainloop()
