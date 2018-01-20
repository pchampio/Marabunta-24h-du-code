import operator
from utils import *
from wrapper import Protocol
# import Protocol

ANT_ECLAIREUR = 0
ANT_RAMASSEUR = 1
PH_NEED_RECHARGE = 30


t, obj = Protocol.readInput()

def antIA(ant):
	# ANT PROGRAM

	if ant.type == ANT_ECLAIREUR:
		idPathStart = ant.m1
		gotFood     = ant.m2

		# NEED STAMINA
		if ant.stamina < STAMINA_NEED_EAT:
			ant.say("ON BOUFFE, ON NEED DE LA STAMINA")
			ant.eat(1)
			return

		phs = ant.arrSeePheromone
		# needRechargePhs = les phs qui sont < PH_NEED_RECHARGE
		nearest = compareKey("area", phs, operator.eq, "NEAR")
		needRefuel = compareKey("persistance", nearest, operator.lt, PH_NEED_RECHARGE)
		if len(needRefuel) >= 0:
			ant.rechargePheromone(needRefuel[0]["id"])
			return

		# nearestPh = la ph la plus proche dans
		
		if nearestPh:
			ant.say("LE PHEROMONE A BESOIN DE SE FAIRE RECHARGER")
			ant.rechargePheromone(nearestPh["id"])
			return

		# farPh = la phs la plus loin
		# HOME RETURN
		if gotFood == True:
			ant.say("ON SE DIRIGE VERS LE CHEMIN DU RETOUR")
			ant.moveTo(farPh["id"])
			idPathStart -= 1
			ant.setMemory(idPathStart, gotFood)
			ant.memory()
			return

		# partie calcul min distance
		# distance = min(SEE_NEST.dist, SEE_PH.dist && SEE_PH.type == idPathStart - 1)
		phs    = compareKey("id", ant.arrSeePheromone, operator.eq, idPathStart - 1)
		phDist = minMaxKey("dist", phs, min)

		nestsFriendly = compareKey("friend", ant.arrSeeNest, operator.eq, "FRIEND")
		nestDist = minMaxKey("dist", nestsFriendly, min)

		distance = min(nestDist, phDist)

		if distance > DISTANCE_NEED_PUT_PH:
			ant.say("ON A BESOIN DE PLACER UN PHEROMONE, ON S ELOIGNE TROP")
			ant.putPheromone(idPathStart)
			idPathStart += 1
			ant.setMemory(idPathStart, gotFood)
			ant.memory()
			return


		if len(ant.arrSeeFood) > 0:
			nearestFoodSrc = ant.arrSeeFood.min()
			
			if nearestFoodSrc == FAR:
				ant.say("ON SE DIRIGE VERS LA BOUFFE")
				ant.moveTo(nearestFoodSrc["id"])

			else:
				ant.say("ON RECUPERE DE LA BOUFFE")
				ant.collect(nearestFoodSrc.id, nearestFoodSrc.amount)
				ant.setMemory(idPathStart, True)
				ant.memory()

			return
		
		ant.say("ON A RIEN TROUVE, ON EXPLORE")
		ant.explore

		return

	elif ant.type == ANT_RAMASSEUR:

		pathID    = ant.m1 # le path qu'on suit
		goingBack = ant.m2 # boolean

		if goingBack == True:

			nests = ant.arrSeeNest()
			if len(nests) >= 0:
				nearestNest = minMaxKey("dist", nests, min)
				
				if nearestNest["area"] == "NEAR":
					ant.say("ON A TROUVE LA NEST, ON RENTRE DEDANS")
					ant.nest(nearestNest["id"])
				else:
					ant.say("ON A TROUVE LA NEST, ON S Y DIRIGE")
					ant.moveTo(nearestNest["id"])
				return

			else:

				pathID -= 1
				ant.setMemory(pathID, goingBack)
				ant.memory()

				destination = ant.arrSeeNest()
				plusLoin    = compareKey("id", destination, operator.eq, pathID)
		

				#if plusLoin["area"] == "NEAR":
				ant.say("ON TROUVE LE CHEMIN")
				ant.moveTo(plusLoin[0]["id"])
				#else:
					

				#ant.moveTo(plusLoin["id"])			
				return

		else:
		
			foods = ant.arrSeeFood()
			if len(foods) >= 0:
				nearestFood = minMaxKey("dist", foods, min)
				
				if nearestFood["area"] == "NEAR":
					ant.say("ON A RECUPERE DE LA BOUFFE")
					ant.collect(nearestFood["id"], nearestFood["amount"])
					ant.setMemory(pathID, True)
					ant.memory()
				else:
					ant.say("ON SE RAPPROCHE DE LA BOUFFE")
					ant.moveTo(nearestFood["id"])

				return

			phs = ant.arrSeePheromone()
			if len(phs) >= 0:
				desiredPh = compareKey("id", phs, operator.eq, pathID)
				ant.moveTo(desiredPh[0]["id"])

				pathID += 1
				ant.setMemory(pathID, goingBack)
				ant.memory()
			else:
				ant.say("ERREUR PAS DE PHEROMONE")
	
			return


		return

	return

def nestIA(nest):
	# NEST PROGRAM

	if nest.memory[0] == 0:
		nest.setMemoryLocation(0, 1)
		nest.memory()
		nest.newAnt(0)

	elif nest.memory[0] == 1:
		nest.setMemoryLocation(0, 2)
		nest.memory()
		nest.antOut(0, 50, 0, 0)	
	

	return

while True:
	nameEntity, entity = Protocol.readInput()
	if nameEntity == 'ANT':
		antIA(entity)
	elif nameEntity == 'NEST':
		nestIA(entity)
	Protocol.exit()
