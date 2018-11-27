def rotate(A, N): #O(N^2)
	for i in range(0,N): 
		for j in range(i, N):
			A[i][j],A[j][i]=A[j][i], A[i][j]
			
	for i in range(0, N):
		for j in range(0, int(N/2)):
			A[i][j], A[i][N-1-j]=A[i][N-1-j], A[i][j]
			
	return(A)
	
if __name__=="__main__":
	A1=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
	A2=[[1,2,3],[4,5,6],[7,8,9]]
	print(A2)
	print(rotate(A2, 3))
