"""
TABLE(clap combinations):


1:- yt with query
2:- yt
3:- reddit
4:- google with query
5:- github
6:- gmail
7:- whatsapp
8 + 1:- image searching
8 + 2:- shopping of a product
8 + 3:- news on a topic
8 + 4:- wikipedia article with query
8 + 5:- games
8 + 6:- chatgpt
"""
import sounddevice as sd
import numpy as np
import time
import pygame
from gtts import gTTS
from io import BytesIO
import webbrowser

pygame.mixer.init()

def speak(text):
    
    tts = gTTS(text, lang="en", slow=False)
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)

    # Rewind buffer and load into pygame
    mp3_fp.seek(0)
    pygame.mixer.music.load(mp3_fp, "mp3")
    pygame.mixer.music.play()

    
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)


def o(afterHTTPS):
    webbrowser.open(f"https://{afterHTTPS}")
    
speak("How can i help you?")

def detect_claps(duration=5, samplerate=44100, threshold=0.6, min_gap=0.3):
    print("Listening for claps...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float32')
    sd.wait()


    audio = audio.flatten()


    audio = np.abs(audio)


    clap_indices = np.where(audio > threshold)[0]

    claps = []
    if len(clap_indices) > 0:
        claps.append(clap_indices[0])
        for i in clap_indices[1:]:
 
            if (i - claps[-1]) > samplerate * min_gap:
                claps.append(i)

    print(f"Detected {len(claps)} claps!")
    return len(claps)


count = detect_claps(duration=5)
print("You clapped", count, "times.")


if count == 1:
    query = input("Enter query for yt search: ")
    webbrowser.open(f"https://youtube.com/results?search_query={query}")
if count == 2:
    webbrowser.open("https://youtube.com")
if count == 3:
    webbrowser.open("https://reddit.com")
if count == 4:
    query = input("Enter query for google: ")
    webbrowser.open(f"https://google.com/search?q={query}")
if count == 5:
    webbrowser.open("https://github.com")
if count == 6:
    o("gmail.com")
if count == 7:
    o("web.whatsapp.com")
if count>7:
    def detect_claps(duration=5, samplerate=44100, threshold=0.6, min_gap=0.3):
        print("Listening for claps...")
        audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float32')
        sd.wait()


        audio = audio.flatten()


        audio = np.abs(audio)


        clap_indices = np.where(audio > threshold)[0]

        claps = []
        if len(clap_indices) > 0:
            claps.append(clap_indices[0])
            for i in clap_indices[1:]:
    
                if (i - claps[-1]) > samplerate * min_gap:
                    claps.append(i)

        print(f"Detected {len(claps)} claps!")
        return len(claps)


    count2 = detect_claps(duration=5)
    print("You clapped", count2, "times.")
    if count2 == 1:
        description = input("Enter your image description: ")
        query = description.replace(" ", "+")
        url = f"https://www.google.com/search?tbm=isch&q={query}"
        webbrowser.open(url)
    if count2 == 2:
        desc = input("Enter product description: ")
        query = desc.replace(" ", "+")
        url = f"https://www.google.com/search?tbm=shop&q={query}"
        webbrowser.open(url)
    if count2 == 3:   
        desc = input("Enter news topic: ")
        query = desc.replace(" ", "+")
        url = f"https://news.google.com/search?q={query}"
        webbrowser.open(url)
    if count2 == 4:
        desc = input("Enter topic: ")
        query = desc.replace(" ", "_")  
        url = f"https://en.wikipedia.org/wiki/{query}"
        webbrowser.open(url)
    if count2 == 5:
        o("poki.com")
    if count2 == 6:
        o("chatgpt.com")
