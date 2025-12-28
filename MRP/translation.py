
try:
	import MRP.registry as registry
except Exception:
	import registry


commands = registry.dataset()
#registry.print_dataset(commands)



# ==== OS commands ====

commands.addData(registry.createCommandChain(name = "echo %x",commands = ["echo %x%"]))



# ==== Internal commands ====

commands.addData(registry.createCommandChain(name = "var %x %= %y",commands = ["var %x% %y%"]))
commands.addData(registry.createCommandChain(name = "bat.percentage %x", commands = ["bat.percentage %x"]))


# ==== Comment commands ===

commands.addData(registry.createCommandChain(name = "rem %x", commands = ["rem %x"]))
commands.addData(registry.createCommandChain(name = "# %x", commands = ["rem %x"]))


if __name__ == "__main__":
	registry.print_dataset(commands)
