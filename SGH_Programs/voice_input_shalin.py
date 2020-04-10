import speech_recognition as sr
import pyttsx3,pyaudio
engine = pyttsx3.init()
voices = engine.getProperty('voices')

def speak(audio):
    engine.setProperty('voice', voices[len(voices) - 1].id)
    engine.say(audio)
    engine.runAndWait()


def myCommand():
    query=""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')


    except sr.UnknownValueError:
        speak("Sorry, I did not get it, please try again!!!")
        print("I couldn't get it.")
        #pass

    return query

inp=[]
def take_inp():
    print("listening: ")
    speak("listening")

    query = myCommand()
    if(query=="terminate" or query=="stop" or query=="abort"):
        exit(0)
    elif(query=="fullstop" or query=="dot"):
        query="."
    elif(query=="comma" or query=="coma"):
        query=","
    elif(query=="question mark"):
        query="?"
    inp.append(query)

    print(query)
    
    return inp
'''
ip=take_inp()
s=""
for i in range(0,len(ip)):
    s=s+str(ip[i])
print(s)
'''
    
