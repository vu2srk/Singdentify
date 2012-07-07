import sys
from numpy.fft import fft
from pylab import *
import wave

from pymongo.connection import Connection
connection = Connection("localhost")
db = connection.foo

def show_wave_n_spec(speech):
    spf = wave.open(speech,'r')
    #sound_info, f, enc = wavread(speech)
    sound_info = spf.readframes(-1)

    sound_info = fromstring(sound_info, 'Int16')

    """totalLen = len(sound_info)

    numChunks = totalLen / CHUNK_SIZE
    
    print numChunks
    print CHUNK_SIZE

    i = 0
    j = 0
    results = []

    while i < numChunks:
	complexNums = []
	while j < CHUNK_SIZE:
		complexNums.append(sound_info[(i*CHUNK_SIZE)+j])	
		j += 1
        
        #print complexNums
    	results.append(fft(complexNums))
	i += 1
	j=0
	
    print results"""

    f = spf.getframerate()
    
    subplot(211)
    plot(sound_info)
    title('Wave from and spectrogram of %s' % sys.argv[1])
     
    
    subplot(212)

    spectrogram = specgram(sound_info, Fs = f, scale_by_freq=True,sides='default')

    totalLen = len(spectrogram[0])
    power = spectrogram[0]
    time = spectrogram[2]

    i = 0
    hashSong = []

    while i < totalLen:
	hashSong.append(str(round(max(power[i]))))
	i += 1

    db.songHashes.insert({"songName":sys.argv[1],"songHash":hashSong})
    print hashSong

    show()
    spf.close()

fil = sys.argv[1]

CHUNK_SIZE = 4096

show_wave_n_spec(fil)
