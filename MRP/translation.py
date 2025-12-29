
try:
	import MRP.registry as registry
except Exception:
	import registry


commands = registry.dataset()
#registry.print_dataset(commands)



# ==== OS commands ====

commands.addData(registry.createCommandChain(name = "echo %x",commands = ["echo %x%"]))
commands.addData(registry.createCommandChain(name = "beep %x",commands = ['echo -e "\a"'])) # This may not work at all, but it definetely wont work on windows


# ==== Internal commands ====

commands.addData(registry.createCommandChain(name = "var %x %= %y",commands = ["var %x% %y%"]))
commands.addData(registry.createCommandChain(name = "bat.percentage %x", commands = ["bat.percentage %x"]))
commands.addData(registry.createCommandChain(name = "goto %x", commands = ["goto %x%"])) # Goes to line in variable %x
commands.addData(registry.createCommandChain(name = "label %x", commands = ["label %x%"])) # Stores the line in variable %x
commands.addData(registry.createCommandChain(name = "proc %x %y %z", commands = ["proc %x %y %z"])) 	# Defines a procedure between the lines stored in
													# variable %x and variable %y


# ==== Comment commands ===

commands.addData(registry.createCommandChain(name = "rem %x", commands = ["rem %x"]))
commands.addData(registry.createCommandChain(name = "# %x", commands = ["rem %x"]))


if __name__ == "__main__":
	registry.print_dataset(commands)
