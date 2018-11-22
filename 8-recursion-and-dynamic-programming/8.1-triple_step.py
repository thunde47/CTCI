p=0
def steps(n): #O(3^N)
	#print(n, p)
	if n==0:
		return p+1
	if n<=1:
		return steps(n-1)
	if n<=2:
		return steps(n-1) + steps(n-2)
	
	if n>=3:
		return steps(n-1) + steps(n-2) + steps(n-3)
	
n=4
print(steps(n))
