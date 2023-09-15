# print a list where values are the square of numbers between 1-30

def printValues():
	integer = list()
	for i in range(1,21):  # i prints ranges 
		integer.append(i**2)
	print(integer)
		
printValues()