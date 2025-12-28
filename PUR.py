



import MRP # Imports the registry system
import EEP



EEP.run.commands = MRP.translation.commands






if __name__ == "__main__":
	code = "echo 'testing 123'"
	code = ""
	with open("test.PUR") as file:
		code = file.read()
	EEP.run.run(code)
