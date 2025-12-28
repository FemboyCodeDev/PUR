import registry



commands = registry.dataset()
#registry.print_dataset(commands)

commands.addData(registry.createCommandChain(name = "echo %x",commands = ["echo {x}"]))
registry.print_dataset(commands)
