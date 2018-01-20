import wrapper.wrapper 
import Protocol

t, obj = Protocol.readInput()


if t == 'ANT':
	ant = obj

	# action de ant
	if ant.type == AntType.exploratrice:
		idPath  = ant.m1
		gotFood = ant.m2 

		if ant.stamina < MIN_STAMINA_BEFORE_EAT:
			ant.eat(1)
			Protocol.exit()
		
		ph = ant.arrSeePheromone
		
	elif ant.type == AntType.ramasseuse:
		Protocol.exit()

elif t == 'NEST':
	nest = obj
	# action de nest
