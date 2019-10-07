import winsound
import time
import sys
from tqdm import tqdm
import math
import wave
import struct

# Audio will contain a long list of samples (i.e. floating point numbers describing the
# waveform).  If you were working with a very long sound you'd want to stream this to
# disk instead of buffering it all in memory list this.  But most sounds will fit in
# memory.
audio = []
sample_rate = 44100.0


def encode(input_text):
	return ['{0:08b}'.format(ord(x), 'b') for x in input_text]


def transfer_holy_information(holy_input):
	frequency = 500
	duration = 250
	
	print("\nHoly information to transfer: \n")
	print(" ".join(holy_input))
	
	print("\nHoly broadcast started: \n")
	
	for holy_byte in tqdm(holy_input):
		for holy_bit in holy_byte:
			if bool(int(holy_bit)):
				winsound.Beep(frequency, duration)
			else:
				time.sleep(duration / 1000)
		
		time.sleep(duration / 1000)
	
	print("\nHoly broadcast ended")


def transfer_holy_information_v2(holy_input, file_name):
	duration = 100
	
	print("\nHoly information to transfer: \n")
	print(" ".join(holy_input))
	
	print("\nHoly broadcast started: \n")
	
	for holy_byte in tqdm(holy_input):
		for holy_bit in holy_byte:
			if bool(int(holy_bit)):
				# print(holy_bit)
				append_sinewave(volume=1, duration_milliseconds=duration)
			else:
				append_silence(duration)
		
		# append_silence(duration)
	
	save_wav(file_name)
	
	print("\nHoly broadcast ended")


def append_silence(duration_milliseconds):

	num_samples = duration_milliseconds * (sample_rate / 1000.0)
	
	for x in range(int(num_samples)):
		audio.append(0.0)
	
	return


def append_sinewave(
		freq=440.0,
		duration_milliseconds=200,
		volume=1.0):
	global audio  # using global variables isn't cool.
	
	num_samples = duration_milliseconds * (sample_rate / 1000.0)
	
	for x in range(int(num_samples)):
		audio.append(volume * math.sin(2 * math.pi * freq * (x / sample_rate)))
	
	return


def save_wav(file_name):
	# Open up a wav file
	wav_file = wave.open(file_name, "w")
	
	# wav params
	nchannels = 1
	
	sampwidth = 2
	
	# 44100 is the industry standard sample rate - CD quality.  If you need to
	# save on file size you can adjust it downwards. The stanard for low quality
	# is 8000 or 8kHz.
	nframes = len(audio)
	comptype = "NONE"
	compname = "not compressed"
	wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))
	
	# WAV files here are using short, 16 bit, signed integers for the
	# sample size.  So we multiply the floating point data we have by 32767, the
	# maximum value for a short integer.  NOTE: It is theortically possible to
	# use the floating point -1.0 to 1.0 data directly in a WAV file but not
	# obvious how to do that using the wave module in python.
	for sample in tqdm(audio):
		wav_file.writeframes(struct.pack('h', int(sample * 32767.0)))
	
	wav_file.close()
	
	return


def main(args):
	try:
		file_name = str(args[1])
	except:
		print("Saving the sacred message as output.wav")
		file_name = "output.wav"
	
	try:
		input_string = str(args[2])
	except:
		print("No input to encode. Using the default prayer to the Omnissiah!\n")
		
		input_string = "Omnissiah, which art in this machine, Hallowed be thy Name." \
		               " Thy capacitors fill. Thy logic be true in this function," \
		               " As it is in others. I give thee this day thine daily maintenance." \
		               " Forgive us our illogical or recursive arguments, As we forgive poorly written error messages." \
		               " And lead us not into disrepair, But deliver us from evil. For thine is the processor," \
		               " The power, and the microchip, For ever and ever. Amen."
		
	transfer_holy_information_v2(encode(input_string), file_name)

# transfer_holy_information(encode(input_string))


if __name__ == '__main__':
	main(sys.argv)
