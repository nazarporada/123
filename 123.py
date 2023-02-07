import pygame
import speech_recognition as sr
from gtts import gTTS

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
        if "здоров" in zadanie:
            with sr.Microphone() as source:
                print("слухаю")
                r.pause_threshold = 1
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)
                try:
                    zadanie = r.recognize_google(audio, language="uk-UA").lower()
                    if 'привіт' in zadanie:
                        tts2 = gTTS("дай Боже", lang='uk')
                        tts2.save('output3.mp3')
                        pygame.mixer.init()
                        pygame.mixer.music.load('output3.mp3')
                        pygame.mixer.music.play()
                        return command()
                    elif 'папа' in zadanie:
                        tts3 = gTTS("До побачення", lang='uk')
                        tts3.save('output3.mp3')
                        pygame.mixer.init()
                        pygame.mixer.music.load('output3.mp3')
                        pygame.mixer.music.play()
                        return command()
                    elif 'як тебе звати' in zadanie:
                        tts4 = gTTS("мене звати роберто", lang='uk')
                        tts4.save('output4.mp3')
                        pygame.mixer.init()
                        pygame.mixer.music.load('output4.mp3')
                        pygame.mixer.music.play()
                        return command()


                except sr.UnknownValueError:
                    tts1 = gTTS("я не розумію", lang='uk')
                    tts1.save('output1.mp3')
                    pygame.mixer.init()
                    pygame.mixer.music.load('output1.mp3')
                    pygame.mixer.music.play()

            return zadanie
    except sr.UnknownValueError:
        tts1 = gTTS("я не розумію", lang='uk')
        tts1.save('output1.mp3')
        pygame.mixer.init()
        pygame.mixer.music.load('output1.mp3')
        pygame.mixer.music.play()


while True:
    command()
