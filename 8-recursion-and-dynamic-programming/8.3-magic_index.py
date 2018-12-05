import time
def magic_index(A): #O(N)
	for i in range(0,len(A)):
		if i==A[i]:
			return i
	return -1
	
def magic_index_fast(A): #O(logN)
	return binary_search(A, 0, len(A)-1)

def binary_search(A, start, end): 
	if end<start:
		return -1
	mid=(start+end)//2
	if mid==A[mid]:
		return mid
	elif mid<A[mid]:
		return binary_search(A, start, mid-1)
	else:
		return binary_search(A, mid+1, end)	
	
if __name__=="__main__":
	A=list()
	for i in range(0, 100000001):
		A.append(i-100)
	
	A[100000000]=100000000
	t1=time.time()
	print(magic_index(A))
	print("Time=", time.time()-t1)
	t1=time.time()
	print(magic_index_fast(A))
	print("Time=", time.time()-t1)
