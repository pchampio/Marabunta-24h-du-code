class Nest:

	def __init__(self, ):
		#Protocol.readAnt()


		#self.food
		self.memory = []
		self.arrAntType = []
		self.arrAnt = []


	def __str__(self):
		return "Food : " + str(self.food) + " -- Memory : " + str(self.memory) + " -- AntType : " + str(self.arrAntType) +  " -- Ant : " + str(self.arrAnt) + " --"


	def say(self, msg):
		Protocol.comment(msg)

	## INFORMATION

	def setFood(self, food):
		self.food = food

	def setMemory(self, memory):
		self.memory = memory

	def setMemoryLocation(self, index, memory):
		self.memory[index] = memory

	def setAntCount(self, t, quantity):
		self.arrAntType.append({"type" : t, "quantity" : quantity})

	def setAntIn(self, t, m1, m2):
		self.arrAnt.append({"type" : t, "m1" : m1, "m2" : m2})


	## ACTIONS

	def newAnt(self, t):
		setAntIn(t,0,0)
		print ("ANT_NEW " + str(t))

	def antOut(self, t, food, m0, m1):
		print ("ANT_OUT " + str(t) + " " + str(food) + " " + str(m0) + " " + str(m1))

	def memory(self, memory=self.memory):
		arr = [str(s) for s in memory]
		print ("SET_MEMORY" + " ".join(arr))
