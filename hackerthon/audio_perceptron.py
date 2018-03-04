import speech_recognition as sr
import sentiment_classifier as s
#import tweet_based_sentiment_classifier as s
import time
import os
from gtts import gTTS

'''
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print("Your input is : {0}".format(text))
try:
    result = s.sentiment(text)
    classification = result[0]
    confidence_level = result[1]
    print("The sentence is {0}, confidence level is {1}".format(classification, confidence_level))
    # print(s.sentiment(text))
except sr.UnknownValueError:
    print("Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Speech Recognition service; {0}".format(e))
'''


def speak(audioString):
    print(audioString)
    # tts = gTTS(text=audioString, lang='en')
    # tts.save("data/audio.mp3")
    # os.system("mpg321 audio.mp3")


def jarvis(data):
    if data is None:
        speak("I can't hear you.")
    else:

        if "Positive" in data:
            speak("You sound like positive.")

        if "Negative" in data:
            speak("You sound like negative.")

        if "where is" in data:
            data = data.split(" ")
            location = data[2]
            speak("Hold on Frank, I will show you where " + location + " is.")
            os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")


def demo():
    print("=================================================================")
    print("Please wait for a moment.")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something please...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("Your input is : {0}".format(text))
        result = s.sentiment(text)
        classification = result[0]
        confidence_level = result[1]
        print("The sentence is {0}, confidence level is {1}".format(classification, confidence_level))
        # print(s.sentiment(text))
        return classification
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Speech Recognition service; {0}".format(e))

# initialization
time.sleep(2)
speak("Hi there, I am Jarvis. What can I do for you?")
while 1:
    data = demo()
    jarvis(data)
