def flip_bit_to_win(n):
	#p contains all permutations of p
	p=[n] #In case all bits are already 1, not flip required and this case must be scrutanized as is	
	for i in range(0, len(bin(n)[2:])):		
		if n&(1<<i)==0: #If bit is 0 at ith location
			p.append(n&(~(1<<i))|(1<<i))  #update bit to 1 at ith location
	c_max=0
	for x in p:
		c=0
		#print(bin(x))	
		while x!=0:
			x=x&(x<<1) #flip least significant 1 to 0
			c+=1 #number of contiguous 1s = number of times loop runs to reduce x to 0
		if c>c_max: #Check if this permutation of n has max contiguous 1s
			c_max=c
	return c_max
print(flip_bit_to_win(1775))
