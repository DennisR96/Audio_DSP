# Bibliotheken
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import scipy.io.wavfile as wavfile
import scipy.signal as signal


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


def Speed(y, factor):
    index = np.arange(0,len(y),factor)
    return y[index[index < len(y)].astype(int)]

def Distortion(y,N):
    y = np.arcsin(np.clip(y,-N,N))
    y = y / np.max(y)
    return y




# Work in Progress
def Semitone_to_Frequency(n):
    f = 440 * np.exp(n * np.log(2) / 12)
    d = n % 12
    Notes = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
    Note = Notes[d]
    #print("Note {A} hat eine Frequenz von {B:.2f} Hz".format(A=Note,B=f))
    return f

def Frequency_to_Note(f):
    Notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    Freq = [440 * np.exp(n*np.log(2) / 12) for n in np.arange(0,12)]
    n = int(np.round(((12*np.log(f/55))/(np.log(2))) - 36))
    idx = n % 12
    Note = Notes[idx]
    z = int(np.round((f / Freq[idx]) + 3))      # WIP**
    print("Die Frequenz {A} Hz entspricht der Note {B}{C}".format(A=f,B=Note,C=z))
    return 0

def ADSR(len_A,len_D,len_S,len_R,height_A,height_S):
    curve_A = np.arange(len_A) * height_A / len_A
    curve_D = height_A - np.arange(len_D) * (height_A - height_S) / len_D
    curve_S = np.ones(len_S) * height_S
    curve_R = height_S * (1 - np.arange(1, len_R + 1) / len_R)
    curve_ADSR = np.concatenate((curve_A, curve_D, curve_S, curve_R))
    return curve_ADSR
