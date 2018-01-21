## OTHER

# operator(value , ....)
def compareKey(key,array,operator, value) :
	return list(filter(lambda x: operator(x[key],value) , array))

##func : min or Max
def minMaxKey(key,array,func) :
	return(func(array, key=lambda x:x[key]))
	
