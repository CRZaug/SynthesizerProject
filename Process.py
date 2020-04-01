"""
The purpose of this class is to process data and create a file that may be written to wav

__freq: the frequency of the first harmonic
__amps: the amplitudes of the other harmonics (positive harmonics)
__N: the number of harmonics

"""


import numpy as np

class Process(): 
    
    def __init__(self, __freq,__amps,__N): # These are the default args, user passes to the new class
        self.process()
    
    def process(self,__freq,__amps,__N):    
        
     
        __t = np.linspace(0,1,44100) # Sampling rate for audio
        
        __randvals = np.random.rand(__N)*2*np.pi
        __amps = (np.cos(__randvals)+ 1j*np.sin(__randvals))*__amps
     
        # All the positive frequencies in the spectrum
        __asf = np.arange(1,__N+1)*__freq 

        # The two sided amplitudes and frequencies 
        __amps2 = np.append(np.conj(np.flip(__amps,axis = 0)),__amps[:-1])
        __asf2 = np.append(-1*np.flip(__asf,axis = 0),__asf[:-1])
        

        # Create the signal thru a DFT
        __signal = 0
        for u in range(len(__amps2)):
            __signal+= (len(__amps2))*(__amps2[u])*np.exp(2j*np.pi*__asf2[u]*__t) 
        
        
        # The signal must be real to write the file
        __signal=np.real(__signal)
        
        
        # Make sure everything is scaled properly. The larget possible magnitude is 32768
        # 24576 is 75% of that value
        
        #__rms_sig = np.sqrt(1/len(__signal)*sum(__signal**2))
        
        
        __a = 24576/max(__signal) # this is the scale factor
        __signal = __a*__signal # This is the new scaled signal
        print(max(__signal))
        
        # Do this as a secondary check on scaling if desired if desired
        # # Convert to decibels relative to full scale
        # __signalDBFS = 20*np.log10(abs(__signal)/32768) # Because 32768 is the largest value for a signed 16bit int
        # print('max DBFS', max(__signalDBFS)) # This value should be negative
        
        # Generate the array that is necessary to write the file. Notice there are now 2 channels
        __newsound = np.zeros((len(__signal),2),dtype=int)
        for kj in range(len(__signal)):
            __newsound[kj]=[int(__signal[kj]),int(__signal[kj])]

    
        # Write and save the array! Needs to have the correct dtype
        __m = max(np.abs(__newsound[0]))
        __newsound = np.asarray(__newsound, dtype=np.int16) # This 16 bit int is where we got 32768 from
        
        return(__newsound,'TempFolder/temp.wav')
        
