import numpy
def concatenar(nmp):
 	NMP =[int(i) for i in nmp.split()]
 	N = numpy.array([input().split() for i in range(NMP[0])], int)
 	M = numpy.array([input().split() for i in range(NMP[1])], int)
 	
 	return numpy.concatenate((N, M), axis = 0)

if __name__ == '__main__':
	print(concatenar(input()))

