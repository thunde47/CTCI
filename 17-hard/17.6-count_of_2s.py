def twos(n):
	t=0
	for i in range(2, n+1):
		
		while i:
			if i%10==2:
				t+=1
			i//=10
	return t
	
print(twos(25))
