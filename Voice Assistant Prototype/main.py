import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import pyaudio

#Different Voices
id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

#hear the mic and return audio as text
def transform_audio_into_text():

    #store recognizer in variable
    r = sr.Recognizer()
    #set microphone
    with sr.Microphone() as source:

        #waiting time
        r.pause_threshold = 0.8

        #report that recording started
        print("You can now speak")

        #Save what you hear as audio
        audio = r.listen(source)

        try:
            #search on google what's heard
            request = r.recognize_google(audio, language = "en-gb")

            #test in text
            print("You said " + request)


            return request

        # In case it doesn't understand audio
        except sr.UnknownValueError:
            #proof that it didnt understand the audio
            print("Oops I did not get that")

            return "I'm still waiting"

        #Incase request cannot be resolved
        except sr.RequestError:

            #Show proof that it didnt understand audio
            print("OOps! I didnt understand audio")
            return "I'm still waiting"



        # Unexpected error
        except :
            #proof that it didnt understand the audio
            print("Oops I did not get that")

            return "I'm still waiting"
        #Incase request cannot be resolved

#Function so the assistant can be heard
def speak(message):

    #start engine of pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("voice", id2)

    #deliver message
    engine.say(message)
    engine.runAndWait()
#Inform day of the week
def ask_day():

    #Create a variable with today information
    day = datetime.datetime.today()
    print(day)

    #Create variable for day of the week
    week_day = day.weekday()
    print(week_day)

    #Name of days to pronounce
    calender = {0: "Monday",
                1: "Tuesday",
                2: "Wednesday",
                3: "Thursday",
                4: "NihadBitch",
                5: "Saturday",
                6: "Sunday"}

    # Say the day of the week
    speak(f"Today is {calender[week_day]}")



#Inform what time it is
def ask_time():

    #Variable with time info
    time = datetime.datetime.now()
    time = f"At this moment it is {time.hour} hours and {time.minute} minutes"
    print(time)

    #Say the time
    speak(time)

#Create initial greeting
def initial_greeting():

    #Say greeting
    speak("Hello I am your personal assistant Zaman. How can I help you?")

#Main function of the assistant
def my_assistant():
    #Activate the initial greeting
    initial_greeting()

    #Cut-off variable
    go_on = True

    #Main loop
    while go_on:
        #Activate microphone and save request
        my_request = transform_audio_into_text().lower()

        if  "open youtube" in my_request:
            speak("Sure, I am opening youtube")
            webbrowser.open("https://www.youtube.com")
            continue
        elif "open browser" in my_request:
            speak("Of course, I am on it")
            webbrowser.open("https://www.google.com")
            continue
        elif "what day is today" in my_request:
            ask_day()
            continue
        elif "what time it is " in my_request:
            ask_time()
            continue
        elif "wikipedia search" in my_request:
            speak("Say less")
            my_request = my_request.replace("wikipedia search","")
            answer = wikipedia.summary(my_request, sentences = 1)
            speak("According to wikipedia")
            speak(answer)
            continue
        elif "search the internet for" in my_request:
            speak("of course, right now")
            my_request = my_request.replace("search the internet for", "")
            pywhatkit.search(my_request)
            speak("this is what I found")
            continue
        elif "play" in my_request:
            speak("Playing it right now")
            pywhatkit.playonyt(my_request)
            continue
        elif "joke" in my_request:
            speak(pyjokes.get_joke())
            continue
        elif "stock price" in my_request:
            share = my_request.split()[-2].strip()
            portfolio = {"Apple": "APPL",
                         "amazon": "AMZN",
                         "google": "GOOGL"}
            try:
                searched_stock =  portfolio[share]
                searched_stock = yf.Ticker(searched_stock)
                price = searched_stock.info["regularMarketPrice"]
                speak(f" I found it! The price of {share} is {price}")
                continue
            except:
                speak("I am sorry but I didn't find it")
                continue
        elif "goodbye" in my_request:
            speak("I am going to rest master. Let me know if you need any serving")
            break


my_assistant()