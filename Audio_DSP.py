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

def Semitone_to_Frequency(n):
    f = 440 * np.exp(n * np.log(2) / 12)
    d = n % 12
    Notes = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
    Note = Notes[d]
    print("Note {A} hat eine Frequenz von {B:.2f} Hz".format(A=Note,B=f))
    return f

def Frequency_to_Note(f):
    Notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    Freq = [440 * np.exp(n*np.log(2) / 12) for n in np.arange(0,12)]
    n = int(np.round(((12*np.log(f/55))/(np.log(2))) - 36))
    idx = n % 12
    Note = Notes[idx]
    z = int(np.round((f / Freq[idx]) + 3))
    print("Die Frequenz {A} Hz entspricht der Note {B}{C}".format(A=f,B=Note,C=z))
    return 0

