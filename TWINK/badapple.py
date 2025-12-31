

import display
import time
import os
import sys





window = display.display()



files = ["uv.TWINK"]


frames = {}
for item in sorted(os.listdir("badapple")):
	#print(item)
	frameNo = item.split("_")[-1]
	frameNo = frameNo.split(".")[0]
	#print(frameNo)
	frames[int(frameNo)] = os.path.join("badapple",item)
for index in sorted(frames):
	print(index)
	files.append(frames[index])




for i in range(1,0,-1):
	print(i)
	time.sleep(1)



fps = 30
timePerFrame = 1/fps
videoStartTime = time.time()
currentIndex = 0
while currentIndex < len(files):
	currentIndex = int ((time.time()-videoStartTime)*fps)
	file = files[currentIndex]
	
	startTime = time.time()
	#os.system("clear")
	time.sleep(1/12)
	window.locationHashes = {}
	window.graphics = []
	with open(file,encoding = "utf-8") as f:
		display.loadImage(f.read(),window)
	
	window.render()
	
	endTime = time.time()
	timetaken = endTime-startTime
	extraTime = timePerFrame-timetaken
	#print(f"Took {timetaken}")
	#print(f"Running at {1/timetaken}")
	#print(f"Extra time {extraTime}")
	
