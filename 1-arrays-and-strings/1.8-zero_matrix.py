def zero_matrix(A,M,N): #O(N^2)
	zero_i=set()
	zero_j=set()
	
	for i in range(M):
		for j in range(N):
			if A[i][j]==0:
				zero_i.add(i)
				zero_j.add(j)
	
	for i in range(M):
		if i in zero_i:
			for j in range(N):
				A[i][j]=0
				
	for j in range(N):
		if j in zero_j:
			for i in range(M):
				A[i][j]=0
	return A
	
if __name__=="__main__":
	A=[[0,4,4,1,5],[7,0,7,8,9],[13,5,2,3,1],[1,1,1,1,0]]
	print(A)
	print(zero_matrix(A,4,5))
