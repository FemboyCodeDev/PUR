


import os
import math
import time
import subprocess
import sys
audioCommand = "pacat --format=u8 --rate=44100 --channels=1"
wrapper = "{content} | {audioCommand}"


audio = []

audio = ([str(int(128+127*math.sin(i*440*2* math.pi /44100))) for i in range(44100)])


def playTone(freq = 440,time = 1):
	samples= int(44100*time)
	content = f"python3 -c 'import sys, math; [sys.stdout.buffer.write(bytes([int(128 + 127 * math.sin(i * {freq} * 2 * math.pi / 44100))])) for i in range({samples})]'"	
	os.system(wrapper.format(content = content,audioCommand = audioCommand))
def playTones(freqs = [440,550,660],timeS = 1):
		samples= int(44100*timeS)
		content = f"python3 -c 'import sys, math; [sys.stdout.buffer.write(bytes([int(128 + 127 * math.sin({time.time()} + (i * freq * 2 * math.pi) / 44100)) for freq in {freqs}])) for i in range({samples})]'"   
		os.system(wrapper.format(content = content,audioCommand = audioCommand))


audio_command = ["pacat", "--format=u8", "--rate=44100", "--channels=1"]
player = subprocess.Popen(audio_command, stdin=subprocess.PIPE)

def get_samples(freqs, duration_s, start_sample_index):
	sample_rate = 44100
	num_samples = int(sample_rate * duration_s)
	buffer = bytearray()
	
	# Define a small fade (e.g., 5ms) to prevent clicks
	fade_len = int(sample_rate * 0.005) 

	for i in range(num_samples):
		current_i = start_sample_index + i
		
		if not freqs:
			buffer.append(128)
			continue
		
		mixed_sine = 0
		for f in freqs:
			mixed_sine += math.sin(2 * math.pi * f * current_i / sample_rate)
		
		# Average the volume
		val_normalized = mixed_sine / len(freqs)
		
		# --- ENVELOPE / FADE LOGIC ---
		# Fade in at start of chunk
		if i < fade_len:
			val_normalized *= (i / fade_len)
		# Fade out at end of chunk
		elif i > (num_samples - fade_len):
			val_normalized *= ((num_samples - i) / fade_len)
		
		# Scale to 0-255 range (u8)
		val = int(128 + (127 * val_normalized))
		buffer.append(val)
	
	return buffer

def loadAudio(file):
	data = {}
	rows = file.split("\n")
	metadata = rows.pop(0).split(":")
	version = metadata[0]
	print(version)
	if version == "0":
		#print("Extracting")
		for row in rows:
			row = row.split(":")
			if len(row) > 2:
				startTime,freq,length = row
				startTime = float(startTime)
				length = float(length)
				if startTime not in data:
					data[startTime] = []
				data[startTime].append({"freq":freq,"length":length,"endtime": startTime+length,"startime":startTime})
	return data

def getPlayingNotes(audio,time):
	notes = []
	for item in audio:
		#print(item)
		#print(audio[item])
		if float(item) <= time:
			#print(item)
			data = audio[item]
			for note in data:
				#print(note)
				if float(note["endtime"]) >= time:
					notes.append({"freq":float(note["freq"])})
	return notes
#playTones()
chunk_duration = 0.08
with open("bad-apple.MEOW") as file:
	audioData = loadAudio(file.read())
#print(audioData)

import time


startTime = time.time()-12
timeElapsed = 0
current_sample_index = 0
while True:
	timeElapsed = time.time()-startTime
	notes = getPlayingNotes(audioData,timeElapsed)
	#print(notes)
	
	# Extract frequency list
	freq_list = [note["freq"] for note in notes]
	# Generate and pipe the bytes
	samples = get_samples(freq_list, chunk_duration, current_sample_index)
	player.stdin.write(samples)
	
	current_sample_index += len(samples)
	#timeElapsed = time.time()-startTime
	

print("done")
