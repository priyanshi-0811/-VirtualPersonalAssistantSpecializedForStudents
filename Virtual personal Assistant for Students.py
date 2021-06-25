#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pyttsx3')


# In[13]:


get_ipython().system('pip install speechRecognition')


# In[11]:


conda install -c anaconda pyaudio


# In[2]:


get_ipython().system('pip install numpy')


# In[3]:


get_ipython().system('pip install wikipedia')


# In[14]:


get_ipython().system('pip install pipwin')


# In[15]:


get_ipython().system('pipwin install pyaudio')


# In[5]:


import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr
import pyaudio
import time


engine = pyttsx3.init('sapi5', debug=False)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def wishMe():
  hour = int (datetime.datetime.now().hour)
  if hour >= 0 and hour < 12:
    speak("Good Morning!")
  elif hour >= 12 and hour < 16:
    speak("Good Afternoon!")
  else:
    speak("Good Evening!")
  speak("I am your Personal Assistant. Please tell me how may I help you")

def takeCommand():
  r= sr.Recognizer()
  with sr.Microphone() as source:
    print("listening...")
    r.pause_threshold = 1
    audio = r.listen(source)
  try: 
    print("Recognizing...")
    query = r.recognize_google(audio, language='en-in')
    print(f"User said: {query}\n")

  except Exception as e:
    print("say that again please....")
    speak("say that again please....")
    return "None"


  return query



if __name__ == "__main__":
    
    wishMe()
    
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            print("According to Wikipedia, ")
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            print("opening youtube")
            speak("opening youtube")
            webbrowser.open("www.youtube.com")
            
        elif 'play music' in query:
            print("opening spotify")
            speak("opening spotify")
            webbrowser.open("www.spotify.com")
        
        elif 'open vedantu' in query:
            print("opening vedantu")
            speak("opening vedantu")
            webbrowser.open("www.vedantu.com")
        
        elif 'open quora' in query:
            print("opening quora")
            speak("opening quora")
            webbrowser.open("www.quora.com")
        
        elif 'open codechef' in query:
            print("opening codechef")
            speak("opening codechef")
            webbrowser.open("www.codechef.com")
            
        elif 'search meditation videos' in query:
            print("searching meditation videos ")
            speak("searching meditation videos")
            webbrowser.open("https://www.youtube.com/results?search_query=mediation+for+peace+of+mind")
        
        elif 'search for best schools nearby' in query:
            print("searching best schools nearby")
            speak("searching best schools nearby")
            webbrowser.open("https://www.google.com/search?sxsrf=ALeKk01xep8YKenb8u3818gnHFjDgqhXVg:1611912113682&q=best+school+near+me&sa=X&ved=2ahUKEwiXnMfH6MDuAhUayzgGHRZDBpgQ7xYoAHoECAQQMA&biw=1366&bih=625")
        
        elif 'what time is it' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is {strTime}")
            print((f"Mam, the time is {strTime}"))
            
        elif 'how are you' in query:
            print("I am fine, Thank you")
            print("How are you, Mam")
            speak("I am fine, Thank you")
            speak("How are you, Mam")
            
        elif 'fine' in query or "mast" in query:
            print("It's good to know that your fine")
            speak("It's good to know that your fine")
            
        elif "who made you" in query or "who created you" in query:
            print("I have been created by you priyanshi, ananya and neha.")
            speak("I have been created by you priyanshi, ananya and neha.")
            
        elif "who i am" in query or "main kaun hun" in query:
            speak("If you talk then definitely your human.")
            print("If you talk then definitely your human.")
            
        elif "good morning" in query:
            print("A warm" + query)
            speak("A warm" + query)
            print("How are you Mam")
            speak("How are you Mam")
            
        elif "good afternoon" in query:
            print(query + "Mam")
            speak(query + "Mam")
            print("How are you Mam")
            speak("How are you Mam")
            
        elif " good evening" in query:
            print(query + "Mam")
            speak(query + "Mam")
            print("How are you Mam")
            speak("How are you Mam")
            
        elif "good night" in query:
            print(query + "Mam")
            speak(query + "Mam")
            print("Have a good sleep")
            speak("Have a good sleep")
       
            
        elif "bore" in query or "feeling bored" in query:
            print("Alright, I can tell you a joke then")
            speak("Alright, I can tell you a joke then")

        
        elif "write a note" in query:
            print("What should i write, mam")
            speak("What should i write, mam")
            note = takeCommand()
            file = open('data.txt', 'w')
            print("Mam, Should i include date and time")
            speak("Mam, Should i include date and time")
            snfm = takeCommand()
            
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
            
        elif "show note" in query or "show notes" in query or "show me my notes" in query:
            speak("Showing Notes")
            file = open("data.txt", "r")
            print(file.read())
            speak(file.read(6))
            
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop Me from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
            
        elif 'tell me about yourself' in query:
            print("Hello,I am your virtual personal assistant, i have been specially created for helping students. I was made as a mini project by three students of ABES Engineering College CE branch second year, Ananya Neha Priyanshi. Thank you")
            speak("Hello,I am your virtual personal assistant, i have been specially created for helping students. I was made as a mini project by three students of ABES Engineering College CE branch second year, Ananya Neha Priyanshi. Thank you")
        
        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            print('okay Bye, Have a good day.')
            speak('okay, Bye, have a good day.')
            takeCommand.exit()
        
            
            


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




