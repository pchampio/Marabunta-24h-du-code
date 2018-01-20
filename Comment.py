# the prod server is not on arch
import platform
DEBUG = platform.linux_distribution()[0] == "arch"
def comment(msg):
	if not DEBUG:
		return
	while len(msg) >= 90:
		part1 = msg[0:90]
		msg = msg[90:]
		commentMax(part1)

	commentMax(msg)

def commentMax(msg):
	print(": {}".format(msg))
