<<<<<<< HEAD
#!/user/bin/env python
=======
  



>>>>>>> parent of e229f76 (Added shebang)
import MRP # Imports the registry system
import EEP
import argparse
EEP.run.commands = MRP.translation.commands
EEP.run.variables = MRP.registry.dataset(name = "Variables")
EEP.run.dataObject = MRP.registry.dataObject
EEP.run.dataClass = MRP.registry.data
#print(MRP.config.version)
#print(MRP.config.shell.template)
if __name__ == "__main__":
	parser = argparse.ArgumentParser(
		description = "PUR: Programmable Utilility Resource"
	)
	parser.add_argument("filename",nargs = "?")
	args = parser.parse_args()
	#print(args)
	if args.filename:
		code = "echo 'testing 123'"
		code = ""
		with open("test.PUR") as file:
			code = file.read()
		EEP.run.run(code)
		MRP.registry.print_dataset(EEP.run.variables)
	else:
		print(MRP.config.shell.template.format(name = MRP.config.name,version = MRP.config.version, device = "Undefined"))
		print('Type "help", "copyright", "credits" or "license()" for more information')
		EEP.run.running = True
		#global EEP.run._lineIndex
		code = []
		while EEP.run.running:
			if EEP.run._lineIndex >= EEP.run._lineIndex:
				line = input(">>>")
				code.append(line)
			try:
				line = code[EEP.run._lineIndex]
				if len("".join(line.split(" "))) > 0:
					EEP.run.runLine(line)
				EEP.run._lineIndex +=1
			except Exception as e:
				print(e)
				EEP.run._lineIndex = len(code)
