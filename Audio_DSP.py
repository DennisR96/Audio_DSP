# Bibliotheken
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import scipy.io.wavfile as wavfile


# .Wav - Manipulation
def WAV_Read(filename):
    fs, data = wavfile.read(filename)
    return fs, data

def WAV_Write():
    pass

def WAV_Play(data,fs):
    sd.play(data,fs)
    sd.wait()
    return 0

def WAV_Record(data,fs):
    pass

# Generator
def Sinus(amp,f,fs,t):
    x = np.arange(0,t,1/fs)
    y = amp * np.sin(2*np.pi*f*x)
    return x, y

def Speed(y, factor):
    index = np.arange(0,len(y),factor)
    return y[index[index < len(y)].astype(int)]

def Distortion(y,N):
    y = np.arcsin(np.clip(y,-N,N))
    y = y / np.max(y)
    return y



