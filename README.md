# Marabunta-24h-du-code
Un jeu multi-agents avec des fourmis
# test communication: T2 OK,


# Nest


`newAnt(type)`  
Create a new ant  
@param : ant's type   

`antOut(type, food, m0, m1)`  
Ant go out!!! We give her food, m0, m1 and her type
@param type : ant's type  
@param food : food amount  
@param m0 : 1 byte
@param m1 : 1 byte  

`memory(memory)`  
Modify nest memory 
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

# UTILS

`compareKey(key,array,operator, value)`

compare key in an array of dict. value operator .....
@param key : key to compare
@param array : array to use
@param operator : operator (see python doc)
@param value : value to compare


	
`minMaxKey(key,array,func)`
Apply function on key of an array of dict. Only tested for min & max
@param key : key to filter on
@param array : array to use
@param func : function to apply
