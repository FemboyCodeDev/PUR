






content = ""



for x in range(0,64):
	for y in range(0,64):
		row = f"{x}:{y}:x:{x*4}:{y*4}:0"
		content = content+row+"\n"

with open("uv.TWINK","w") as file:
	file.write(content)
