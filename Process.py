import numpy as np
#import SynthTry2 as snth

class Process(): 
    
    __file_to_write = None
    __place_to_write = None
    
    
    def __init__(self, __freq,__amps,__N): # These are the default args, user passes to the new class


        self.process()
    
    def process(self,__freq,__amps,__N):    
        
        print('ok')
        print('freq',__freq)
        print('amplitudes',__amps)
        print('number of amplitudes',__N)
        
        __t = np.linspace(0,1,44100)
        
        #amps = np.ones(5,dtype=complex)
        __randvals = np.random.rand(__N)*2*np.pi
        __amps = (np.cos(__randvals)+ 1j*np.sin(__randvals))*__amps
     
        __scale = 88000/sum(np.abs(__amps))
        
        __asf = np.arange(1,6)*__freq
        print(__asf)
        
        __amps2 = np.append(np.conj(np.flip(__amps,axis = 0)),__amps[:-1])
        __asf2 = np.append(-1*np.flip(__asf,axis = 0),__asf[:-1])
        
        print(__asf2)
        
        __signal = 0
        for u in range(len(__amps2)):
            __signal+= (300*len(__amps2))*(__amps2[u])*np.exp(2j*np.pi*__asf2[u]*__t) 
        
        
        # The signal must be real to write the file
        __signal=np.real(__signal)
        
        # Generate the array that is necessary to write the file. Notice there are now 2 channels
        __newsound = np.zeros((len(__signal),2),dtype=int)
        for kj in range(len(__signal)):
            __newsound[kj]=[int(__signal[kj]),int(__signal[kj])]
        # print(newsound[0:10])
        
        
    
        # Write and save the array! Needs to have the correct dtype
        __m = max(np.abs(__newsound[0]))
        #__newsound = np.asarray(__newsound, dtype=np.int16)
        
        __newsound=(__newsound/__m).astype(np.float32)
        
        # self.file_to_write = __newsound
        # 
        # self.place_to_write = 'TestsFolder2/another5.wav'
        
        return(__newsound,'TestsFolder2/temp3.wav')
        
        # wavfile.write(dir, 44100, newsound) #44100 Hz is the sampling rate for audio files
        # 
        # 
        # mixer.init()
        # mixer.music.load(dir)
        # mixer.music.play()
        
     
#         
#     def run_sth(self):
#         print('playing the sound you generated')
#         a = self.frequency_box.get()
#         
#         print(a)
#         
#         print(self._amps)
#         
#         # for i in range((self.amp_num()):
#             
#         
#         while True:
#             try:
#                 f = float(a)
#                 break
#             except ValueError:
#                 print("Oops!  That was not a valid number.  Try again...")
#                 f=0
#                 break
#         print(f)
#         self.playtone(f)
#         return f
#     
# 
# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()