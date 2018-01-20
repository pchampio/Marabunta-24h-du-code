from wrapper import Protocol


def antIA(ant):
	# ANT PROGRAM
	return

def nestIA(ant):
	# NEST PROGRAM
	return

while True:
	nameEntity, entity = Protocol.readInput()
	if nameEntity == 'ANT':
		antIA(entity)
	elif nameEntity == 'NEST':
		nestIA(entity)
	Protocol.exit()
