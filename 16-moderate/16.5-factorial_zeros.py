def factorial_zeros(n):
	print(factorial(n))
	
	zeros=0
	for i in range(5, n+1, 5): #O(n/5)
		sqr=0
		j=i
		while j%5==0:
			j=j/5
			sqr+=1
		#print(i, sqr)
		zeros+=sqr
			
	return zeros
	
def factorial(n):
	if n==1 or n==0:
		return 1
	else: 
		return n*factorial(n-1)

print(factorial_zeros(150))
	
	
