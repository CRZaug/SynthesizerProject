import numpy as np
from numpy.fft import fft, ifft
import tkinter as tk
from scipy.io import wavfile
from pygame import mixer
from Process import Process

class Application(tk.Frame): # Application is a child class of tk.Frame
    
    __amps = None 
    __N = None
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        
      
    def create_widgets(self):
        
        # Create the place where the user specifies the frequency
        self.freq_title = tk.Label(self)
        self.freq_title["text"]="Frequency"
        self.freq_title.grid(row=0,column=0)
        
        v = tk.StringVar(root, value='698') # This is the suggested frequency F5
        self.frequency_box = tk.Entry(self,textvariable=v)
        self.frequency_box.grid(row=1,column=0)
        
        
        # Create the number of modes the user can play with
        self.__N = 10
        
        rownum = 2
        colnum = 0
        
        self.t = tk.Label(self,text = 'Harmonic frequency')
        self.t.grid(row = rownum+1,column=colnum)
        
        # Add the sliders for the other harmonics
        slider_results = []
        for i in range (self.__N):
            self.h1_t = tk.Label(self)
            self.h1_t["text"]= str(i+1)
            self.h1_t.grid(row=rownum+1,column=colnum+1)

            
            self.h1_scale = tk.Scale(self, from_=100, to=0, orient="vertical")
            self.h1_scale.grid(row=rownum,column=colnum+1)

            colnum+=1
            
            
            slider_results.append(self.h1_scale)
            
        # Create a vector of the sliders
        self.__slider_amps = slider_results
        
        # Create the run and quit buttom
        self.run=tk.Button(self,text = 'run',command = self.run_sth) # do the thing
        self.run.grid(row=rownum+2)
        self.quit=tk.Button(self,text = 'quit',command = self.master.destroy)
        self.quit.grid(row=rownum+3)
        

    # This runs whne the run button is pressed
    def run_sth(self):
        
        while True:
            try:
                __passfreq = float(self.frequency_box.get())
                __passamp = []
                for i in range(self.__N):
                    __passamp.append(float(self.__slider_amps[i].get()))
                break
            except ValueError:
                print("Oops!  That was not a valid number.  Try again...")
                break
        
        # Create the wav file data
        (__wave,__file) = Process.process(self,__passfreq,__passamp,self.__N)
        
        # Write the file
        wavfile.write(__file, 44100,__wave)
        
        # Play the file using pygame
        mixer.init()
        mixer.music.load(__file)
        mixer.music.play()
        

root = tk.Tk()
app = Application(master=root)
app.mainloop()