import time
from functools import lru_cache
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
	
cache=dict()	
def cache_fibonacci(n):
	return helper_fibonacci(n)

def helper_fibonacci(n):
	if n in cache:
		#Cache already exists
		return cache[n]
	if n==1:
		value=0
	elif n==2:
		value=1
	else:
		#Cache not set
		a=helper_fibonacci(n-1)
		b=helper_fibonacci(n-2)
		value=a+b
	cache[n]=value
	return value

@lru_cache(maxsize=1024)
def lru_cache_fibonacci(n):
	if n==1:
		return 0
	if n==2:
		return 1 
	else:
		a=rec_fibonacci(n-1)
		b=rec_fibonacci(n-2)
		return a+b				
	
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
t1=time.time()
print(lru_cache_fibonacci(n))
print("LRU Cached-recursive time=", time.time()-t1)
