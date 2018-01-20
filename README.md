# Marabunta-24h-du-code
Un jeu multi-agents avec des fourmis
# test communication: T2 OK,


# Nest


`newAnt(type)`  
Permet de creer une nouvelle fourmi  
@param : le type de la fourmi a creer   

`antOut(type, food, m0, m1)`  
Permet de faire sortir une fourmi d'un certain type ave cune quantite de nourriture. On peut aussi lui donner ses valeurs m0 et m1  
@param type : type de la fourmi  
@param food : quantite de nourriture  
@param m0 : 1 octet  
@param m1 : 1 octet  

`memory(memory)`   
Modifie la memoire de la nest.  
@param memory : array length must be equal to 20     


# Ant  

`explore(self)`  
Ant go explore!!!  

`turn(angle)`   
Turn the ant around  
@param angle : angle  

`moveTo(id)`  
Move the ant towards the id   
@param id : Objective's id   


`putPheromone(`type)`  
Place down pheromone  
@param type : type of the pheromone  

`changePheromone(id, type)`  
Change the type of the pheromone  
@param id : Changing Pheromone's id  
@param type :  new pheromone type  


`rechargePheromone(id)`  
Reload the pheromone  
@param id : pheromone's id   

`collect(id, quantity)`  
Harvest food  
@param id : Food Pile's id  
@param quantity : Amount of food to harvest  

`doTropha(id, quantity)`  
Throphallaxy between two ants  
@param id : Receiving ant's id  
@param quantity :  Amount of food to give  


`eat(quantity)`  
Convert food to stamina  
@param quantity :  Quantity to convert  

`nest(id)`  
Enter in a nest  
@param id : nest's id  
	
`attack(id, strength)`  
Attack another ant  
@param id : victim's id  
@param strength : Strength of the attack


`suicide()`  
Kill the ant  
	
`memory(m0=self.m1, m1=self.m2)`  
By default the value of the ant.  
Change the ant's memory  
@param m0 : 1st byte  
@param m1 : 2nd byte  
