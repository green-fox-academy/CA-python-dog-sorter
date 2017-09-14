dogs = [
{"name": "Bodri", "age": 9},
{"name": "Lolka", "age": 7},
{"name": "Killer", "age": 2},
{"name": "Hektor", "age": 1}
]

def printer(dogs):
	for dog in dogs:
		print(dog["name"] + ", " + str(dog["age"]))
	print("")	


def is_in_order(this, that):
	return this["age"] <= that["age"]	


def swapper(this, that):
	first = dogs.index(this)
	second = dogs.index(that)
	dogs[first], dogs[second] = dogs[second], dogs[first]

def bubble_sort(dogs):
	for i in range(len(dogs)):
		printer(dogs)
		for j in range(len(dogs)-1-i):
			if not is_in_order(dogs[j], dogs[j+1]):
				swapper(dogs[j], dogs[j+1])



bubble_sort(dogs)
		