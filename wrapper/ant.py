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
		return "m1 : " + self.m1 + "\nm2 : " + self.m2 + "\ntype : " + self.type + "\nstamina : " + self.stamina + "\nfood : " + self.food + "\nisAttacked? : " + self.isAttacked + "\nsee Pheromone : " + self.arrSeePheromone + "\nsee Ant : " + self.arrSeeAnt + "\nSee Nest : " + self.arrSeeNest + "\nSee Food : " + self.arrSeeFood + "\n"  



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
