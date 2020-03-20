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
        self.title = tk.Label(self)
        self.title["text"]="Frequency"
        self.title.pack(side='left')
        

        self.frequency = tk.Entry(self)
        
        self.frequency.pack(side='left')
        
        self.run = tk.Button(self,text = 'Run!')
        self.run["command"] = self.run_sth
        self.run.pack(side='bottom')
        
        self.quit = tk.Button(self,text = 'quit',command = self.master.destroy)
        
        self.quit.pack(side='bottom')
        
    
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
    
    
        
       
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")
        # 
        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=self.master.destroy)
        # self.quit.pack(side="bottom")

    # def say_hi(self):
    #     print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()