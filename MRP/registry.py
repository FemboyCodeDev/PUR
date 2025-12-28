


class dataObject: # The actual data in the dataset
	def __init__(self,type = "None"):
		self.type = type # What type is this object, stored in a string
		self.canHaveData = False # Can this object store other objects
		self.data = [] # This is where all the data objects get stored
		self.rawData = [] # This is where raw data like string data gets stored
	def addData(self,data):
		if self.canHaveData:
			self.data.append(data)

	def getData(self, format = "string"):
		if format == "string":
			return self._getDataString()
	def _getDataString(self):
		if self.type == "None":
			return "Nonetype"
		if self.type == "N/A":
			return "Not Applicable"
		if self.type == "string":
			return "".join([str(x) for x in self.rawData])
		if self.type == "commandChain":
			return ";".join([x._getDataString() for x in self.data])
		if self.type == "command":
			return str(self.rawData[0])

class data:
	def __init__(self,name = "", object = dataObject(type="None")):
		self.object = object
		self.name = name
	def addData(self,data):
		if self.object.canHaveData:
			self.object.addData(data)


def createCommandChain(name = "chain", commands = []): # This defines a command chain, this can be used to execute complex code sequences
	objects = []
	for i, command in enumerate(commands):
		obj = dataObject(type = "command")
		obj.rawData = [ command]
		objects.append(obj)
	obj = dataObject(type = "commandChain")
	obj.data = objects
	return data(name = name,object = obj)

class dataset:
	def __init__(self, name = "Unnamed Dataset"):
		self.data = []
		self.name = name
	def addData(self,data):
		self.data.append(data)





def print_dataset(dataset):
	print(f"Showing Dataset: {dataset.name}")
	for data in dataset.data:
		name = data.name
		data = data.object.getData(format = "string")
		print(f"{name} : {data}")

