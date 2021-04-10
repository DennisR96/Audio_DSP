import numpy as np
import matplotlib.pyplot as plt
import Audio_DSP

def Compressor(x,Attack,Release,Make_Up_Gain,Ratio,Threshold,Width):
    # 0 - Parameter
    A = Attack
    Re = Release
    M = Make_Up_Gain
    R = Ratio
    T = Threshold
    W = Width

    # 1 - Linear to Decibel
    x_G = 20*np.log10(np.abs(x))




# Testsginal
x = Audio_DSP.Sinus(amp=1,f=3,fs=48000,t=3)

plt.plot(x)