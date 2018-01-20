import sys
from ant import Ant
from nest import Nest
class Protocol:
	MAX_LENGTH = 100 - 3

	@classmethod
	def exit():
		print("END")
		exit()

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
		print(": {}".format(msg), flush=True)

	@classmethod
	def readInput(cls):
		firstLine = sys.stdin.readline()
		name = firstLine.split()[1]
		obj = None
		if name == 'ANT':
			print("readAnt")
			obj = cls.readAnt()
		elif name == 'NEST':
			print("readNest")
			obj = cls.readNest()
		else:
			print("unknown")

		return [name, obj]

		# return data

	@classmethod
	def readAnt(cls):
		cls.comment("reading ant...")
		line = sys.stdin.readline().split()
		ant = Ant()
		while line[0] != 'END':
			cmd = line[0]
			args = line[1:]
			if cmd == 'TYPE':
				t = int(args[0])
				ant.setType(t)

			elif cmd == 'MEMORY':
				m1, m2 = [int(v) for v in args]
				ant.setMemory(m1, m2)

			elif cmd == 'ATTACKED':
				ant.setAttacked()

			elif cmd == 'STAMINA' :
				stamina = int(args[0])
				ant.setStamina(stamina)

			elif cmd == 'STOCK':
				food = int(args[0])
				ant.setFood(food)

			elif cmd == 'SEE_PHEROMONE':
				ident, zone, typePheromone, persistance = args
				ident = int(ident)
				dist = int(dist)
				typePheromone = int(typePheromone)
				persistance = int(persistance)
				ant.setSeePheromone(ident, zone, typePheromone, persistance)

			elif cmd == 'SEE_ANT':
				ident, zone, dist, friend, stamina = args
				ident = int(ident)
				dist = int(dist)
				stamina = int(stamina)
				ant.setSeeAnt(ident, zone, dist, friend)

			elif cmd == 'SEE_NEST':
				ident, zone, dist, friend = args
				ident = int(ident)
				dist = int(dist)
				ant.setSeeNest(ident, zone, dist, friend)

			elif cmd == 'SEE_FOOD':
				print(line)
				ident, zone, dist, amount = args
				ident = int(ident)
				dist = int(dist)
				amount = int(amount)
				ant.setSeeNest(ident, zone, dist, amount)


			line = sys.stdin.readline().split()
		return ant

	@classmethod
	def readNest(cls):
		cls.comment("reading nest...")
		line = sys.stdin.readline().split()
		nest = Nest()
		while line[0] != 'END':
			cmd = line[0]
			args = line[1:]
			if cmd == 'STOCK':
				qtt = args[0]
				qtt = int(qtt)
				nest.setFood(qtt)

			elif cmd == 'MEMORY':
				tab_mem = [int(v) for v in args]
				nest.setMemory(tab_mem)

			elif cmd == 'ANT_COUNT':
				typ, qtt = [int(v) for v in args]
				nest.setMemory(typ, qtt)

			elif cmd == 'ANT_IN':
				typ, m1, m2 = [int(v) for v in args]
				nest.setAntIn(typ, m1, m2)

			line = sys.stdin.readline().split()

		return ant


t, obj = Protocol.readInput()
print(obj)
print(t)
print("ANT_NEW 4")
Protocol.comment("test")
