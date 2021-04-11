import numpy as np
import matplotlib.pyplot as plt

# 1 - Signal erstellen
t = 3                       # Zeit
fs = 48000                  # Abtastfrequenz
N = fs * t                  # Samples

f = 6000                    # Frequenz
T = 1/f                     # Periode
amp = 1                     # Amplitude

x_arange = np.arange(0,t,1/fs)                                                  # X-Achse
x = amp * np.sin(2*np.pi*x_arange*f) + amp/2 * np.sin(2*np.pi*x_arange*2*f)     # Y-Achse


# 2 - Fast Fourier Analyse
y = np.fft.fft(x)                                       # FFT
y = y / len(y)                                          # FFT Normalise
y_freq = np.fft.fftfreq(x.size,1/fs)                    # Frequencies


# 3 - Plot erstellen
fig, ax = plt.subplots(nrows=3, ncols=1,figsize=(10,12))
ax[1].plot(y_freq,np.abs(y))
ax[1].set_title("$FFT$ - Fast Fourier Transformation")
ax[1].set_xlabel("Frequenz in [Hz]")
ax[1].set_xlim(0,20000)                                    # Only Display Positive Values
#ax.set_ylim(0.0,1.0)
ax[1].set_ylabel("Amplitude")
plt.show()