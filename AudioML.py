# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:19:14 2020

@author: sambhu
"""
import pyaudio

import speech_recognition as sr
import webbrowser as wb

SR=sr.Recognizer()

SpeechRocognition=sr.Recognizer()
SpeechRecognitionListen=sr.Recognizer()


with sr.Microphone() as source:
    print("Search Anything on YouTube")
    print('speak now')
    audio = SpeechRecognitionListen.listen(source)
    RequestText=SpeechRocognition.recognize_google(audio)
if 'search' in RequestText or 'YouTube' in RequestText:
    print(RequestText)
    SpeechRocognition=sr.Recognizer()
    url='https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
        print('Okay!, What to Search?')
        audio  = SpeechRocognition.listen(source)
        try:
            get=SpeechRocognition.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except  sr.UnknownValueError: 
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))
            
