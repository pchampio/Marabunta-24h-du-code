import operator
from utils import *
from wrapper import Protocol
from Comment import comment
import time

# import Protocol

ANT_ECLAIREUR = 0
ANT_RAMASSEUR = 1
PH_NEED_RECHARGE = 30
STAMINA_NEED_EAT = 100
DISTANCE_NEED_PUT_PH = 90


def antIA(ant):
	# ANT PROGRAM

	#  time.sleep(1)

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
		if len(needRefuel) > 0:
			ant.say("LE PHEROMONE A BESOIN DE SE FAIRE RECHARGER")
			ant.rechargePheromone(needRefuel[0]["id"])
			return

		# farPh = la phs la plus loin
		# HOME RETURN
		if gotFood == True:
			ant.say("ON SE DIRIGE VERS LE CHEMIN DU RETOUR")
			ant.moveTo(farPh["id"])
			idPathStart -= 1
			ant.setMemory(idPathStart, gotFood)
			ant.commitMemory()
			return

		# partie calcul min distance
		ant.say("test")
		phs    = compareKey("type", ant.arrSeePheromone, operator.eq, idPathStart)

		nestsFriendly = compareKey("friend", ant.arrSeeNest, operator.eq, "FRIEND")
		#  ant.say("nestsFriendly" + str(nestsFriendly))
		#  ant.say("phs" + str(phs))
		#  ant.say("idPathStart" + str(idPathStart))
		#  ant.say("arrSeePheromone" + str(ant.arrSeePheromone))

		if nestsFriendly and phs:
			phDist = minMaxKey("dist", phs, min)
			nestDist = minMaxKey("dist", nestsFriendly, min)
                        ant.say("pierre" + )

			distance = min(nestDist, phDist)

			if distance["dist"] > DISTANCE_NEED_PUT_PH:
				ant.say("ON A BESOIN DE PLACER UN PHEROMONE, ON S ELOIGNE TROP 2")
				ant.putPheromone(idPathStart)
				ant.setMemory(idPathStart, gotFood)
				ant.commitMemory()
				return
		if phs:
			distance = minMaxKey("dist", phs, min)

			if distance["dist"] > DISTANCE_NEED_PUT_PH:
				ant.say("ON A BESOIN DE PLACER UN PHEROMONE, ON S ELOIGNE TROP phs")
				ant.putPheromone(idPathStart)
				idPathStart += 1
				ant.setMemory(idPathStart, gotFood)
				ant.commitMemory()
				return

		ant.say("dsfs" + str(len(phs)))
		if nestsFriendly and len(phs) == 0:
			distance = minMaxKey("dist", nestsFriendly, min)

			if distance["dist"] > DISTANCE_NEED_PUT_PH:
				ant.say("ON A BESOIN DE PLACER UN PHEROMONE, ON S ELOIGNE TROP nest " + str(idPathStart))
				ant.putPheromone(idPathStart)
				#  idPathStart += 1
				#  ant.setMemory(idPathStart, gotFood)
				#  ant.commitMemory()
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
				ant.commitMemory()

			return

		ant.explore()
		ant.say("ON A RIEN TROUVE, ON EXPLORE")

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
				ant.commitMemory()

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
					ant.commitMemory()
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
				ant.commitMemory()
			else:
				ant.say("ERREUR PAS DE PHEROMONE")

			return


		return

	return

def nestIA(nest):
	# NEST PROGRAM

	comment(str(nest))

	if nest.memory[0] == 0:
		nest.setMemoryLocation(0, 1)
		nest.commitMemory()
		nest.newAnt(0)

	elif nest.memory[0] == 1:
		nest.setMemoryLocation(0, 2)
		nest.commitMemory()
		nest.antOut(0, 2, 0, 0)


	return

while True:
	nameEntity, entity = Protocol.readInput()
	comment(nameEntity)
	if nameEntity == 'ANT':
		antIA(entity)
	elif nameEntity == 'NEST':
		nestIA(entity)

	Protocol.exit()
