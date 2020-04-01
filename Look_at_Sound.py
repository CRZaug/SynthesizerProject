"""
This code reads in recordings of instruments and cleans the recordings. (.wav)

None of this is done in stereo, so just use the x channel.

By clean, I mean removes all noise. If you know what note is being played, it finds the harmonics.
It removes all amplitudes except those harmonics.
Then it writes a .wav file.

"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft
import wave
from scipy.io import wavfile

# Define so that we may examine the spectrum; this is the frequency vector
def kvec(gridnum):
        split = int(gridnum/2)
        k = np.zeros(gridnum)
        k[0:split+1] = np.arange(0,split+1,1)
        k[split+1:gridnum] = np.arange(-split+1,0,1)
        return k


# This reads in files of a trumpet and mellophone playing an F4
frequency = 349.23

# Names of the files
names = ['TempFolder/temp']
#names = ['trumpet']

#Comment back in later  if you want to see the spectra
fig2,ax2=plt.subplots(1,2,figsize = (9,4))

j=0
for name in names:

    # read in the wav file, which I had to convert from mp4 to wav using iTunes
    fs, data = wavfile.read(name+'.wav')

    # number of data points
    N = len(data)
    
    # the time grid
    t = np.linspace(0,len(data)/fs,len(data))
    
    # Only read in the x channel because we are saving time
    x = np.zeros(N,dtype=int)
    for row in range(N):
        x[row]=data[row][0]
        
 
    N = len(x) # this seems repetitive but ok
    
    # We want things to be even for FFT purposes, even though the FFT is smart enough to deal with this anyway
    if N%2 !=0:
        t=np.delete(t,-1)
        x=np.delete(y,-1)
        N=N-1
    
    # This is the period of data collection, assuming t[0]=0
    L=t[-1]    
    
    # Get the Frequencies and Fourier amplitudes
    k = kvec(N)
    data = fft(x)
    
    #print(1/N*sum(data*np.conj(data)))
    
    # Plot both the mellophone and the trumpet, normalizing by |a_0|
    # This plot will just let us compare the two. It's commented out for now
    ax2[j].plot((k/L)[:N//2],np.abs(data)[:N//2])
    #ax2[j].plot((k/L)[:N//5],np.abs(data)[:N//5]/max(data)
    ax2[j].axvline(x=698.46, ymin=0, ymax=1,color='r',linestyle = '--')
    ax2[j].set_xlabel('frequency (Hz)')
    ax2[j].set_ylabel('Normalized Amplitude')
    ax2[j].set_yscale('log')
    ax2[j].set_title(name+' X Channel FFT')
    j+=1
plt.show()
 