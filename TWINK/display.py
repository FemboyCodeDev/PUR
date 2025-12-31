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
		self.height = 256
		self.width = 256
		self.graphics = []
		self.scrollx = 0
		self.scrolly = 0
		self.locationHashes = {}

	def addDisplayChar(self,object):
		self.graphics.append(object)

	def addChar(self,x = 0,y = 0,char = " ", color = (255,0,0)):
		object = displayChar(x = x, y = y, char = char,color = color)
		self.addDisplayChar(object)

		hash = self.calculateHash(x,y)

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
		hash = self.calculateHash(x,y)
		for item in self.locationHashes[hash]:
			if item.atXY(x,y,scroll = (self.scrollx,self.scrolly)):
				char = item.getChar()
		return char



class displayChar:
	def __init__(self,x = 0,y = 0,char  = " ",color = (255,0,0)):
		self.x = x
		self.y = y
		self.depth = 0
		self.char = char
		self.color = color
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


FullBlock = "█"



if __name__  == "__main__":
	window = display()
	for x in range(0,64,1):
		for y in range(0, 64, 1):
			window.addChar(x = x, y = y, char = FullBlock,color = (x*4,y*4,0))
	window.render()
