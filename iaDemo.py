from wrapper import Protocol

t, obj = Protocol.readInput()

if t == 'ANT':
	ant = obj
	ant.explorer()
	Protocol.exit()

elif t == 'NEST':
	nest = obj

	if nest.memory[0] == 0:
		nest.setMemoryLocation(0, 1)
		nest.memory()
		nest.newAnt(0)
	elif nest.memory[0] == 1:
		nest.setMemoryLocation(0, 2)
		nest.memory()
		nest.antOut(0, 50, 0, 0)

	Protocol.exit()

Protocol.exit()
