from scipy import signal
import numpy as np

def smooth_convolution(time_series, window_type='hann', window_size=10, fft=False):
	window = [1] #Unit Impluse
	if window_type=='hann':
		window = signal.hann(window_size)
	elif window_type=='triangle':
		window = range(0,window_size/2)+range(window_size/2,-1,-1)
	else:
		raise NameError('Window Type \''+window_type+'\' is not supported!')
	print(window)
	if fft:
		return signal.fftconvolve(sig, window, mode='same') / sum(window)
	return signal.convolve(sig, window, mode='same') / sum(window)