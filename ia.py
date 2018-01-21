import operator
from utils import *
from wrapper import Protocol
from Comment import comment
import time
from random import randint

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
		lastIdPaht = []
		lastIdPaht.append(0)
		for ph in ant.arrSeePheromone:
			lastIdPaht.append(ph["type"])
		idPathStart = max(lastIdPaht)

		if idPathStart > ant.m1:
			ant.say("SUICIDE")
			ant.suicide()
			return



		gotFood     = (ant.m2 == 1)

		# NEED STAMINA
		if ant.stamina < STAMINA_NEED_EAT:
			ant.say("ON BOUFFE, ON NEED DE LA STAMINA")
			ant.suicide()
			return

		phs = ant.arrSeePheromone
		# needRechargePhs = les phs qui sont < PH_NEED_RECHARGE
		nearest = compareKey("area", phs, operator.eq, "NEAR")
		needRefuel = compareKey("persistance", nearest, operator.lt, PH_NEED_RECHARGE)



		#  if len(needRefuel) > 0:
			#  ant.say("LE PHEROMONE A BESOIN DE SE FAIRE RECHARGER")
			#  ant.rechargePheromone(needRefuel[0]["id"])
			#  return

		# farPh = la phs la plus loin
		# HOME RETURN


		id_min = 0
		type_min = 99999999999
		for ph in ant.arrSeePheromone:
			if type_min > ph["type"]:
				id_min = ph["id"]
				type_min = ph["type"]
		if gotFood:

			if ant.arrSeeNest and ant.arrSeeNest[0]["area"] == 'FAR':
				ant.say("ON SE DIRIGE VERS LE BERCAIL")
				ant.moveTo(ant.arrSeeNest[0]["id"])
				return

			if ant.arrSeeNest and ant.arrSeeNest[0]["area"] == 'NEAR':
				ant.say("BERCAIL")
				ant.nest(ant.arrSeeNest[0]["id"])
				return

			ant.say("ON SE DIRIGE VERS LE CHEMIN DU RETOUR")
			ant.moveTo(id_min)
			return

		# partie calcul min distance
		ant.say("test")
		phs = [ x for x in phs if x["dist"] < DISTANCE_NEED_PUT_PH ]
		ant.say("phs" + str(phs))

		if not phs:
			ant.say("ON A BESOIN DE PLACER UN PHEROMONE, INIT")
			ant.putPheromone(idPathStart + 1)
			return


		#  ant.say("idPathStart" + str(idPathStart))
		#  ant.say("arrSeePheromone" + str(ant.arrSeePheromone))


		ant.say("arrSeeFood" + str(ant.arrSeeFood))
		if ant.arrSeeFood:

			nearestFoodSrc = [ x for x in ant.arrSeeFood if x["area"] == 'NEAR']

			if nearestFoodSrc:
				ant.say("ON RECUPERE DE LA BOUFFE")
				ant.collect(nearestFoodSrc[0]["id"],  min(nearestFoodSrc[0]["amount"], ant.FOOD_MAX) - 1)
				ant.setMemory(idPathStart + 10, 1)
				ant.commitMemory()
				return

			else:
				ant.say("ON SE DIRIGE VERS LA BOUFFE")
				ant.moveTo(ant.arrSeeFood[0]["id"])
				return


		ant.explore()
		ant.say("ON A RIEN TROUVE, ON EXPLORE")

		return

	elif ant.type == ANT_RAMASSEUR:

		lastIdPaht = []
		lastIdPaht.append(0)
		for ph in ant.arrSeePheromone:
			lastIdPaht.append(ph["persistance"])
		idPathStart = max(lastIdPaht)


		gotFood     = (ant.m2 == 1 or ant.m2 == 2)
		needMove = (ant.m2 == 1)

		# NEED STAMINA
		if ant.stamina < STAMINA_NEED_EAT:
			ant.say("ON BOUFFE, ON NEED DE LA STAMINA")
			ant.eat(1)
			return

		phs = ant.arrSeePheromone
		# needRechargePhs = les phs qui sont < PH_NEED_RECHARGE
		nearest = compareKey("area", phs, operator.eq, "NEAR")
		needRefuel = compareKey("persistance", nearest, operator.lt, PH_NEED_RECHARGE)



		#  if len(needRefuel) > 0:
			#  ant.say("LE PHEROMONE A BESOIN DE SE FAIRE RECHARGER")
			#  ant.rechargePheromone(needRefuel[0]["id"])
			#  return

		# farPh = la phs la plus loin
		# HOME RETURN


		id_min = 0
		pers_min = 99999999999
		for ph in ant.arrSeePheromone:
			if pers_min > ph["persistance"]:
				id_min = ph["id"]
				pers_min = ph["persistance"]
		if gotFood:

			if ant.arrSeeNest and ant.arrSeeNest[0]["area"] == 'FAR':
				ant.say("ON SE DIRIGE VERS LE BERCAIL")
				ant.moveTo(ant.arrSeeNest[0]["id"])
				return

			if ant.arrSeeNest and ant.arrSeeNest[0]["area"] == 'NEAR':
				ant.say("BERCAIL")
				ant.nest(ant.arrSeeNest[0]["id"])
				return

			ant.say("ON SE DIRIGE VERS LE CHEMIN DU RETOUR")
			
			if needMove:
				ant.setMemory(ant.m1, 2)
				ant.moveTo(pers_min)
			else :
			
				ant.setMemory(ant.m1,1)
				nearestPhero = [ x for x in ant.arrSeePheromone if x["distance"] == 0][0]
				ant.rechargePheromone(nearestPhero)
			
			ant.commitMemory()
			return



		ant.say("arrSeeFood" + str(ant.arrSeeFood))
		if ant.arrSeeFood:

			nearestFoodSrc = [ x for x in ant.arrSeeFood if x["area"] == 'NEAR']

			if nearestFoodSrc:
				ant.say("ON RECUPERE DE LA BOUFFE")
				ant.collect(nearestFoodSrc[0]["id"],  min(nearestFoodSrc[0]["amount"], ant.FOOD_MAX))
				ant.setMemory(ant.m1, 2)
				ant.commitMemory()
				return

			else:
				ant.say("ON SE DIRIGE VERS LA BOUFFE")
				ant.moveTo(ant.arrSeeFood[0]["id"])
				return

		return


	return

