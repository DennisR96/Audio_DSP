import numpy as np
import scipy.signal as signal

def Sinus(amp,f,fs,t):
    x = np.arange(0,t,1/fs)
    y = amp * np.sin(2*np.pi*f*x)
    return x, y

def Sawtooth(amp,f,fs,t):
    x = np.arange(0,t,1/fs)
    y = amp * signal.sawtooth(2*np.pi*f*x)
    return x, y