import sys

class Protocol:
	MAX_LENGTH = 100 - 2


	# @staticmethod
	@classmethod
	def comment(cls, msg):
		while len(msg) >= cls.MAX_LENGTH:
			part1 = msg[0:cls.MAX_LENGTH]
			msg = msg[cls.MAX_LENGTH:]
			cls.commentMax(part1)

		cls.commentMax(msg)

	@classmethod
	def commentMax(cls, msg):
		print(":{}".format(msg))

	@classmethod
	def readInput(cls):
		data = sys.stdin.readlines()
		name = data[0].split()[1]
		obj = None
		if name == 'ANT':
			print("readAnt")
			obj = cls.readAnt(data[1:])
		elif name == 'NEST':
			print("readNest")
			obj = cls.readNest(data[1:])
		else:
			print("unknown")

		return [name, obj]

		# return data

	@classmethod
	def readAnt(cls, data):
		print("reading ant...")


	@classmethod
	def readNest(cls, data):
		print("reading nest...")




# a = Ant()
# a.say("hello world and everything")


t, obj = Protocol.readInput()
print(obj)
print(t)
