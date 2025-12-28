



def formatFunction(function):
	functionData = []
	for item in function.split(" "):
		if item[0] == "%":
			data = {"input": item[1:]}
		else:
			data = {"command": item}
		functionData.append(data)
	return functionData



def reformatRunFunction(funcData,funcIn,funcOut):
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
	print(data1)
	for i in range(len(data1)-1,0,-1):
		print(data1[i],i)
		if len(data1[i]) == 0:
			data1.pop(i)
	print("".join(data1),data1)
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
	print(vars)
	inputs = dict({})
	index = 0 # This is the current index of the variable data from funcIn
	for item in funcData:
		print(item)
		if "input" in item:
			print(item["input"])
			inputs[item["input"]] = vars.pop(0)
	print(inputs)
	for input in inputs:
		print(input)
		funcOut = inputs[input].join(funcOut.split(f"%{input}%")) 
									# TODO: Fix security vunribility that makes it so that you can 
									# insert new variables and potenstionally other shell code 
									# with variable content
	print(funcOut)

if __name__ == "__main__":
	funcData = formatFunction("echo %x")
	print(funcData)

	funcToRun = "echo 'Hello World'"
	reformatRunFunction(funcData,funcToRun,"echo %x%")

