def search_no_size(A, n): #O(logN)
	index=1
	while A.elementAt(index)!=-1 and A.elementAt(index)<n: #O(logN)
		index*=2
	#start=index/2 because n is in last expansion
	binary_search(A, index/2, index, n) 
	
def binary_search(A, start, end, n): #O(logN)
	if end<start:
		return False
	mid=(start+end)//2
	if A[mid]==n:
		return True
	elif A[mid]==-1 or A[mid]>n:
		return binary_search(A, start, mid-1, n)
	else:
		return binary_search(A, mid+1, end, n)
