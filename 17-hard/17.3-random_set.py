import random
def random_set(A,m):
	n=len(A)
	#print(random.random())
	s=set()
	for i in range(0,m):
		s.add(A[int(random.random()*(n-1))])
	return s

if __name__=="__main__":
	A=[2,4,9,7,1,3,12,3]
	print(random_set(A,3))
