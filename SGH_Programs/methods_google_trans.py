from googletrans import Translator,LANGUAGES

class Mytranslator:
    def __init__(self):
        self.langs=list(LANGUAGES.values())
    def run(self,txt="type text here",src="english",dest="hindi"):
        self.ts=Translator()
        self.txt=txt
        self.src=src
        self.dest=dest
        try:
            self.translated=self.ts.translate(self.txt,src=self.src,dest=self.dest)
        except:
            self.translated=self.ts.translate(self.txt)
        self.ttext=self.translated.text

        return self.ttext
        