NB_ANT_CREATED = 0
KILL_AT_PH = 1

def nestIA(nest):
	# NEST PROGRAM

	comment(str(nest))

	if nest.memory[KILL_AT_PH] == 0:
		nest.memory[KILL_AT_PH] = 20
		nest.commitMemory()

	if nest.arrAnt:
		nest.memory[KILL_AT_PH] = int(nest.arrAnt[0]["m1"] * 1.1)
		nest.commitMemory()


	if nest.arrAntType:
		nest.antOut(0, 0, nest.memory[KILL_AT_PH], 0)
		return

	if nest.memory[NB_ANT_CREATED] < (nest.food/10) / (nest.memory[NB_ANT_CREATED] + 1):
		nest.memory[NB_ANT_CREATED] += 1
		nest.commitMemory()
		nest.newAnt(0)
		return

	if randint(0,40) < 2:
		nest.memory[NB_ANT_CREATED] -= nest.memory[NB_ANT_CREATED]//10
		nest.memory[KILL_AT_PH] = int(nest.memory[KILL_AT_PH]+1 * 1.5)
		nest.commitMemory()
		nest.newAnt(0)
		return


while True:
	nameEntity, entity = Protocol.readInput()
	comment(nameEntity)
	if nameEntity == 'ANT':
		antIA(entity)
	elif nameEntity == 'NEST':
		nestIA(entity)

	Protocol.exit()
