import numpy as np
import matplotlib.pyplot as plt

# All Pass
def AllPass(x,Gain,Delay):
    g = Gain
    m = Delay
    y = np.zeros(len(x))
    for n in range(0,len(x)):
        y[n] = -g * x[n] + x[n-m] + g * y[n-m]
    return y

# Canonical Filter
def Canonical(x,fc,fs,Mode, Order,Q):
    K = np.tan(np.pi * fc / fs)
    if Order == 1:
        if Mode == "LP":                          
            a0 = 0
            a1 = (K-1) / (K+1)
            a2 = 0
            b0 = K / (K + 1)
            b1 = K / (K + 1)
            b2 = 0
        elif Mode == "HP":                            
            a0 = 0
            a1 = (K-1) / (K+1)
            a2 = 0    
            b0 = 1 / (K+1)
            b1 = -1 / (K+1)
            b2 = 0
        elif Mode == "AP":                           
            a1 = (K-1) / (K + 1)
            a2 = 0
            b0 = (K-1) / (K + 1)
            b1 = 1
            b2 = 0 
    elif Order == 2:
        if Mode == "LP":                            
            b0 = ((K**2) * Q) / ((K**2) + Q + K + Q)
            b1 = (2*(K**2) * Q) / ((K**2) * Q + K + Q)
            b2 = ((K**2) * Q) / ((K**2) * Q + K + Q)
            a1 = (2*Q * ((K**2) - 1)) / ((K**2) * Q + K + Q)
            a2 = ((K**2) * Q - K + Q) / ((K**2) * Q + K + Q)
        elif Mode == "HP":                          
            b0 = (Q) / ((K**2) * Q + K + Q)
            b1 = - (2*Q)/((K**2) * Q + K + Q)
            b2 = (Q) / ((K**2)* Q + K +Q)
            a1 = (2*Q * ((K**2) - 1)) / ((K**2) * Q + K + Q)
            a2 = ((K**2) * Q - K + Q) / ((K**2) * Q + K + Q)
        elif Mode == "BP":                          
            b0 = (K) / ((K**2) * Q + K + Q)
            b1 = 0
            b2 = - (K) / ((K**2) * Q + K + Q)
            a1 = (2*Q * ((K**2) - 1)) / ((K**2) * Q + K + Q)
            a2 = ((K**2) * Q - K + Q) / ((K**2) * Q + K + Q)   
        elif Mode == "BR":                          
            a1 = (2*Q * ((K**2) - 1)) / ((K**2) * Q + K + Q)
            a2 = (K**2 * Q - K + Q) / ((K**2) * Q + K + Q)
            b0 = (Q*(1+K**2)) / ((K**2) * Q + K + Q)
            b1 = (2*Q*((K**2) -1)) / ((K**2) * Q + K + Q)
            b2 = (Q * (1 + K**2)) / ((K**2) * Q + K + Q)
        elif Mode == "AP":                         
            a1 = (2*Q * ((K**2) - 1)) / ((K**2) * Q + K + Q)
            a2 = ((K**2) * Q - K + Q) / ((K**2) * Q + K + Q)
            b0 = ((K**2) * Q - K + Q) / ((K**2) + K + Q)
            b1 = (2 * Q * ((K**2) - 1))/(((K**2)*Q)+K+Q)
            b2 = 1
        pass
    xh = np.zeros(len(x))
    y = np.zeros(len(x))
    for n in range(0,len(x)):
        xh[n] = x[n] - a1 * xh[n-1] - a2 * xh[n-2]
        y[n] = b0 * xh[n] + b1 * xh[n-1] + b2 * xh[n-2]
    return y

# Comb Filter
def CombFilter(x,Gain,Delay):
    g = Gain
    m = Delay
    y = np.zeros(len(x))
    for n in range(0,len(x)):
        y[n] = x[n-m] + g * y[n-m]
    return y

plt.magnitude_spectrum(x)
plt.magnitude_spectrum(y)
plt.show()
