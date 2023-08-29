import os
import speech_recognition as sr
import win32com.client
import webbrowser
import openai
import datetime
from config import apikey
import random
import numpy as np

speaker = win32com.client.Dispatch("SAPI.SpVoice")
# s = ("Heyyy Deep")
# speaker.speak(s)

# def say(text):
#     os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  1.1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred!"

# chatStr = ""
# def chat(query):
#     global chatStr
#     print(chatStr)
#     openai.api_key = apikey
#     chatStr += f"Harry: {query}\n Jarvis: "
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt= chatStr,
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     say(response["choices"][0]["text"])
#     chatStr += f"{response['choices'][0]['text']}\n"
#     return response["choices"][0]["text"]

# def ai(prompt):
#     openai.api_key = apikey
#     text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=prompt,
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )

#     text += response["choices"][0]["text"]
#     if not os.path.exists("Openai"):
#         os.mkdir("Openai")

#     with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
#         f.write(text)


# if __name__ == '__main__':
while True:
    print("Listening...")
    s = "please try again"
    query = takeCommand()

    if "open youtube".lower() in query.lower():
            s = ("Opening youtube")
            speaker.speak(s)
            webbrowser.open("https://www.youtube.com")
            break
    # sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
    # for site in sites:
    #     if f"Open {site[0]}".lower() in query.lower():
    #         s = (f"Opening {site[0]}")
    #         webbrowser.open(site[1])
    #         speaker.speak(s)
    #         break

    if "music".lower() in query.lower():
        musicPath = "C:/Users/deepp/Desktop/Till I Collapse.mp3"
        os.startfile(musicPath)
        break

    elif "time".lower() in query.lower():
        musicPath = "/Users/deepp/Desktop/Till I Collapse.mp3"
        tm = datetime.datetime.now().strftime("%H:%M:%S")
        s = (f"Time is {tm}")
        speaker.speak(s)
        break
    else:
        speaker.speak(s)
        break
        # elif "Using artificial intelligence".lower() in query.lower():
        #     ai(prompt=query)

        # elif "AI Quit".lower() in query.lower():
        #     exit()

        # elif "reset chat".lower() in query.lower():
        #     chatStr = ""

        # else:
        #     print("Chatting...")
        #     chat(query)