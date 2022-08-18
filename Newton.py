import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia


engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    time = int (datetime.datetime.now().hour)
    if time >= 0 and time < 12:
        speak("Good Morning!")
    elif time >= 12 and time <18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Newton Sir. Please tell me how may i help you.")

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as mp:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(mp)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-US")
        print("User said: {0}".format(query))
    except:
        print("Say that again please!")
        return "None"
    return query

if __name__ == "__main__":
    # speak("Hello! i am Newton.")
    fool = "fool is an angry girl, named as Areeba Fatima. bohat ee dheeett. or zidddi larkki hay."
    wishMe()
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:

            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
        if ("Areeba" in query or "ariba" in query or "reba" in query) and "who" in query:
            speak("Oh! you mean fool?")
            speak(fool)