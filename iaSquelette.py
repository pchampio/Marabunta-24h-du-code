from wrapper import Protocol


def antIA(ant):
	# ANT PROGRAM

def nestIA(nest):
	# NEST PROGRAM

while True:
	nameEntity, entity = Protocol.readInput()
	if nameEntity == 'ANT':
		antIA(entity)
	elif nameEntity == 'NEST':
		nestIA(entity)
	Protocol.exit()
