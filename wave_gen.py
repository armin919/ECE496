import matplotlib.pylab as pyl
import numpy as np
import matplotlib.pyplot as plot
import sounddevice as sd
from scipy.io.wavfile import write



def signalGen(bit,startTime):
	
	stepSize = 1/44100 #resolution, Time between sampling
	t = np.arange(startTime,startTime+1,stepSize) #arrange(start,stop,increment value)

	if bit == "1":
		ym = 1000 * np.sin(2 * pyl.pi * (440) * t) #Modulating signal
	else:
		ym = 1000 * np.sin(2 * pyl.pi * (880) * t) #Modulating signal

	return t,ym
	

def FinilizeSignal(bitSeq):
	wave = [] #has the form [[time,sinewave]]
	count = 0
	for bit in bitSeq:
		t,ym = signalGen(bit,count) #getting related sine wave for each time interval
		wave.append([t,ym])
		count += 1
	return wave


wave = FinilizeSignal("111101010101010")

finalWave = []	

for sine in wave:
	wav_wave = np.array(sine[1], dtype=np.int16)
	sd.play(wav_wave, blocking=True)
	pyl.plot(sine[0],sine[1],'b')
	finalWave = np.append(finalWave,sine[1])
	#print(finalWave)
scaled = np.int16(finalWave/np.max(np.abs(finalWave)) * 32767)
write('test.wav', 44100, scaled)
#print(finalWave)
#pyl.show()
