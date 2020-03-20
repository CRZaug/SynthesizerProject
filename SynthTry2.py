import numpy as np
#import matplotlib.pyplot as plt
from numpy.fft import fft, ifft
import tkinter as tk
from scipy.io import wavfile
from pygame import mixer

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        
        # Create the place where the user specifies the frequency
        self.freq_title = tk.Label(self)
        self.freq_title["text"]="Frequency"
        #self.title.pack(side='left')
        self.freq_title.grid(row=0,column=0,pady=20)
        
        self.frequency_box = tk.Entry(self)
        self.frequency_box.grid(row=0,column=1,pady=20)
        
        self.freq_scale = tk.Scale(self, from_=0, to=200, orient="horizontal")
        self.freq_scale.grid(row=0,column=2,pady=20,padx=10)
        
        
        # Create the space where the user sets the first harmonic amplitude
        self.h1_t = tk.Label(self)
        self.h1_t["text"]="1st harmonic amplitude"
        #self.title.pack(side='left')
        self.h1_t.grid(row=2,column=0)
        
        self.h1_box = tk.Entry(self)
        self.h1_box.grid(row=2,column=1)
        
    
        self.h1_scale = tk.Scale(self, from_=0, to=1, orient="horizontal")
        self.h1_scale.grid(row=2,column=2,padx=10)
        
        # Create the space where the user sets the second harmonic amplitude
        self.h2_t = tk.Label(self)
        self.h2_t["text"]="2nd harmonic amplitude"
        #self.title.pack(side='left')
        self.h2_t.grid(row=3,column=0)
        
        self.h2_box = tk.Entry(self)
        self.h2_box.grid(row=3,column=1)
        
        self.h2_scale = tk.Scale(self, from_=0, to=1, orient="horizontal")
        self.h2_scale.grid(row=3,column=2,padx=10)
        
        # Create the space where the user sets the third harmonic amplitude
        self.h3_t = tk.Label(self)
        self.h3_t["text"]="3rd harmonic amplitude"
        #self.title.pack(side='left')
        self.h3_t.grid(row=4,column=0)
        
        self.h3_box = tk.Entry(self)
        self.h3_box.grid(row=4,column=1)
        
        self.h3_scale = tk.Scale(self, from_=0, to=1, orient="horizontal")
        self.h3_scale.grid(row=4,column=2,padx=10)
    
    def playtone(self,f):    
        
        
        t = np.linspace(0,1,44100)
        
        amps = np.ones(5,dtype=complex)
        randvals = np.random.rand(5)*2*np.pi
        amps = np.cos(randvals)+ 1j*np.sin(randvals)
     
        
        
        asf = np.arange(1,6)*f
        print(asf)
        
        amps2 = np.append(np.conj(np.flip(amps,axis = 0)),amps[:-1])
        asf2 = np.append(-1*np.flip(asf,axis = 0),asf[:-1])
        
        print(asf2)
        
        signal = 0
        for u in range(len(amps2)):
            signal+= (50*len(amps2))*(amps2[u])*np.exp(2j*np.pi*asf2[u]*t) #the amplitude matters! also sounds better w/ a 1/2
        
        
        # The signal must be real to write the file
        signal=np.real(signal)
        
        # Generate the array that is necessary to write the file. Notice there are now 2 channels
        newsound = np.zeros((len(signal),2),dtype=int)
        for kj in range(len(signal)):
            newsound[kj]=[int(signal[kj]),int(signal[kj])]
        # print(newsound[0:10])
        
        
    
        # Write and save the array! Needs to have the correct dtype
        newsound = np.asarray(newsound, dtype=np.int16)
        
        dir = 'TestsFolder2/another5.wav'
        
        wavfile.write(dir, 44100, newsound) #44100 Hz is the sampling rate for audio files
        
        
        mixer.init()
        mixer.music.load(dir)
        mixer.music.play()
        
     
        
    def run_sth(self):
        print('playing the sound you generated')
        a = self.frequency.get()
        while True:
            try:
                f = float(a)
                break
            except ValueError:
                print("Oops!  That was not a valid number.  Try again...")
                break
        print(f)
        self.playtone(f)
        return f
    

root = tk.Tk()
app = Application(master=root)
app.mainloop()