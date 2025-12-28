



import MRP # Imports the registry system
import EEP



EEP.run.commands = MRP.translation.commands
EEP.run.variables = MRP.registry.dataset(name = "Variables")
EEP.run.dataObject = MRP.registry.dataObject
EEP.run.dataClass = MRP.registry.data




if __name__ == "__main__":
	code = "echo 'testing 123'"
	code = ""
	with open("test.PUR") as file:
		code = file.read()
	EEP.run.run(code)
	#MRP.registry.print_dataset(EEP.run.variables)
