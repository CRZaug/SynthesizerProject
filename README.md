# SynthesizerProject

This project is meant to create a very simple synthesizer. I do mean simple: its main (only, really) purpose is to let the user explore how adding different harmonics to a fundamental frequency change the timbre of a note.

This project is mainly divided into two parts, the first part being inspiration for the second. 

First, the file BrassFFT.py visualizes the differences in the Fourier spectrum of a note (F4) played by a trumpet vs a mellophone (thanks to Spencer Peterson for providing the audio recordings). The original notes are included as .wav files.

Second, the files GUI.py and Process.py work together to create the synthesizer. Running GUI.py will open a rudimentary GUI where the user can input a frequecency and change the amplitudes of the harmonics (recommended that the first harmonic is always given a nonzero amplitude for the best effect!). Pressing run will call a function in Process.py and also use the pygame package to play the sound (the wav file that is played is stored in TempFolder). 

All python modules that this project depend on are:

- numpy

- matplotlib

- wave

- scipy

- pygame

- tkinter



_Some notes:_ There are a few instances where there are some bugs. Sometimes pressing run one time will create a strange sound, but pressing it again will play the expected sound. Playing frequencies that are sufficiently high (near the limits of human hearing) will result in a lower sound being played. I think these issues are caused by the way .wav files are written, but I am unsure. In fact, writing somewhat consistent .wav files was a major aspect of this project. So if I have time, I hope to continue working on these issues.

_Some personal reflections:_ I created this project as a way to kill time and also learn some things and create some cool things during the 2020 coronavirus lockdown. As a part of this process, I've taken my first steps in learning to design and create a GUI. As a happy accident, as it wasn't initially part of my plan, I've had the chance to learn some object oriented programming in Python. I've also had the excuse to try to use GitHub more effectively, a work in progress!
