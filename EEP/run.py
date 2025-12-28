

import os




commands = None # This gets populated when this library is run by PUR.py

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
	#print(func)

	for item in commands.data: # Where all the objects are stored
		#print(item.name, type(item))
		currentFunc = (item.object._getFunction())
		#print(currentFunc,func)
		#Compare the two functions to see if the primary executor is the same
		funcOther = currentFunc.split(" ")[0]
		if funcOther == func:
			#print("Found Function")
			return item

def reformatRunFunction(funcData,funcIn,funcOut): # Outputs a function that could be run in the shell?
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
	#print(data1)
	for i in range(len(data1)-1,0,-1):
		#print(data1[i],i)
		if len(data1[i]) == 0:
			data1.pop(i)
	#print("".join(data1),data1)
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
	#print(vars)
	inputs = dict({})
	index = 0 # This is the current index of the variable data from funcIn
	for item in funcData:
		#print(item)
		if "input" in item:
			#print(item["input"])
			inputs[item["input"]] = vars.pop(0)
	#print(inputs)
	for input in inputs:
		#print(input)
		funcOut = inputs[input].join(funcOut.split(f"%{input}%")) 
									# TODO: Fix security vunribility that makes it so that you can 
									# insert new variables and potenstionally other shell code 
									# with variable content
	#print(funcOut)
	return funcOut


def runLine(line):
	funcInfo = findFunctionInfo(line)
	#print(funcInfo)
	funcData = formatFunction(funcInfo.name)
	#print(funcData)
	formatedFunction = reformatRunFunction(funcData, line, funcInfo.object._getFunction())
	#print("result", formatedFunction)
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
				print(line)
				runLine(line)
		i = i+1
def _executeFormatedFunction(function):
	internals = ["var","notif","bat.percent"]
	func = function.split(" ")[0]
	if func in internals:
		_runInternalFunction(function)
	else:
		_runOSFunction(function)



if __name__ == "__main__":
	funcData = formatFunction("echo %x")
	print(funcData)

	funcToRun = "echo 'Hello World'"
	reformatRunFunction(funcData,funcToRun,"echo %x%")

