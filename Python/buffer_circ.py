def buffer_circular(x,buffer,delay,n):
    length = len(buffer)
    indexC = np.mod(n-1,length) 
    indexD = np.mod(n-delay-1,length) 
    y[n] = buffer[indexD]
    buffer[indexC] = x[n]
    return y[n], buffer
