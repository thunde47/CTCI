def missing_number(A,n): #O(NlogN)
	expected_number=['0']*8

	for i in range(0,n+1): #O(N)
		bin_expected_number=''.join(expected_number)		
		try:
			if bin_expected_number!=A[i]:
				return bin_expected_number
		except:
			return bin_expected_number

		carry, expected_number[-1]=('0','1') if A[i][-1]=='0' else ('1','0')		
		for j in range(len(A[i])-2,-1,-1): #O(logN)
			if A[i][j]=='0' and carry=='1':
				expected_number[j]='1'
				carry='0'
			elif A[i][j]=='1' and carry=='1':
				expected_number[j]='0'
				carry='1'
			elif carry==0:
				expected_number[j]=A[i][j]
		
		
if __name__=="__main__":
	A=list()
	n=25
	for i in range(0, n+1):
		A.append('{0:08b}'.format(i))
	del A[13]
	print(missing_number(A,n))
		
