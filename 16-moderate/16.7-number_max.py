def max(a,b):
	try: 
		d=a-b
		n=(1-int(d/(abs(d))))//2
		return a*(1-n)+b*n
	except ZeroDivisionError:
		return 0
	
print(max(17,0))

