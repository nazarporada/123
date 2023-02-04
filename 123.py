import webbrowser
from datetime import datetime
import os
from gtts import gTTS
import pygame
import datetime

import speech_recognition as sr



def talk(words):
    print(words)
    os.system("say " + words)


tts = gTTS("Доброго дня", lang='uk')
tts.save('output.mp3')
pygame.mixer.init()
pygame.mixer.music.load('output.mp3')
pygame.mixer.music.play()


def command():
    global zadanie
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говоріть")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        zadanie = r.recognize_google(audio, language="uk-UA").lower()
        print("Ви сказали: " + zadanie)
    except sr.UnknownValueError:
        tts1 = gTTS("я не розумію", lang='uk')
        tts1.save('output1.mp3')
        pygame.mixer.init()
        pygame.mixer.music.load('output1.mp3')
        pygame.mixer.music.play()

    return zadanie


def makeSomething(zadanie):
    if 'привіт' in zadanie:

        tts2 = gTTS("дай Боже", lang='uk')
        tts2.save('output3.mp3')
        pygame.mixer.init()
        pygame.mixer.music.load('output3.mp3')
        pygame.mixer.music.play()
    elif 'бувай здоровий' in zadanie:
        tts3 = gTTS("До побачення", lang='uk')
        tts3.save('output3.mp3')
        pygame.mixer.init()
        pygame.mixer.music.load('output3.mp3')
        pygame.mixer.music.play()
    elif 'як тебе звати' in zadanie:
        tts4 = gTTS("мене звати роберто", lang='uk')
        tts4.save('output4.mp3')
        pygame.mixer.init()
        pygame.mixer.music.load('output4.mp3')
        pygame.mixer.music.play()
    elif 'ти бидло' in zadanie:
        tts5 = gTTS("Ні, це Андрій Калита бидло, а не я", lang='uk')
        tts5.save('output5.mp3')
        pygame.mixer.init()
        pygame.mixer.music.load('output5.mp3')
        pygame.mixer.music.play()
    elif 'котра година' in zadanie:
        time = datetime.datetime.now().strftime('%I:%M %p')
        tts6 = gTTS(time, lang='uk')
        tts6.save('output6.mp3')
        pygame.mixer.init()
        pygame.mixer.music.load('output6.mp3')
        pygame.mixer.music.play()
    elif 'яка погода' in zadanie:
        webbrowser.open("https://ua.sinoptik.ua/погода-львів")
        tts7 = gTTS("", lang='uk')
        tts7.save('output7.mp3')
        pygame.mixer.init()
        pygame.mixer.music.load('output7.mp3')
        pygame.mixer.music.play()


while True:
    makeSomething(command())
