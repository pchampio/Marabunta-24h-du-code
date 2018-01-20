# the prod server is not on arch
DEBUG = platform.linux_distribution()[0] == "arch"
def comment(cls, msg):
	if not DEBUG:
		return
	while len(msg) >= 98:
		part1 = msg[0:98]
		msg = msg[98:]
		commentMax(part1)

	commentMax(msg)

def commentMax(cls, msg):
	print(": {}".format(msg))
