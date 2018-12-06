def sorted_merge(A, B, lenA, lenB):
	nA=lenA-1
	nB=lenB-1
	index=lenA+lenB-1
	while nB>=0: #worst case O(nA+nB)
		if nA>=0 and A[nA]>B[nB]:
			A[index]=A[nA]
			nA-=1
		else:
			A[index]=B[nB]
			nB-=1
		index-=1
	return A
		
if __name__=="__main__":
	A=[1,4,5,30,42,None, None, None]
	B=[3,7,50]
	print(sorted_merge(A,B,5,3))
