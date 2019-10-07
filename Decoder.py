import numpy as np
import sys

from scipy.io import wavfile


def main(args):
	try:
		samplerate, data = wavfile.read(str(args[1]))
		samples = data.shape[0]
	
	except:
		print("Required sacred file to decode!")
		exit()
	
	holy_message = []
	
	print("Decoding sacred message...\n")
	
	holy_byte = ""
	for bit in range(int(samples / samplerate / 0.1)):
		
		star_point = int(np.floor(samplerate * bit * 0.1))
		end_point = int(np.floor(samplerate * (bit + 1) * 0.1))
		
		# print(data[star_point + 1:end_point])
		
		if np.all(data[star_point:end_point] == 0):
			holy_byte += "0"
			identified_bit = 0
		else:
			holy_byte += "1"
			identified_bit = 1
		
		if (bit + 1) % 8 == 0:
			holy_message.append(holy_byte)
			holy_byte = ""
		# print(holy_byte)
		
		if bit % 8 == 0 and bit != 0:
			print("\n")
		
		print("Bit {} (from {} until {}): {}".format(bit + 1, star_point, end_point, identified_bit))
	
	holy_message = [chr(int(holy_byte, 2)) for holy_byte in holy_message]
	
	print("\nDecoding successful! Praise the Omnissiah:\n")
	
	print("".join(holy_message))


if __name__ == '__main__':
	main(sys.argv)
