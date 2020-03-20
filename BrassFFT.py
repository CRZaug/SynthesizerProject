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
names = ['trumpet','mellophone']

#Comment back in later  if you want to see the spectra
#fig2,ax2=plt.subplots(1,2,figsize = (9,4))

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
    
    ## Plot both the mellophone and the trumpet, normalizing by |a_0|
    ## This plot will just let us compare the two. It's commented out for now
#     ax2[j].plot((k/L)[:N//5],np.abs(data)[:N//5]/max(data))
#     ax2[j].axvline(x=698.46, ymin=0, ymax=1,color='r',linestyle = '--')
#     ax2[j].set_xlabel('frequency (Hz)')
#     ax2[j].set_ylabel('Normalized Amplitude')
#     ax2[j].set_yscale('log')
#     ax2[j].set_title(name+' X Channel FFT')
#     j+=1
# plt.show()
    
    
    # It's easier to work with a 1-sided spectrum, so take positive modes
    amps = np.abs(data[:N//2])
    freqs = (k/L)[:N//2]
    
    max_peak_at_harmonic = [] # This will be the vector of peaks
    asf = [] # frequency associated with each peak
    for peakno in np.arange(1,14):
        
        # This range may be made more or less stict, depends on the needs
        mmin = frequency*.95*peakno
        mmax = frequency*1.05*peakno
        temp = []
        ftemp = []
        for p in range(len(freqs)):
            
            # ind all freqs in the above defined range
            if mmin < freqs[p] and mmax > freqs[p]:
                #plt.plot(freqs[p],amps[p],'.')
                temp.append(amps[p])
                ftemp.append(freqs[p])
        loc = np.where(amps == max(temp))[0][0] # Find the maximum value
        max_peak_at_harmonic.append(data[loc]) # This should be a complex number; it's the max amp at a mode
        asf.append(freqs[loc]) # This is the mode where the max amp above occurs
        
        ### Some plots to help visualize the above process
        # plt.plot(freqs[loc],max(temp),marker = '*',markersize = 10)
        # plt.plot(ftemp,temp)
        # plt.show()
     
    ## This plot shows the found amplitudes and compares it to the raw data   
    plt.plot(asf,np.abs(max_peak_at_harmonic),'.',markersize = 7)
    plt.plot(freqs,amps)
    plt.plot(asf,np.real(max_peak_at_harmonic),'.')
    plt.show()
    plt.close()
    
    # At this point, we have created a super-simplified version of the sound, extremely cleaned.
    # So now let's go about turning this back into an actual signal using a dft
    
    # Re-create 2 sided spectrum (amps and freqs)
    amps2 = np.append(np.conj(np.flip(max_peak_at_harmonic,axis = 0)),max_peak_at_harmonic[:-1])
    asf2 = np.append(-1*np.flip(asf,axis = 0),asf[:-1])

    
    # Do the DFT. Using a DFT because it's slightly easier and I am being lazy
    # If I wanted to do an FFT, I'd need to look at the raw data and set all modes that aren't the modes I want to 0
        # Granted, that wouldn't be that hard, but I am being lazy for now
    # Then insteaed of the DFT, I'd use signal = xnew = np.real(ifft(0.5*len(amps2)/N*ftx2))
        # See the note about the 1/2 term below
    signal = 0
    for u in range(len(amps2)):
        signal+= (0.5*len(amps2)/N)*(amps2[u])*np.exp(2j*np.pi*asf2[u]*t) #the amplitude matters! also sounds better w/ a 1/2
    
    # The signal must be real to write the file
    signal=np.real(signal)
    
    ### Plot the signal if you'd like
    # plt.plot(t,signal)
    # plt.show()
    
    ### Comare the FFT of the new signal to the original data if you'd like
    # plt.plot(k,np.abs(data)*N,)
    # plt.plot(kvec(len(signal)),np.abs(fft(signal)),'.')
    # plt.show()
    
    
    # Generate the array that is necessary to write the file. Notice there are now 2 channels
    newsound = np.zeros((len(signal),2),dtype=int)
    for kj in range(len(signal)):
        newsound[kj]=[int(signal[kj]),int(signal[kj])]
    print(newsound[0:10])
    
    # Write and save the array! Needs to have the correct dtype
    newsound = np.asarray(newsound, dtype=np.int16)
    wavfile.write('TestsFolder/'+name+'_final.wav', 44100, newsound) #44100 Hz is the sampling rate for audio files