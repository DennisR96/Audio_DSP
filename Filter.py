import numpy as np
import matplotlib.pyplot as plt

def Filter(x):
    # 6 - 9 kHz Bandpass
    y = [0] * len(x)
    b0 = 0.0101
    b1 = 2.4354
    b2 = 0.0202
    b3 = 0
    b4 = 0.0101

    a1 = 2.4354
    a2 = 3.1869
    a3 = 2.0889
    a4 = 0.7368

    for n in range(4,len(x)):
        y[n] = b0*x[n] - b2 * x[n-2] + b4 * x[n-4] + a1 * y[n-1] - a2*y[n-2] + a3*y[n-3] - a4*y[n-4]
    return y

f = 6e03
fs = 48000
#x = [np.sin(2*np.pi*i*f) for i in np.arange(0,1,1/fs)]
x = [99999999999,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
#x = np.random.random(48000)
y = Filter(x)


plt.magnitude_spectrum(x)
plt.magnitude_spectrum(y)
plt.show()