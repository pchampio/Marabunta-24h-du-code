NO_DEBUG = True

def comment(cls, msg):
	if NO_DEBUG:
		return
	while len(msg) >= 98:
		part1 = msg[0:98]
		msg = msg[98:]
		commentMax(part1)

	commentMax(msg)

def commentMax(cls, msg):
	print(": {}".format(msg))
