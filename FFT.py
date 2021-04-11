import numpy as np
import matplotlib.pyplot as plt

def Fast_Fourier(x):
    # 2 - Fast Fourier Analyse
    y = np.fft.fft(x)  # FFT
    y = y / len(y)  # FFT Normalise
    y_freq = np.fft.fftfreq(x.size, 1 / fs)  # Frequencies
    return y_freq, y

# 1 - Signal erstellen
t = 3                       # Zeit
fs = 48000                  # Abtastfrequenz
N = fs * t                  # Samples

f = 6000                    # Frequenz
T = 1/f                     # Periode
amp = 1                     # Amplitude

x_arange = np.arange(0,t,1/fs)                                                  # X-Achse
x = amp * np.sin(2*np.pi*x_arange*f) + amp/2 * np.sin(2*np.pi*x_arange*2*f)     # Y-Achse

# 2 - Fast Fourier
y_freq, y = Fast_Fourier(x)



# 3 - Plot erstellen
N = 128
fig, ax = plt.subplots(nrows=3, ncols=1,figsize=(8,16))
ax[0].plot(x_arange[0:N],x[0:N],color='C0')
ax[0].set_ylabel("Amplitude")
ax[0].set_title("Zeitbereich")
ax[0].set_xlabel("Zeit in [s]")
ax[1].plot(y_freq,np.abs(y),color='C1')
ax[1].set_title("Frequenzbereich")
ax[1].set_xlabel("Frequenz in [Hz]")
ax[1].set_xlim(0,20000)                                    # Nur Positive Werte
#ax.set_ylim(0.0,1.0)
ax[1].set_ylabel("Amplitude")
ax[2].set_title("Phasensektrum")
ax[2].phase_spectrum(x,fs,color='C2')
plt.show()