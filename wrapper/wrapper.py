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

	@staticmethod
	def readInput():
		data = sys.stdin.readlines()
		return data

	@classmethod
	def readAnt(cls):
		data = cls.readInput
		print "Counted", len(data), "lines."






class Ant:
	STAMINA_MAX = 10000
	FOOD_MAX = 1000

	def __init__(self, ):
		# Protocol.readAnt()
		self.char2 = c1
		self.char1 = c2



	def say(self, msg):
		Protocol.comment(msg)


a = Ant()
a.say("hello world and everything")
