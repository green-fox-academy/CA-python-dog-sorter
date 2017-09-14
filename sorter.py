dogs = [
{"name": "Bodri", "age": 9, "gender": "female"},
{"name": "Lolka", "age": 7, "gender": "male"},
{"name": "Killer", "age": 2, "gender": "female"},
{"name": "Hektor", "age": 1, "gender": "male"},
{"name": "Korte", "age": 1, "gender": "female"}
]

def printer(dogs):
	for dog in dogs:
		print(dog["name"] + ", " + str(dog["gender"]))	


def is_in_order(this, that):
	return this["gender"] == "female"
	# return this["age"] <= that["age"]	


def swapper(this, that):
	first = dogs.index(this)
	second = dogs.index(that)
	dogs[first], dogs[second] = dogs[second], dogs[first]

def bubble_sort(dogs):
	for i in range(len(dogs)):
		for j in range(len(dogs)-1-i):
			if not is_in_order(dogs[j], dogs[j+1]):
				swapper(dogs[j], dogs[j+1])

def insertion_sort(dogs):
    for i in range(1,len(dogs)):    
        j = i                   
        while j > 0 and is_in_order(dogs[j], dogs[j-1]) : 
            swapper(dogs[j], dogs[j-1]) 
            j -= 1 




bubble_sort(dogs)
printer(dogs)		