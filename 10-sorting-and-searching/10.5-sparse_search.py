import random
import time

#Based in the sparseness the time complexity will vary
#from O(logN) in the average case to O(N) in the worst case
#Worst case arises when array is all "". In that case,
#reset function will traverse wntire array to find the
#nearest word (not "").

def sparse_recursive_search(A, start, end, word):
	if end<start:
		return "Not found"
	mid=(start+end)//2
	
	if A[mid]=="":
		mid=reset(A, mid, word)	
	if A[mid]==word:
		return "Found at " + str(mid)		
	elif A[mid]<word:
		return recursive_search(A, mid+1, end, word)
	else:
		return recursive_search(A, start, mid-1, word)
		
def sparse_iterative_search(A, word):
	start=0
	end=len(A)-1
	while start<=end:
		mid=(start+end)//2
		if A[mid]=="":
			mid=reset(A, mid, word)	
		if A[mid]==word:
			return "Found at " + str(mid)
		elif A[mid]<word:
			start=mid+1
		else:
			end=mid-1
	return "Not found"
	
def reset(A, mid, word):
	left=mid-1
	right=mid+1
	while left>=0 and right<len(A):

		if A[left]=="":
			left-=1
		elif A[left]<word:
			left=mid-1
		else:
			return left
		if A[right]=="":
			right+=1
		elif A[right]>word:
			right=mid+1
		else:
			return right
	return mid
			
words=["Adwaith", "Badlands", "Bisti", "Chandrayaan", "Dusk", "Elephant"]
A=[""]*1000000
loc=0
for word in words:
	loc=random.randint(loc, len(A)-1)
	A[loc]=word
#print(A)
t1=time.time()
print(sparse_recursive_search(A, 0, len(A)-1, "Elephant"))
print("Recursive binary search time = ", time.time()-t1)
t1=time.time()
print(sparse_iterative_search(A, "Elephant"))
print("Iterative binary search time = ", time.time()-t1)
