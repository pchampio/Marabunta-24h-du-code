# the prod server is not on arch
import platform
DEBUG = platform.linux_distribution()[0] == "arch"
DEBUG = False

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def comment(msg):
	if not DEBUG:
		return
	while len(msg) >= 80:
		part1 = msg[0:80]
		msg = msg[80:]
		commentMax(part1)

	commentMax(msg)

def commentMax(msg):
	print(": " + bcolors.FAIL + "{}".format(msg) + bcolors.ENDC)
