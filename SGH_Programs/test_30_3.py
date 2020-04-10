from tkinter import *
import tkinter as tk
from tkinter import messagebox
from nltk.corpus import wordnet
from nltk.corpus import words
from spellchecker import SpellChecker
import pyautogui
    
#http://www.bitforestinfo.com/2017/05/how-to-create-find-findall-replace-and-replaceall-function-in-tkinter-text-widget-python-magicstick-text-editor.html

spell = SpellChecker()
window=Tk()
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry('%dx%d+0+0' % (width,height))

text=Text(window,bg="grey25",insertbackground="white",foreground="white",font=('Arial',45))
text.pack(side=TOP,fill=BOTH,expand=True,ipady=5)
text.tag_configure("misspelled", foreground="red", underline=True)

def Spellcheck(event):
        '''Spellcheck the word preceeding the insertion point'''
        index = text.search(r'\s', "insert", backwards=True, regexp=True)
        
        if index == "":
            index ="1.0"
        else:
            index = text.index("%s+1c" % index)
        
        word = text.get(index, "insert")

        if (word in wordnet.synsets(word)) or (word in words.words() or word=="." or word=="?" or word=="&" or ("." in word) or ("?" in word) or ("\'" in word) or ("\"" in word)):
            text.tag_remove("misspelled", index, "%s+%dc" % (index, len(word)))
        else:
            text.tag_add("misspelled", index, "%s+%dc" % (index, len(word)))

def spell_check():
    ranges = text.tag_ranges(tk.SEL)
    rag=str(ranges)
    first=text.index("sel.first")
    last=text.index("sel.last")
    print(first+" "+last)
    x, y = pyautogui.position()
    print(x,y)

    if ranges:
        print('SELECTED Text is %r' % text.get(*ranges))
    else:
        print('NO Selected Text')
    word = text.get(*ranges)

    cor = spell.correction(word)
    candi = (spell.candidates(word))
    OPTIONS=list(candi)
    lenth=len(OPTIONS)
    
    def func(value):
        line=str(text.get('1.0','end-1c'))
        #text.delete('1.0','end-1c')
        #text.insert('end-1c',line.replace(word,value,1))
        text.delete(str(first),str(last))
        text.insert(str(first),value)
        
            
    frame = Frame(window)
    #frame.config(font=('Arial',20))
    frame.place(x=x,y=y)
    variable = StringVar(frame)
    
    variable.set(word)
    w = OptionMenu(frame, variable, *OPTIONS,command=func)    
    w.pack(side=TOP,fill=BOTH,expand=True,ipady=5)
    w.config(bg="cyan",fg="BLACK",font=('Arial',20))
    w["menu"].config(bg="Blue",fg="white",font=('Arial',20))
    
    def close():
            frame.place_forget()
            
    #btn=Button(frame,text="Close",command=close,bg="Red",fg="white")
    #btn.pack(side=BOTTOM,fill=BOTH,expand=True,ipady=0)
    window.bind('<Button-1>',lambda e: text.after(20,close(),e))

    
        
        

window.bind('<Shift_L>',lambda e: text.after(20,spell_check(),e))


        

text.bind("<space>",Spellcheck)
text.bind("<.>", Spellcheck)
text.bind("<,>", Spellcheck)
text.bind("<?>", Spellcheck)
text.bind("<Return>", Spellcheck)
text.bind("<!>", Spellcheck)
text.bind("<@>", Spellcheck)
text.bind("<&>", Spellcheck)


window.mainloop()

