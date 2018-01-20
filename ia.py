import wrapper.wrapper 
import Protocol

t, obj = Protocol.readInput()


if t == 'ANT':
	ant = obj

	# action de ant
	if ant.type == AntType.exploratrice:
		idPath  = ant.m1
		gotFood = ant.m2 

		# NEED STAMINA
		if ant.stamina < STAMINA_NEED_EAT:
			ant.eat(1)
			Protocol.exit()
		
		phs = ant.arrSeePheromone
		# needRechargePhs = les phs qui sont < PH_NEED_RECHARGE
		# nearestPh = la ph la plus proche dans 
		if nearestPh:
			ant.rechargePheromone(nearestPh["id"])
			Protocol.exit()
		

		# farPh = la phs la plus loin
		# HOME RETURN
		if gotFood == True:
			ant.moveTo(farPh["id"])
			Protocol.exit()

		# partie calcul min distance

		if len(ant.arrSeeFood) > 0:
			Protocol.exit()
			#if ant.arrSeeFood
			
		
	elif ant.type == AntType.ramasseuse:
		Protocol.exit()

elif t == 'NEST':
	nest = obj
	# action de nest
