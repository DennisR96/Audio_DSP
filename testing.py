import Audio_DSP
import matplotlib.pyplot as plt
import numpy as np



def ADSR(len_A,len_D,len_S,len_R,height_A,height_S):
    curve_A = np.arange(len_A) * height_A / len_A
    curve_D = height_A - np.arange(len_D) * (height_A - height_S) / len_D
    curve_S = np.ones(len_S) * height_S
    curve_R = height_S * (1 - np.arange(1, len_R + 1) / len_R)
    curve_ADSR = np.concatenate((curve_A, curve_D, curve_S, curve_R))
    return curve_ADSR

x, y = Audio_DSP.Sinus(1,3,48000,3)
ADSR = ADSR(10,20,60,10,1,0.5)
y = np.convolve(y,ADSR)

plt.plot(y)
plt.show()