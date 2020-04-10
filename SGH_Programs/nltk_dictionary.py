from nltk.corpus import wordnet as wn
#res=wn.synset('pond.n.01').lemma_names()
#ex=wn.synset('pond.n.01').examples()
#op=wn.lemma("good.a.01.good").antonyms()


def give_syn(word):
    word_in=word+".n.01"
    try:
        res=wn.synset(word_in).lemma_names()
        res=str(res)
        return res
    except:
        return "No synonym found."
    #print(word+"------>synonymes: "+str(res))

def give_examples(word):
    word_in=word+".n.01"
    try:
        ex=wn.synset(word_in).examples()
        return ex
    except:
        return "No example found."


def give_opposite(word):
    word_in=word+".a.01."+word
    try:
        opp=wn.lemma(word_in).antonyms()
        k = opp
        m = str(k[0]).split(".")
        l = m[0]
        l=l[7:]
        return l
    except:
        return "No opposite found."

