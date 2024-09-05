import numpy as np
import matplotlib.pyplot as plt
 
fs = 1000
t = np.linspace(0, 1, fs,endpoint=False)

freq = 50
x= np.sin(2 * np.pi *freq *t)

X =np.fft.fft(x)
freqs = np.fft.fftfreq(len(X),1/fs)

ampli = np.abs(X)

plt.figure(figsize=(10,6))
plt.plot(freqs[:len(freqs)//2],ampli[:len(ampli)//2])
plt.grid()
plt.show()

