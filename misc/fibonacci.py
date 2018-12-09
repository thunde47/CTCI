import time
def rec_fibonacci(n):
	if n==1:
		return 0
	if n==2:
		return 1 
	else:
		a=rec_fibonacci(n-1)
		b=rec_fibonacci(n-2)
		return a+b

def iter_fibonacci(n):
	if n==1:
		return 0
	if n==2:
		return 1
	a,b,f=0,1,0
	for i in range(2,n):		
		f=a+b
		a,b=b,f		
	return f
	
def cache_fibonacci(n):
	cache=[-1]*(n)
	return helper_fibonacci(n, cache)

def helper_fibonacci(n, cache):
	if n==1:
		return 0
	if n==2:
		return 1
	if cache[n-1]==-1: #Cache not set
		a=helper_fibonacci(n-1, cache)
		b=helper_fibonacci(n-2, cache)
		cache[n-1]=a+b
	#Cache already contains the desired value
	return cache[n-1]
		
	
n=30
t1=time.time()
print(rec_fibonacci(n))
print("Recurion time=", time.time()-t1)
t1=time.time()
print(iter_fibonacci(n))
print("Iteration time=", time.time()-t1)
t1=time.time()
print(cache_fibonacci(n))
print("Cached-recursive time=", time.time()-t1)
