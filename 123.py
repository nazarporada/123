import requests
import os
import datetime
from datetime import datetime

import pygame
import speech_recognition as sr
from gtts import gTTS


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
    global data
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
    elif 'котра година' in zadanie:
        time = datetime.now().strftime("%H:%M")
        tts6 = gTTS(time, lang='uk')
        tts6.save('output6.mp3')
        pygame.mixer.init()
        pygame.mixer.music.load('output6.mp3')
        pygame.mixer.music.play()
    elif 'який сьогодні день' in zadanie:
        time = datetime.now().strftime("%d/%m/%Y")
        tts8 = gTTS("сьогодні" + time, lang='uk')
        tts8.save('output8.mp3')
        pygame.mixer.init()
        pygame.mixer.music.load('output8.mp3')
        pygame.mixer.music.play()
    elif 'яка погода' in zadanie:

        s_city = "Lviv, UA"
        city_id = 0
        appid = "d972ec87c4d3b913ea5d14a1a6a9ac34"
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/find",
                               params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
            data = res.json()
            cities = ["{} ({})".format(d['name'], d['sys']['country'])
                      for d in data['list']]
            print("city:", cities)
            city_id = data['list'][0]['id']
            print('city_id=', city_id)
        except Exception as e:
            print("Exception (find):", e)
            pass

        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                               params={'id': city_id, 'units': 'metric', 'lang': 'uk', 'APPID': appid})
            data = res.json()
            print("conditions:", data['weather'][0]['description'])
            print("temp:", data['main']['temp'])
        except Exception as e:
            print("Exception (weather):", e)
            pass

        if data['main']['temp'] < 0:
            tts7 = gTTS(data['weather'][0]['description'] + str(round(data['main']['temp'])) + str("градуси нижче нуля"),
                        lang='uk')
            tts7.save('output7.mp3')
            pygame.mixer.init()
            pygame.mixer.music.load('output7.mp3')
            pygame.mixer.music.play()
        else:
            tts7 = gTTS(data['weather'][0]['description'] + str(round(data['main']['temp'])) + str("градуси вище нуля"),
                        lang='uk')
            tts7.save('output7.mp3')
            pygame.mixer.init()
            pygame.mixer.music.load('output7.mp3')
            pygame.mixer.music.play()


while True:
    makeSomething(command())