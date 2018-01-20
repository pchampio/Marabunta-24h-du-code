
## code provisoire nest

ANT_FOOD_START = 20
STEP_BTW_PATHS = 51

nest = "Un truc"
nbAntsTab = "le tableau du nombre d'ants"


# 


if 0 in nbAntsTab:
	i = nbAntsTab.index(0)

	if nest.getAntCount(ANT_ECLAIREUR) == 0:
		nest.newAnt(ANT_ECLAIREUR)
	else
		nest.setMemoryLocation(i, 1)
		nest.commitMemory()

		nest.antOut(ANT_ECLAIREUR, ANT_FOOD_START, i * STEP_BTW_PATHS, 0)
	
	return

elif 2 in nbAntsTab:
	i = nbAntsTab.index(2)

	if nest.getAntCount(ANT_RAMASSEUR) == 0:
		nest.newAnt(ANT_RAMASSEUR)
	else:
		nest.setMemoryLocation(i, 4)
		nest.commitMemory()

		nest.antOut(ANT_RAMASSEUR, ANT_FOOD_START, i * STEP_BTW_PATHS, 0)

	return

elif 3 in nbAntsTab:
	i = nbAntsTab.index(3)

	if nest.getAntCount(ANT_RAMASSEUR) == 0:
		nest.newAnt(ANT_RAMASSEUR)
	else:
		nest.setMemoryLocation(i, 4)
		nest.commitMemory()

		nest.antOut(ANT_RAMASSEUR, ANT_FOOD_START, i * STEP_BTW_PATHS, 0)

	return

minValue = min(nbAntsTab)




































# pathsTab # le tableau des chemins vers la bouffe (première moitié)
antsTab  # le tableau donnant le nombre fourmis parties pour chaque chemin

if nest.getAntCount(ANT_ECLAIREUR) == 0:
	nest.newAnt(ANT_ECLAIREUR)
	return

else:
	

	if 0 in antsTab:
		# il y a des paths qui sont pas encore explorés
		index = antsTab.index(0)
		nest.antOut(ANT_ECLAIREUR, ANT_FOOD_START, index * MAX_PHEROMONES, 0)
		nest.setMemoryLocation(index, 1)
		nest.commitMemory()
		return
	
	
