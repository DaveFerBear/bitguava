from scipy import signal
import numpy as np

def smooth_convolution(time_series, window_type='hann', window_size=10):
	window = [1] #Unit Impluse
	if window_type=='hann':
		window = signal.hann(window_size)
	elif window_type=='triangle':
		window = range(0,window_size/2)+range(window_size/2,-1,-1)
	else:
		raise NameError('Window Type \''+window_type+'\' is not supported!')
	print(window)
	return signal.convolve(sig, window, mode='same') / sum(window)

smooth_convolution([x for x in range(100)], 'triangle', window_size=2)
