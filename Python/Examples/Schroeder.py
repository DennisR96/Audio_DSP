import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import scipy.io.wavfile as wavfile

fs, x = wavfile.read("Python/Examples/h1.wav")




T = 1500
x = x[0:T]
x_range = np.arange(0,len(x)/fs,1/fs)



#x = np.abs(x) / np.max(x)
sch_sum = np.cumsum(x[::-1]**2)[::-1]
sch_sum_db = 10.0 * np.log10(sch_sum / np.max(sch_sum))

sch_trapz = integrate.cumtrapz(x[::-1]**2,initial=0)[::-1]
sch_trapz_db = 10.0 * np.log10(sch_trapz / np.max(sch_trapz))

plt.plot(x_range,sch_trapz_db)
plt.plot(x_range,sch_sum_db)
plt.xlabel("Zeit in [s]")
plt.ylabel("Amplitude")
plt.title("Schroeder Rückwärtsintegration")
plt.show()