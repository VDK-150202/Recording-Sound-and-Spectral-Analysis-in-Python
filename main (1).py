import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft,fft2  #Importing the fft and inverse fft functions from fftpackage
import numpy as np
#plt.close('all')

#details for sound recording
Fs=19000  # Sampling frequency
d=  5    # duration is 3 sec

#record sound
print(" start Speaking:)")
#To record audio data from your sound device into a NumPy array, we used rec():
a =sd.rec( int(d*Fs), Fs,1, blocking ='True')# d*fs gives total no of samples;blocking is used because we dont want to move frwd untill rec is done
# import sounddevice as sd
#  sd.query_devices()
print('End recording')

#play
sd.play(a,Fs)

#plot the recorded wave
plt.plot(a); plt.title('Recorded sound')
plt.show()

#spectrum

X_f= fft2(a) #spectrum is taken from fft command which is provided from the scipy module

#create frequency axis

n= np.size(a) #defining the total length ; a is the data recieved after recording
# numpy.linspace(start,stop,dtype: type of o/p array)
#As FFT is double sided spectrum we are ploting only half part of it i:e Fs/2
fr=(Fs/2)*np.linspace(0,1,round(n/2)) # 0 is a start vlue and 1 is stop value, The numpy.linspace() function returns number spaces evenly w.r.t interval.
X_m= (2/n)*abs(X_f[0:np.size(fr)])

#plot spectrum
plt.figure()
plt.plot(fr,X_m); plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude'); plt.title('Sound Spectrum')
plt.show()
plt.plot(abs(X_f))