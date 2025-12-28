

import os


data_locations = {}

data_locations["bat.base"] =	"/sys/class/power_supply/BAT0/"
data_locations["bat.percent"]=	"/sys/class/power_supply/BAT0/percent"
data_locations["bat.status"]=	"/sys/class/power_supply/BAT0/status"

commands = None # This gets populated when this library is run by PUR.py



internal_functions = ["var","notif","bat.percent"]


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
	return funcOut


def runLine(line):
	funcInfo = findFunctionInfo(line)
	funcData = formatFunction(funcInfo.name)
	formatedFunction = reformatRunFunction(funcData, line, funcInfo.object._getFunction())
	_executeFormatedFunction(formatedFunction)

def _runOSFunction(function):
	os.system(function)


def run(code):
	lines = code.split("\n")
	i = 0
	while i < len(lines):
		line = lines[i]
		if line != "":
			if False in [x == " " for x in list(line)]:
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


def _setVar(function):
	_todoError("Variables setting has not yet been implemented")
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

