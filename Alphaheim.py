import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import pyjokes
import pywhatkit
import time
import wolframalpha
# my api id 568LEA-4HXR9L9AKR


#init pyttsx
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty('voices',voices[1].id)
engine.setProperty('rate',140)

def speak(audio): 
    engine.say(audio) 
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello I am your desktop voice assistant named Alphaheim")
    speak("How may I help you?")

def take_command(): 
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        print("listening...") 
        r.pause_threshold = 1
        audio = r.listen(source) 
    try: 
      print("recognizing...") 
      query = r.recognize_google(audio, language='en-in') 
      print(f"user said:{query}\n") 
    except Exception as e: 
          print(e) 
          speak("i didnt understand") 
          return "None" 
    return query

if __name__ == '__main__':
   
    wishMe()
    while True:
      query = take_command().lower()
     
      if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia",'')
            result = wikipedia.summary(query,2)
            speak("According to Wikipedia")
            speak(result)

      elif "tell me your name" in query:
            speak("I am Alphaheim. Your deskstop Assistant")

      elif 'play' in query:
        song = query.replace('play', '')
        speak('playing ' + song)
        pywhatkit.playonyt(song)

      elif 'who is' in query:
        person = query.replace('who is', '')
        info = wikipedia.summary(person, 1)
        speak(info)

      elif 'what is' in query:
        person = query.replace('what is', '')
        information = wikipedia.summary(person, 1)
        speak(information)

      elif 'open youtube' in query:
          speak("Opening Youtube")
          webbrowser.open("youtube.com")

      elif 'search'  in query:
            text = query.replace("search", "")
            webbrowser.open_new_tab(text)
            time.sleep(5)

      elif 'open whatsapp' in query:
          speak("Opening whatsapp")
          webbrowser.open("whatsapp.com")  

      elif 'open facebook' in query:
          speak("Opening facebook")
          webbrowser.open("facebook.com")  

      elif 'open gmail' in query:
          speak("gmail ")
          webbrowser.open("gmail.com")

      elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
      elif 'joke' in query:
            speak(pyjokes.get_joke())

      elif 'news' in query:
            news = webbrowser.open("https://timesofindia.indiatimes.com")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

      elif "write a note" in query:
            speak("What should i write")
            note = take_command()
            file = open('alpha.txt', 'w')
            speak("Should i include date and time")
            snfm = take_command()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
      elif "show note" in query:
            speak("Showing Notes")
            file = open("alpha.txt", "r")
            print(file.read())
            speak(file.read())

      elif "calculate" in query:
             
            app_id = "568LEA-4HXR9L9AKR"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

      
      elif 'stop' in query:
            exit(0)
