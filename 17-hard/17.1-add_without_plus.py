def add_without_plus(a,b):
	bin_a='{0:032b}'.format(a)
	
	bin_b='{0:032b}'.format(b)
	len_bin_a=len(bin_a)
	len_bin_b=len(bin_b)
	bin_c=list()
	#print(bin_a, bin_b)
	if len_bin_a>len_bin_b:
		length=len_bin_a
	else:
		length=len_bin_b
	carry='0'
	
	for i in range(length-1, 1, -1):
		does_carry=False
		
		if bin_a[i]==bin_b[i]=="1":
			bin_c.append("0")
			does_carry=True
		elif bin_a[i]==bin_b[i]=="0":
			bin_c.append("0")
		else:
			bin_c.append("1")
			
		if carry=="1":
			if bin_c[-1]=="0":
				bin_c[-1]="1"
			else:
				bin_c[-1]="0"
				does_carry=True
				
		if does_carry:
			carry="1"
		else:
			carry="0"
		
	bin_c.append(carry)
	
	bin_c_str=''.join(reversed(bin_c))
	
	return int(bin_c_str,2)
			
	
if __name__=="__main__":
	print(add_without_plus(1343324,2100000))
