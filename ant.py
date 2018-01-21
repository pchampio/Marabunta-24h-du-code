from Comment import comment

class Ant:
	STAMINA_MAX = 10000
	FOOD_MAX = 1000


	def say(self, msg):
		comment(msg)

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

	def setSeePheromone(self, uniq, area, dist, type2, persistance):
                self.arrSeePheromone.append({"id": uniq, "area" : area, "dist" : dist, "persistance" : persistance, "type": type2})

	def setSeeAnt(self, uniq, area, dist, friend, stamina):
		self.arrSeeAnt.append({"id": uniq, "area" : area, "dist" : dist, "friend" : friend, "stamina" : stamina})

	def setSeeNest(self, uniq, area, dist, friend):
		self.arrSeeNest.append({"id" : uniq, "area" : area, "dist" : dist, "friend" : friend})

	def setSeeFood(self, uniq, area, dist, amount):
		self.arrSeeFood.append({"id" : uniq, "area" : area, "dist" : dist, "amount" : amount})

	## Actions

	def explore(self):
		if self.requireStamina(1) == False: return

		print ("EXPLORE")


	def turn(self, angle):
		if angle < -180 or angle > 180:
			self.say("ERROR: ANGLE MUST BETWEEN -180 and 180")
			return
		if self.requireStamina(1) == False: return

		print ("TURN " + str(angle))

	def moveTo(self, uniq):
		if self.requireStamina(2) == False: return
		print ("MOVE_TO " + str(uniq))

	def putPheromone(self, t):
		if not 0 <= t <= 1023:
			self.say("ERROR: PHEROMONE TYPE SHOULD BE IN [0, 1023], CURRENTLY " + str(t))
			return
		if self.requireStamina(3) == False: return

		print ("PUT_PHEROMONE " + str(t))

	def changePheromone(self, uniq, t):
		pheromone = [x for x in self.arrSeePheromone if x["id"] == uniq]
		if not pheromone:
			self.say("ERROR: PHEROMONE " + str(uniq) + " NOT FOUND")
			return
		if pheromone[0]["area"] != "NEAR":
			self.say("ERROR: PHEROMONE " + str(uniq) + " IS NOT NEAR THE ANT")
			return
		if not 0 <= t <= 1023:
			self.say("ERROR: PHEROMONE TYPE SHOULD BE IN [0, 1023], CURRENTLY " + str(t))
			return
		if self.requireStamina(2) == False: return

		print ("CHANGE_PHEROMONE " + str(uniq) + " " + str(t))

	def rechargePheromone(self, uniq):
		pheromone = [x for x in self.arrSeePheromone if x["id"] == uniq]
		if not pheromone:
			self.say("ERROR: PHEROMONE " + str(uniq) + " NOT FOUND")
			return
		if pheromone[0]["area"] != "NEAR":
			self.say("ERROR: PHEROMONE " + str(uniq) + " IS NOT NEAR THE ANT")
			return
		if self.requireStamina(1) == False: return

		print ("RECHARGE_PHEROMONE " + str(uniq))

	def collect(self, uniq, quantity):
		food = [x for x in self.arrSeeFood if x["id"] == uniq]
		if not food:
			self.say("ERROR: FOOD " + str(uniq) + " NOT FOUD")
			return
		if quantity <= 0:
			self.say("ERROR: FOOD QUANTITY TO COLLECT CANNOT BE <= 0")
			return
		if self.requireStamina(4) == False: return

		print ("COLLECT " + str(uniq) + " " + str(quantity))

	def doTropha(self, uniq, quantity):
		ant = [x for x in self.arrSeeAnt if x["id"] == uniq]
		if not ant:
			self.say("ERROR: " + str(uniq) + " NOT FOUND")
			return
		if ant[0]["area"] != "NEAR":
			self.say("ERROR: " + str(uniq) + " NOT NEAR THE ANT")
			return
		if quantity <= 0 or quantity >= self.food:
			self.say("ERROR: NOT ENOUGH FOOD (" + str(self.food) + ") TO GIVE " + str(quantity))
			return
		if self.requireStamina(quantity) == False: return
		print ("DO_THROPHALLAXIS " + str(uniq) + " " + str(quantity))

	def eat(self, quantity):
		if quantity > self.food:
			self.say("ERROR: NOT ENOUGH FOOD TO EAT " + str(quantity) + " WITH " + str(self.food) + " FOOD")
			return
		print ("EAT " + str(quantity))

	def nest(self, uniq):
		dest = [x for x in self.arrSeeNest if x["id"] == uniq]
		if not dest:
			self.say("ERROR: " + str(uniq) + " NOT FOUND IN NESTS AROUND ANT")
			return
		if dest[0]["area"] != "NEAR":
			self.say("ERROR: " + str(uniq) + " NOT NEAR THE ANT")
			return
		if dest[0]["friend"] != "FRIEND":
			self.say("ERROR: " + str(uniq) + " NOT FRIEND WITH THE ANT")
			return
		if self.requireStamina(2) == False: return

		print ("NEST " + str(uniq))

	def attack(self, uniq, strength):
		target = [x for x in self.arrSeeAnt if x["id"] == uniq]

		if not target:
			self.say("ERROR: TARGET " + str(uniq) + " NOT FOUND")
			return
		if target[0]["area"] != "NEAR":
			self.say("ERROR: TARGET " + str(uniq) + " NOT NEAR THE ANT")
			return
		if target[0]["friend"] == "FRIEND":
			self.say("ERROR: TRYING TO ATTACK A FRIEND ANT " + str(uniq) + " CANCELS")
			return
		if strength > 5 or strength < 1:
			self.say("ERROR: TRYING TO HURT WITH A STREGTH NOT IN [1,5], WITH " + str(strength))
			return
		if self.requireStamina(strength) == False: return

		print ("ATTACK " + str(uniq) + " " + str(strength))

	def suicide(self):
		print ("SUICIDE")

	def commitMemory(self):
		print ("SET_MEMORY " + str(self.m1) + " " + str(self.m2))

	def requireStamina(self, neededStamina):
		# print error if not enough stamina, return false in this case
		# return True if enough stamina, does not print anything
		if self.stamina < neededStamina:
			self.say("ERROR: NOT ENOUGH STAMINA, I HAVE " + self.stamina + " NEEDS " + neededStamina)
			return False
		return True
