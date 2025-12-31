#


def colorise(r,g,b):
#	return "\\e[31m"

	return f"\x1b[38;2;{r};{g};{b}m"




hashingPrimes = [4657,2347]



class display:
	def __init__(self):
		self.fontHeight = 14
		self.fontHeight = 8	

		self.fontWidth = 7
		self.fontWidth = 8
		self.height = 512
		self.width = 512
		self.graphics = []
		self.scrollx = 0
		self.scrolly = 0
		self.locationHashes = {}

	def addDisplayChar(self,object):
		self.graphics.append(object)

	def addChar(self,x = 0,y = 0,char = " ", color = (255,0,0)):
		object = displayChar(x = x, y = y, char = char,color = color)
		self.addDisplayChar(object)
		self.addObjectToHash(x,y,object)
	
	def addObjectToHash(self,x,y,object):
		#print(hash)
		hash = self.calculateHash(x,y)
		#print(hash)
		if hash not in self.locationHashes:
			self.locationHashes[hash] = []

		self.locationHashes[hash].append(object)

	def calculateHash(self,x,y):
		hash = x*hashingPrimes[0]+y*hashingPrimes[1]
		return hash
	def render(self):
		content = ""
		for sy in range(0,int(self.height/self.fontHeight)):
			row = ""
			for sx in range(0,int(self.width/self.fontWidth)):
				x = sx + self.scrollx
				y = sy + self.scrolly
				row += self.getChar(x=x,y=y)
			#print(row)
			content += row+ "\n"
		print(content)
	def getChar(self,x = 0,y = 0):
		char = " "
		currentDepth = None
		hash = self.calculateHash(x,y)
		#print(hash)
		if hash in self.locationHashes:
			for item in self.locationHashes[hash]:
				print(item)
				if item.atXY(x,y,scroll = (self.scrollx,self.scrolly)):
					if currentDepth == None:
						currentDepth = item.depth - 1
					if not item.depth < currentDepth:
						char = item.getChar()
						currentDepth = item.depth
		return char




class displayChar:
	def __init__(self,x = 0,y = 0,char  = " ",color = (255,0,0)):
		self.x = x
		self.y = y
		self.depth = 0
		self.char = char
		self.color = color
		self.controlId = "world"
	def getChar(self):
		r,g,b = self.color
		return colorise(r,g,b) +self. char
	def getXY(self,scroll = (0,0)):
		return self.x,self.y
	def atXY(self,x,y,scroll = (0,0)):
		selfx,selfy = self.getXY(scroll = scroll)
		#print(selfx,selfy,x,y)
		if selfx == x:
			if selfy == y:
				return True
		return False




def loadImage(data,window):
	objects = []
	for row in data.split("\n"):
		x,y,char,r,g,b = 0,0," ",255,0,0
		row = row.split(":")
		if len(row) > 0:
			if len(row) > 2:
				x,y,char = row[0],row[1],row[2]
				#print(x,y,char)
				if len(row) > 3:
					r,g,b = row[3],row[3],row[3]
					if len(row) > 5:
						r,g,b = row[3],row[4],row[5]
				#print(x,y,char,r,g,b)

				object = displayChar(x=int(x),y=int(y),char=char,color=(int(r),int(g),int(b)))
				object.depth = 10
				window.addDisplayChar(object)
				window.addObjectToHash(int(x),int(y),object)				



FullBlock = "█"



if __name__  == "__main__":
	window = display()
	for x in range(0,128,1):
		for y in range(0, 128, 1):
			pass
			#window.addChar(x = x, y = y, char = FullBlock,color = (x*2,y*2,0))


	with open("img.TWINK") as file:
		loadImage(file.read(),window)
	window.render()
