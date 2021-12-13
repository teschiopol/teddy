import speech_recognition as sr
import os, time
import sounddevice as sd


r = sr.Recognizer()
print("Recording...")
fs = 48000
duration=5
audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1)
time.sleep(5)
print(audio_data)

# return audio from that array

'''
# read the audio data from the default microphone
print("Recognizing...")
# convert speech to text
text = r.recognize_google(audio_data, 'it-IT')
print(text)
'''
