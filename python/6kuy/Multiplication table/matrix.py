import numpy as np

def multiplication_table(size):
	scope = []
	for i in range(size):
		scope.append(i+1)
	array = np.array([scope])
	array = np.outer(array, array)
	s = array.tolist()
	print(s)
	return s 
multiplication_table(2)
multiplication_table(3)    

