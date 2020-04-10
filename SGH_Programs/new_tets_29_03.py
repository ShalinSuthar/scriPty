import tkinter as tk
from tkinter import font as tkFont
from nltk.corpus import wordnet
from nltk.corpus import words

#https://stackoverflow.com/questions/3732605/add-advanced-features-to-a-tkinter-text-widget


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        ## Toolbar
        self.toolbar = tk.Frame()
        
        self.bold = tk.Button(name="toolbar", text="bold", 
                              borderwidth=1, command=self.OnBold,)
        self.bold.pack(in_=self.toolbar, side="left")
        

        ## Main part of the GUI
        # I'll use a frame to contain the widget and 
        # scrollbar; it looks a little nicer that way...
        text_frame = tk.Frame(borderwidth=1, relief="sunken")
        self.text = tk.Text(wrap="word", background="white", 
                            borderwidth=0, highlightthickness=0)
        self.vsb = tk.Scrollbar(orient="vertical", borderwidth=1,
                                command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(in_=text_frame,side="right", fill="y", expand=False)
        self.text.pack(in_=text_frame, side="left", fill="both", expand=True)
        self.toolbar.pack(side="top", fill="x")
        text_frame.pack(side="bottom", fill="both", expand=True)

        # clone the text widget font and use it as a basis for some
        # tags
        
        bold_font = tkFont.Font(self.text, self.text.cget("font"))
        bold_font.configure(weight="bold")
        self.text.tag_configure("bold", font=bold_font)
        
        self.text.tag_configure("misspelled", foreground="red", underline=True)
        

        # set up a binding to do simple spell check. This merely
        # checks the previous word when you type a space. For production
        # use you'll need to be a bit more intelligent about when
        # to do it.
        #self.text.bind("<space>", self.Spellcheck)

        self.text.bind("<space>", self.Spellcheck)
        self.text.bind("<.>", self.Spellcheck)
        self.text.bind("<,>", self.Spellcheck)
        self.text.bind("<?>", self.Spellcheck)
        self.text.bind("<Return>", self.Spellcheck)
        self.text.bind("<!>", self.Spellcheck)
        self.text.bind("<@>", self.Spellcheck)
        self.text.bind("<&>", self.Spellcheck)

        # initialize the spell checking dictionary. YMMV.
        #self._words=open("words.txt").read().split("\n")

    def Spellcheck(self, event):
        '''Spellcheck the word preceeding the insertion point'''
        index = self.text.search(r'\s', "insert", backwards=True, regexp=True)
        
        if index == "":
            index ="1.0"
        else:
            index = self.text.index("%s+1c" % index)
        
        word = self.text.get(index, "insert")
        '''
        if word in self._words:
            self.text.tag_remove("misspelled", index, "%s+%dc" % (index, len(word)))
        '''   
        if word in wordnet.synsets(word):
            self.text.tag_remove("misspelled", index, "%s+%dc" % (index, len(word)))
        else:
            self.text.tag_add("misspelled", index, "%s+%dc" % (index, len(word)))
        
        
        '''
        
        
        if word in words.words():
            self.text.tag_remove("misspelled", index, "%s+%dc" % (index, len(word)))
        '''
        
       
        
        

    def OnBold(self):
        #Toggle the bold state of the selected text

        # toggle the bold state based on the first character
        # in the selected range. If bold, unbold it. If not
        # bold, bold it.
        current_tags = self.text.tag_names("sel.first")
        if "bold" in current_tags:
            # first char is bold, so unbold the range
            self.text.tag_remove("bold", "sel.first", "sel.last")
        else:
            # first char is normal, so bold the whole selection
            self.text.tag_add("bold", "sel.first", "sel.last")


if __name__ == "__main__":
    app=App()
    app.mainloop()
