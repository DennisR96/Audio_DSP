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
amp = 1
f = 3
t = 3
fs = 48000
x_arange = np.arange(0,t,1/fs)
x = amp * np.sin(2*np.pi*x_arange*f)

fig, ax = plt.subplots(nrows=2,ncols=1,figsize=(6,7))
ax[1].plot(x_arange,x)
ax[1].set_xlabel("Amplitude in [s]")
plt.show()