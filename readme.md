#Song Identification using Numpy, Scipy, Audiolab

>This implementation attempts to match a piece of music and find the most appropriate match in the database. It has applications as a song identifier or as a song suggester. 

>The matching of the input piece of music against the database is done by creating spectrograms and identifying key points in the spectrogram. In this case, peaks of power. A spectrogram is a graph with the time on the X-axis, frequency on the Y-axis and power on the Z-axis. Fast fourier transform is used to calculate the power and plot the spectrogram. 

>The DB (MongoDB) contains pre-processed songs with their respective hashed peak points of spectrograms. The input song's spectrogram is plotted, peak points are hashed and is matched against the database. 

>This implementation was inspired by [Avery Li-Chun Wang's paper](http://www.ee.columbia.edu/~dpwe/papers/Wang03-shazam.pdf)
