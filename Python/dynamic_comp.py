import numpy as np
import matplotlib.pyplot as plt
import Audio_DSP
import sounddevice as sd

def Compressor(x,Attack,Release,Make_Up_Gain,Ratio,Threshold,Width):
    # 0 - Parameter
    fs = 48000
    A = Attack
    Re = Release
    M = Make_Up_Gain
    R = Ratio
    T = Threshold
    W = Width

    # 1 - Linear to Decibel
    x_G = 20*np.log10(np.abs(x))

    #2 - Gain Computing
    # 2.1 - Compression
    y_G = np.zeros(len(x_G))
    overshooting = (x_G - T)
    for i in range(0,len(overshooting)):
        if 2*(overshooting[i]) < -W:
            y_G[i] = x_G[i]
        elif 2*np.abs(overshooting[i])<= W:
            y_G[i] = x_G[i] + (1/R-1)*(overshooting[i]+W/2)**2 / (2*W)
        elif 2*np.abs(overshooting[i]) > W:
            y_G[i] = T + overshooting[i] / R

    # 2.2 - Make-Up Gain
    y_G = y_G + M


    # 2.3 - Gain Computation
    g_c = y_G - x_G

    # 3 - Gain Smoothing
    a_A = np.exp(-np.log(9) / (fs * Attack))  # Attack-Coefficient #-np.log(9)
    a_R = np.exp(-np.log(9) / (fs * Release))  # Release-Coefficient
    g_s = np.zeros(len(g_c))

    for i in range(0, len(g_c)):
        if g_c[i] <= g_s[i - 1]:
            g_s[i] = a_A * g_s[i - 1] + (1 - a_A) * g_c[i]
        elif g_c[i] > g_s[i - 1]:
            g_s[i] = a_R * g_s[i - 1] + (1 - a_R) * g_c[i]


    # 4 - Decibles to Linear
    g_lin = 10 ** (g_s/20)

    # 5 - Apply Compression
    y = x * g_lin
    return y, x_G, y_G

# Testsginal
amp = 1
f = 2
t = 3
fs = 48000
x_arange = np.arange(0,t,1/fs)
x1 = amp * np.sin(2*np.pi*x_arange*f)
x2 = amp/2 * np.sin(2*np.pi*x_arange*f)
x = np.concatenate((x1,x2))
x_arange = np.arange(0,len(x)/fs,1/fs)

# Compression


A, x_G_Soft, y_G_Soft = Compressor(x=x,Attack=0.00001,Release=0.00001,Make_Up_Gain=10,Ratio=5,Threshold=-20,Width=30)
B, x_G_Hard, y_G_Hard = Compressor(x=x,Attack=0.00001,Release=0.00001,Make_Up_Gain=10,Ratio=5,Threshold=-20,Width=0)

x_SoftB = np.arange(0,len(A)/fs,1/fs)
x_HardA = np.arange(0,len(B)/fs,1/fs)

fig, ax = plt.subplots(nrows=1,ncols=1)
ax.plot(x_G_Soft,x_G_Soft,label="No Compression")
ax.plot(x_G_Hard,y_G_Hard,label="5:1 - Compression, Hard Knee")
ax.plot(x_G_Soft,y_G_Soft,label="5:1 - Compression, Soft Knee")
ax.set_title("Characteristic")
ax.set_xlabel("Input $x_G$ in [dB]")
ax.set_ylabel("Output $y_G$ in [dB]")
ax.set_ylim(-50,0)
ax.set_xlim(-50,0)
ax.legend()
plt.close()


fig, ax = plt.subplots(nrows=1,ncols=1)
ax.set_title("Signals")
ax.plot(x_arange,x,label="No Compression")
ax.plot(x_HardA,B,label="5:1 - Compression, Hard Knee")
ax.plot(x_SoftB,A,label="5:1 - Compression, Soft Knee")
ax.legend()
ax.set_xlabel("Time in [s]")
ax.set_ylabel("Amplitude")
plt.show()
plt.close()

sd.play(A,fs)
sd.wait()
