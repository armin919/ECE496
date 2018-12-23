import wave
import numpy as np
import pyaudio
import sys



#Reading a wav file and read one frame per second and identify its frequency, it returns array of frequency
def freqFinderWav(fileName):
	freqArr = []
	with wave.open(fileName, 'r') as wr:
    		samplingFreq = wr.getframerate()  
    		frameNum = wr.getnframes() #Number of NumPy elements
    		loopNum = frameNum/samplingFreq #Deciding how many bits are there
    		bitNum = 0
    		while bitNum < loopNum:
                        wr.setpos(bitNum*samplingFreq)
                        da = np.fromstring(wr.readframes(samplingFreq), dtype=np.int16)
                        left, right = da[0::2], da[1::2]  # separate into left and right channel
                        lf, rf = np.absolute(np.fft.rfft(left)), np.absolute(np.fft.rfft(right))
        		#print (np.argmax(lf))
        		#print( np.argmax(rf))
                        freqArr.append(np.argmax(lf))
                        bitNum += 1
	return freqArr

#turning freqArray to bit sequence 
def demod(FreqArr):
	bitSeq = []
	for freq in FreqArr:
		if freq == 440:
			bitSeq.append(1)
		if freq == 880:
			bitSeq.append(0)
	return bitSeq

#Recording from the mic and make a file called "test.wav"
def ListenMic():
	CHUNK = 1024
	WIDTH = 2
	CHANNELS = 2
	RATE = 44100
	RECORD_SECONDS = 15

	p = pyaudio.PyAudio()

	stream = p.open(format=pyaudio.paInt16,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

	print("* recording")
	frames = []
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    		data = stream.read(CHUNK)  #read audio stream
    		frames.append(data)  #appending all chunks to get the whole picture

	print("* done")

	stream.stop_stream()
	stream.close()

	p.terminate()
	waveFile = wave.open("test.wav",'wb')
	waveFile.setnchannels(CHANNELS)
	waveFile.setsampwidth(p.get_sample_size(pyaudio.paInt16))
	waveFile.setframerate(RATE)
	waveFile.writeframes(b''.join(frames))
	waveFile.close()


ListenMic()
freqArr = freqFinderWav("test.wav")
print(freqArr)
bitSeq = demod(freqArr)
print(bitSeq)




