


def colorise(r,g,b):
	return "\\e[31m"

	return f"\\e[38;2;{r};{g};{b}m"


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
	def addDisplayChar(self,object):
		self.graphics.append(object)
	def addChar(self,x = 0,y = 0,char = " "):
		object = displayChar(x = x, y = y, char = char)
		self.addDisplayChar(object)
	def render(self):
		for sy in range(0,int(self.height/self.fontHeight)):
			row = ""
			for sx in range(0,int(self.width/self.fontWidth)):
				x = sx + self.scrollx
				y = sy + self.scrolly
				row += self.getChar(x=x,y=y)
			print(row)
	def getChar(self,x = 0,y = 0):
		char = " "
		for item in self.graphics:
			if item.atXY(x,y,scroll = (self.scrollx,self.scrolly)):
				char = item.char
		return char



class displayChar:
	def __init__(self,x = 0,y = 0,char  = " "):
		self.x = x
		self.y = y
		self.depth = 0
		self.char = char
		self.color = (255,0,0)
	def getChar(self):
		r,g,b = self.color
		return colorise(r,g,b) + char
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
	for x in range(0,32,1):
		for y in range(0, 32, 1):
			window.addChar(x = x, y = y, char = FullBlock)
	window.render()
