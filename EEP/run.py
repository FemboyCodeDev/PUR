

import os


data_locations = {}

data_locations["bat.base"] =	"/sys/class/power_supply/BAT0/"
data_locations["bat.percent"]=	"/sys/class/power_supply/BAT0/percent"
data_locations["bat.status"]=	"/sys/class/power_supply/BAT0/status"

commands = None # This gets populated when this library is run by PUR.py


variables = None # This gets replaced with a dataset when the library is run by PUR.py
dataObject = None # This gets replaced with the dataObject class when the library is run by PUR.py
dataClass = None # This gets replaced with the data class when the library is run by PUR.py

internal_functions = ["var","notif","bat.percent","rem","label","proc"]


# ==== Format Function ====
#

def formatFunction(function):
	functionData = []
	for item in function.split(" "):
		if item[0] == "%":
			data = {"input": item[1:]}
		else:
			data = {"command": item}
		functionData.append(data)
	return functionData


def findFunctionInfo(functionData):
	func = functionData.split(" ")[0]

	for item in commands.data: # Where all the objects are stored
		currentFunc = (item.object._getFunction())
		#Compare the two functions to see if the primary executor is the same
		funcOther = currentFunc.split(" ")[0]
		if funcOther == func:
			return item

def reformatRunFunction(funcData,funcIn,funcOut): # Outputs a function (string) that could be run in the shell?
	funcInData = funcIn.split(" ")
	data1 = []
	for item in funcInData:
		if "'" in item:
			data2 = []
			for segment in item.split("'"):
				data2.append("'")
				data2.append(segment)
			data2.pop(0)
			data1.extend(data2)

		else:
			data1.append(item)
	for i in range(len(data1)-1,0,-1):
		if len(data1[i]) == 0:
			data1.pop(i)

	# ==== Variable grouping ======
	# Groups the variable into sections
	# Example:
	#	Foo 'bar' 'fee' -> [bar,fee]
	vars = []
	funcName = data1.pop(0)
	var = ""
	string = False
	for item in data1:
		if "'" in item:
			string = not string
		else:
			var = var+item+" "
		if not string:
			vars.append(var)
			var = ""
	# ==== Variable extraction ====
	# Names the variables and puts them in a dictionary
	inputs = dict({})
	index = 0 # This is the current index of the variable data from funcIn
	for item in funcData:
		if "input" in item:
			inputs[item["input"]] = vars.pop(0)

	# ==== Applies the variables ====
	# TODO: REPLACE THIS
	# THIS CODE IS INCREADIBLY INSECURE AND WILL CAUSE UNWANTED CODE EXECUTION
	# REPLACE THIS PIECE OF SHIT ASAP
	for input in inputs:
		funcOut = inputs[input].join(funcOut.split(f"%{input}%")) 
									# TODO: Fix security vunribility that makes it so that you can 
									# insert new variables and potenstionally other shell code 
									# with variable content
	

	excludes = ["var","label"]
	if funcOut.split(" ")[0] not in excludes:
		func = funcOut
		funcOut = []
		variablePrefixes = ["$"] # TODO: Move this to start of code
		for item in func.split(" "):
			if len(item) > 0:
				if item[0] in variablePrefixes:
					variableName = item
					#print("Variable to replace:", variableName)
					# === Find Variable ===
					for dataPoint in variables.data:
						#print(dataPoint.name)
						if dataPoint.name == variableName:
							funcOut.append(dataPoint.object.getData(format = "string"))
							break
					continue
				else:
					funcOut.append(item) 	# TODO: Make this peice of code more elegant and faster
					continue 		# TODO: Remove the continue call
			funcOut.append(item)
		#print("Debug Spot1:", funcOut)
		funcOut = " ".join(funcOut)
	return funcOut


def runLine(line):
	if line[0] == "#":
		return
	funcInfo = findFunctionInfo(line)
	funcData = formatFunction(funcInfo.name)
	formatedFunction = reformatRunFunction(funcData, line, funcInfo.object._getFunction())
	#print(formatedFunction)
	_executeFormatedFunction(formatedFunction)

def _runOSFunction(function):
	os.system(function)


global _lineIndex
_lineIndex = 0
def run(code):
	global _lineIndex
	lines = code.split("\n")
	i = 0
	while i < len(lines):
		line = lines[i]
		if line != "":
			if False in [x == " " for x in list(line)]:
				_lineIndex = i
				runLine(line)
		i = i+1


def _executeFormatedFunction(function):
	internals = internal_functions # TODO: Remove this shitty line of code
	func = function.split(" ")[0]
	if func in internals:
		_runInternalFunction(function)
	else:
		_runOSFunction(function)
def _runInternalFunction(function):
	func = function.split(" ")[0]
	if func == "var":
		_setVar(function)
	elif func == "notif":
		_sendNotification(function)
	elif func == "bat.percent":
		_getBatPercent(function)
	elif func == "bat.status":
		_getBatStatus(function)
	elif func == "label":
		_setLabel(function)
	else:
		_todoError(f"{func} not implemented")

def _setLabel(function):
	global _lineIndex
	#print(f"{function} {_lineIndex}")
	splitFunction = function.split(" ")
	allowedStarts = ["$"]
	for item in splitFunction:

		if len(item) > 0:
			if item[0] in allowedStarts:
				_setVar(f"var {item} {_lineIndex}")
	#_todoError("Label has not yet been implemented")

# ==== Set variable function ====
# THIS PIECE OF CODE IS AN ABSOLUTE PIECE OF SHIT AND NEEDS REPLACING
def _setVar(function):

	#print(function)
	varName = function.split(" ")[1]
	#print(varName)
	contents = function.split(" ")
	contents.pop(0)
	contents.pop(0)
	#print(contents)
	contents = " ".join(contents)
	#print(contents)

	ObjectType = "NoneType"

	if varName[0] == "$":
		ObjectType = "string"
	else:
		#TODO: Implement variable type not supported error
		pass
	#print(ObjectType)

	if variables is not None:
		object = dataObject(type = ObjectType)
		object.rawData = [contents]
		dataObj = dataClass(name = varName, object = object)
		variables.addData(dataObj)
		#print_dataset(variables)
	#_todoError("Variables setting has not yet been implemented")


def _todoError(text):
	raise NotImplementedError(text)
def _sendNotification(function):
	_todoError("Notifications Not Implemented")
def _getBatPercent(function):
	_todoError("Getting battery percentage is not yet implemented")
def _getBatStatus(function):
	_todoError("Getting battery status is not yet implemented")

if __name__ == "__main__":
	funcData = formatFunction("echo %x")
	print(funcData)

	funcToRun = "echo 'Hello World'"
	reformatRunFunction(funcData,funcToRun,"echo %x%")

