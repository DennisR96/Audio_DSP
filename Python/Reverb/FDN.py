# FDN
import numpy as np
import matplotlib.pyplot as plt

def buffer_circular(intp,buffer,delay,n):
    length = len(buffer)
    indexC = np.mod(n-1,length) 
    indexD = np.mod(n-delay-1,length) 
    outp = buffer[indexD]
    buffer[indexC] = intp
    return outp, buffer


fs = 48000
x = np.concatenate(([1],np.zeros(fs)))
x_range = np.arange(0,len(x)/fs,1/fs)
y = np.zeros(len(x))

N = 4
a = np.zeros((N,N))
a[0,:] = [0,1,1,0]
a[1,:] = [-1,0,0,-1]
a[2,:] = [1,0,0,-1]
a[3,:] = [0,1,-1,0]
a = a * (1/np.sqrt(2)) * 0.97


b = [1, 1, 1, 1]
c = [0.8, 0.8, 0.8, 0.8]
d = 0.3
#g = [0.97,0.97,0.97, 0.97]

G_1 = 0
G_2 = 0
G_3 = 0
G_4 = 0

M = [129, 347, 561, 634]
#M = [129, 343, 658, 1024]

t_60  = max(M) / (0.15 * fs)
print(t_60)

buffer_M1 = np.zeros(M[0])
buffer_M2 = np.zeros(M[1])
buffer_M3 = np.zeros(M[2])
buffer_M4 = np.zeros(M[3])


for n in range(0,len(x)):
    # Input Gain
    A_1 = b[0] * x[n]
    A_2 = b[1] * x[n]
    A_3 = b[2] * x[n]
    A_4 = b[3] * x[n]
    
    # Apply Gain Matrix
    B_1 = A_1 + G_1
    B_2 = A_2 + G_2
    B_3 = A_3 + G_3
    B_4 = A_4 + G_4
    
    # Apply Buffer
    C_1, buffer_M1 = buffer_circular(B_1,buffer_M1,M[0],n)
    C_2, buffer_M2 = buffer_circular(B_2,buffer_M2,M[1],n)
    C_3, buffer_M3 = buffer_circular(B_3,buffer_M3,M[2],n)
    C_4, buffer_M4 = buffer_circular(B_4,buffer_M4,M[3],n)
    
    # Output Gain
    D_1 = c[0] * C_1
    D_2 = c[1] * C_2
    D_3 = c[2] * C_3
    D_4 = c[3] * C_4
    
    # Create Gain Matrix
    V_1 = C_1 * a[0,0] + C_2 * a[0,1] + C_3 * a[0,2] + C_4 * a[0,3]
    V_2 = C_1 * a[1,0] + C_2 * a[1,1] + C_3 * a[1,2] + C_4 * a[1,3]
    V_3 = C_1 * a[2,0] + C_2 * a[2,1] + C_3 * a[2,2] + C_4 * a[2,3]
    V_4 = C_1 * a[3,0] + C_2 * a[3,1] + C_3 * a[3,2] + C_4 * a[3,3]
    
    G_1 = V_1 #* g[0]
    G_2 = V_2 #* g[1]
    G_3 = V_3 #* g[2]
    G_4 = V_4 #* g[3]
    
    # Output
    y[n] = (D_1 + D_2 + D_3 + D_4) + (d * x[n])

plt.plot(x_range,y)
