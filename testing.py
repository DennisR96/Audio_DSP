import Audio_DSP
import matplotlib.pyplot as plt

x, y = Audio_DSP.Sinus(1,5,48000,3)

plt.plot(x,y)
plt.show()