class Ant:
	STAMINA_MAX = 10000
	FOOD_MAX = 1000


	def say(self, msg):
		Protocol.comment(msg)

	def __init__(self):
		#self.m1
		#self.m2
		#self.stamina
		#self.type
		#self.food
		self.isAttacked = False
		self.arrSeePheromone = []
		self.arrSeeAnt = []
		self.arrSeeNest = []
		self.arrSeeFood = []

	def __str__(self):
		return "m1 : " + str(self.m1) + " -- 2 : " + str(self.m2) + " -- type : " + str(self.type) + " -- stamina : " + str(self.stamina) + " -- food : " + str(self.food) + " -- isAttacked? : " + str(self.isAttacked) + " -- see Pheromone : " + str(self.arrSeePheromone) + " -- see Ant : " + str(self.arrSeeAnt) + " -- See Nest : " + str(self.arrSeeNest) + " -- See Food : " + str(self.arrSeeFood)

	## Informations

	def setType(self, t):
		self.type = t

	def setMemory(self, m1, m2):
		self.m1 = m1
		self.m2 = m2

	def setAttacked(self):
		self.isAttacked = True

	def setStamina(self, quantity):
		self.stamina = quantity

	def setFood(self, quantity):
		self.food = quantity

	def setSeePheromone(self, uniq, area, dist, persistance):
		self.arrSeePheromone.append({"id": uniq, "area" : area, "dist" : dist, "persistance" : persistance})

	def setSeeAnt(self, uniq, area, dist, friend, stamina):
		self.arrSeeAnt.append({"id": uniq, "area" : area, "dist" : dist, "friend" : friend, "stamina" : stamina})

	def setSeeNest(self, uniq, area, dist, friend):
		self.arrSeeNest.append({"id" : uniq, "area" : area, "dist" : dist, "friend" : friend})

	def setSeeFood(self, uniq, area, dist, amount):
		self.arrSeeFood.append({"id" : uniq, "area" : area, "dist" : dist, "amount" : amount})

	## Actions

	def explore(self):
		print ("EXPLORE")

	def turn(self, angle):
		print ("TURN " + str(angle))

	def moveTo(self, uniq):
		print ("MOVE_TO " + str(uniq) )

	def putPheromone(self, t):
		print ("PUT_PHEROMONE " + str(type))

	def changePheromone(self, uniq, t):
		print ("CHANGE_PHEROMONE " + str(uniq) + " " + str(t))

	def rechargePheromone(self, uniq):
		print ("RECHARGE_PHEROMONE " + str(uniq))

	def collect(self, uniq, quantity):
		print ("COLLECT " + str(uniq) + " " + str(quantity))

	def doTropha(self, uniq, quantity):
		print ("DO_THROPHALLAXIS " + str(uniq) + " " + str(quantity))

	def eat(self, quantity):
		print ("EAT " + str(quantity))

	def nest(self, uniq):
		print ("NEST " + str(uniq))

	def attack(self, uniq, strength):
		print ("ATTACK " + str(uniq) + " " + str(strength))

	def suicide(self):
		print ("SUICIDE")

	def memory(self):
		print ("SET_MEMORY " + str(self.m0) + " " + str(self.m1))
