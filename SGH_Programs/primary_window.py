from tkinter import *
from PIL import ImageTk,Image
import os
from tkinter import Menu

class Widget:
    def __init__(self):
        root = Tk()
        root.title('scriPty')
        root.config(background='black')

        menubar = Menu(root)
        file = Menu(menubar, tearoff=0)
        file.add_command(label="New")
        file.add_command(label="Open")
        file.add_command(label="Save")
        file.add_command(label="Save as...")
        file.add_command(label="Close")

        file.add_separator()

        file.add_command(label="Exit", command=root.quit)

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

        root.config(menu=menubar)

        root.geometry('1350x720')

        root.iconbitmap(r'icn.ico')
        img = ImageTk.PhotoImage(Image.open(r'logo5.png'))
        img2 = ImageTk.PhotoImage(Image.open(r'txt.png'))
        img3 = ImageTk.PhotoImage(Image.open(r'stt.png'))
        img4 = ImageTk.PhotoImage(Image.open(r'ocr.png'))
        img5 = ImageTk.PhotoImage(Image.open(r'image (1).png'))


        panel = Label(root, image=img, bg='black')
        panel.pack(side="top", fill='both', expand="yes")


        panel.place(x=550, y=10)


        self.compText = StringVar()
        self.userText = StringVar()

        def clicked():
            root.destroy()
            os.system('python window1_try.py')
        btn1 = Button(text='click here for Normal text check!',image=img2,command=clicked, font=('Black ops one', 10, 'bold'),
                      bg='black', fg='white', border=0,compound='top')
        btn1.pack(fill='both', expand='no', side='left')

        def tts():
            root.destroy()
            os.system('python window2.py')
        btn2 = Button(text='click here for Speech to Text!',image=img3,command=tts, font=('Black ops one', 10, 'bold'), bg='black',
                      fg='white', border=0, compound='top')
        btn2.pack(fill='both', expand='no', side='right')

        def ocr():
            root.destroy()
            os.system('python window3.py')
        btn3 = Button(text='click here for OCR text check!',image=img4,command=ocr, font=('Black ops one', 10, 'bold'), bg='black',
                      fg='white',border=0, compound='top')
        btn3.pack(fill='both', expand='no', side='right')

        def Dict():
            root.destroy()
            os.system('python dictonary_gui_window4.py')
        btn4 = Button(text='click here for Dictonary and Translation!',image=img5, command=Dict, font=('Black ops one', 10, 'bold'), bg='black',
                      fg='white',border=0, compound='top')
        btn4.pack(fill='both', expand='no', side='right')

        btn1.place(x=80, y=280)
        btn2.place(x=400, y=280)
        btn3.place(x=750, y=280)
        btn4.place(x=1080, y=280)
        root.mainloop()
widget = Widget()