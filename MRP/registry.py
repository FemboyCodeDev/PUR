


class dataObject:
	def __init__(self,type = "None"):
		self.type = type # What type is this object, stored in a string
		self.canHaveData = False # Can this object store other objects
		self.data = [] # This is where all the data objects get stored
	def addData(self,data):
		if self.canHaveData:
			self.data.append(data)



class data:
	def __init__(self,name = "", object = dataObject(type="None"):
		self.object = object
	def addData(self,data):
		if self.object.canHaveData:
			self.object.addData(data)



class dataset:
	def __init__(self):
		self.data = []
	def addData(self,data):
		self.data.append(data)


