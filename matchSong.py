import sys
from numpy.fft import fft
from pylab import *
import wave

from pymongo.connection import Connection
connection = Connection("localhost")
db = connection.foo

def is_sublist(a, b):
    if a == []: return True
    if b == []: return False
    return b[:len(a)] == a or is_sublist(a, b[1:])

def matchSong(speech):
    spf = wave.open(speech,'r')
    sound_info = spf.readframes(-1)

    sound_info = fromstring(sound_info, 'Int16')

    f = spf.getframerate()

    subplot(211)
    plot(sound_info)
    title('Wave from and spectrogram of %s' % sys.argv[1])

    subplot(212)
    spectrogram = specgram(sound_info[:203456], Fs = f, scale_by_freq=True,sides='default')

    totalLen = len(spectrogram[0])
    power = spectrogram[0]
    time = spectrogram[2]

    i = 0
    hashSong = []

    while i < totalLen:
        hashSong.append(str(round(max(power[i]))))
        i += 1
 
    songs = db.songHashes.find()
    matches = {}

    print "==============================================="
    print "Searcing songs DB for a match"
    print "==============================================="

    for song in songs:
        print "Searching : " + song['songName']
        matchLength = len(set(song['songHash']) & set(hashSong)) 
	if (matchLength):
		matches[song['songName']] = matchLength
		#print "Found : " + song['songName']
		#break
    print "==============================================="
    print str(len(matches)) + " Matches found"
    print "================================================"

    for key, value in sorted(matches.iteritems(), key=lambda (k,v): (v,k)):
    	print "%s: %s matches" % (key, value)
    
    print "================================================"

    inverse = [(value, key) for key, value in matches.items()]
    print "Best match: " + max(inverse)[1]

    spf.close()
    show()

song = sys.argv[1]

matchSong(song)

