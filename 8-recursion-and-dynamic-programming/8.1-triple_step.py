import time

p=0
def steps(n): #O(3^N)
	
	if n==0:
		return p+1
	if n<=1:
		return steps(n-1)
	if n<=2:
		return steps(n-1) + steps(n-2)
	
	if n>=3:
		return steps(n-1) + steps(n-2) + steps(n-3)
		
p=0		
def steps_efficient(n): #O(N)
	cache=[None]*(n+1)
	return steps_cache(n, cache)
	
def steps_cache(n, cache):
	if n==0:
		return p+1
	if cache[n]!=None:
		return cache[n]
	if n<=1:
		cache[n]=steps_cache(n-1,cache)
		return cache[n]
	if n<=2:
		cache[n]=steps_cache(n-1,cache) + steps_cache(n-2, cache)
		return cache[n]
	if n>=3:
		cache[n]=steps_cache(n-1, cache) + steps_cache(n-2, cache) + steps_cache(n-3, cache)	
		return cache[n]
	
n=30
t0=time.time()
print("Permutations using Brute force=",steps(n))
print("Time elapsed", time.time()-t0)
t0=time.time()
print("Permutations using Caching=", steps_efficient(n))
print("Time elapsed", time.time()-t0)
