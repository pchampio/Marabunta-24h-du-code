from wrapper import Protocol

t, obj = Protocol.readInput()

if t == 'ANT':
	ant = obj
	ant.explorer()
	Protocol.exit()

elif t == 'NEST':
	nest = obj
	#nest.newAnt(0)
	Protocol.exit()

Protocol.exit()
