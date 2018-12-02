def tic_tac_win(A):
	for i in range(0,3):
		if A[i][0]==A[i][1]==A[i][2] or A[0][i]==A[1][i]==A[2][i]:
			return True
	return A[0][0]==A[1][1]==A[2][2] or A[0][2]==A[1][1]==A[2][0]
	
if __name__=="__main__":
	A=[[1,1,0],[1,0,1],[1,1,0]]
	print(tic_tac_win(A))

