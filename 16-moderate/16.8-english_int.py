def english_int(n):
	if n==0:
		return n,"zero"
	original_n=n
	english=list()
	ones={
	0:'',
	1:'one ',
	2:'two ',
	3:'three ',
	4:'four ',
	5:'five ',
	6:'six ',
	7:'seven ',
	8:'eight ',
	9:'nine '
	}
	
	tens={
	0:'',
	1:'ten ',
	2:'twenty ',
	3:'thirty ',
	4:'forty ',
	5:'fifty ',
	6:'sixty ',
	7:'seventy ',
	8:'eighty ',
	9:'ninty '
	}
	
	level={
	1:'',
	2:'thousand ',
	3:'million ',
	4:'billion ',
	5:'trillion '
	}
	
	teens={
	'one ':'eleven ',
	'two ':'twelve ',
	'three ':'thirteen ',
	'four ':'forteen ',
	'five ':'fifteen ',
	'six ':'sixteen ',
	'seven ':'seventeen ',
	'eight ':'eighteen ',
	'nine ':'nineteen ',
	}
	
	chunk=1
	while n:
		r=n%1000
		n=n//1000
		if r!=0:
			english.append(level[chunk])
		i=0
		while r:
			r2=r%10
			r=r//10
			if i==0:
				english.append(ones[r2])
			elif i==1:
				if r2==1 and english[-1]!='':
					old_one=english[-1]
					english.pop()
					english.append(teens[old_one])
				else:			
					english.append(tens[r2])
			else:
				english.append("hundred ")
				english.append(ones[r2])
			i+=1
		chunk+=1	
	english.reverse()
	
	english=''.join(english)
	return original_n,english
		
	
if __name__=="__main__":
	print(english_int(701112012320912))
	print(english_int(100000))
	print(english_int(0))
	print(english_int(1))
	print(english_int(19))
	print(english_int(21))
	print(english_int(7000001))
	print(english_int(401))
	
		
