
try:
	import MRP.registry as registry
except Exception:
	import registry


commands = registry.dataset()
#registry.print_dataset(commands)


commands.addData(registry.createCommandChain(name = "echo %x",commands = ["echo %x%"]))
commands.addData(registry.createCommandChain(name = "var %x %= %y",commands = ["var %x% %y%"]))


if __name__ == "__main__":
	registry.print_dataset(commands)
