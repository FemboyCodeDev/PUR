
import struct

import os
import math
import time
import subprocess
import sys

audio_command = ["pacat", "--format=u8", "--rate=44100", "--channels=1"]
player = subprocess.Popen(audio_command, stdin=subprocess.PIPE)

import time


import wave

with wave.open("bad-apple.wav") as wav_file:
	metadata = wav_file.getparams()
	print(wav_file.getnchannels())
	frames = wav_file.readframes(metadata.nframes)
	sampwidth = metadata.sampwidth
	n_channels = metadata.nchannels
	frames = b''.join([frames[i:i+sampwidth] for i in range(0,len(frames),sampwidth*n_channels)])

format_string = "<" + "h" * (len(frames)//2)
pcm_samples = struct.unpack(format_string,frames)
#print(pcm_samples)
print("normalising")

print("adjusting")

pcm_min = min(pcm_samples)
pcm_samples = [x-pcm_min for x in pcm_samples]
print("scaling")
pcm_max = max(pcm_samples)
pcm_samples = [int((x/pcm_max)*255) for x in pcm_samples]
print("playing")
startTime = time.time()-12
timeElapsed = 0
current_sample_index = 0

print(pcm_samples[1440:1500])
player.stdin.write(bytes(pcm_samples))
"""
while True:
	timeElapsed = time.time()-startTime


	#samples = get_samples(freq_list, chunk_duration, current_sample_index)
	samples = []
	player.stdin.write(samples)
	
	current_sample_index += len(samples)
	#timeElapsed = time.time()-startTime
	
"""
print("done")
