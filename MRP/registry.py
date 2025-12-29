


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
		if self.type == "procedure":
			return f"Procedure: {self.data[0].object._getDataString()} -> {self.data[1].object._getDataString()}"
	def _getFunction(self):
		if self.type in ["command"]:
			return str(self.rawData[0])
		elif self.type in ["commandChain"]:
			if len(self.data) == 1:
				return self.data[0]._getFunction()
			else:
				raise TypeError("This is command chain, and not a command, you cannot just get the function inside of it")
		else:
			raise TypeError(f"This is a {self.type} and this function cannot be run on it")

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


def createProcedure(name = "procedure",startName = "None",endName= "None"):
	startObject = None
	endObject = None
	allowedTypes = ["linePointer"]
	procedureObject = dataObject(type = "procedure")
	for data in dataset.data:
		if data.name in [startName,endName]:
			if data.object.type in allowedTypes:
				targetObject = data
			else:
				print("Object of type {data.object.type} is not allowed") # TODO: Make it display allowed types
				continue
			if data.name == startName:
				startObject = data
			elif data.name == endName:
				endObject = data
			else:
				raise Exception
	procedureObject.addData(startObject)
	procedureObject.addData(endObject)
	return data(name = name, object = procedureObject)
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

