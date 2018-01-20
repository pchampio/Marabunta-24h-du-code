from wrapper import Protocol

t, obj = Protocol.readInput()

if t == 'ANT':
	ant = obj
	# ANT PROGRAM
	
elif t == 'NEST':
	nest = obj
	# NEST PROGRAM
	
Protocol.exit()
