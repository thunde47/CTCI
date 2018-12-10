def subtract(a,b):
	return a+negative(b)
	
def multiply(a,b):
	if a==0 or b==0:
		return 0
	sign=None
	if (a<0 and b<0) or (a>0 and b>0):
		sign=1
	else:
		sign=-1
	
	mult=0
	for i in range(0,abs(b)):
		mult+=abs(a)	
	return negative(mult) if sign==-1 else mult	
	
def divide(a,b):
	if b==0:
		return "Division by zero"
	if a==0:
		return 0
	sign=None
	if (a<0 and b<0) or (a>0 and b>0):
		sign=1
	else:
		sign=-1
	div=0
	while multiply(abs(b),div)<=abs(a):
		div+=1
	return negative(div) if sign==-1 else div
	
def negative(b):
	increment=-1 if b>0 else 1
	i=0
	while b:
		b+=increment
		i+=increment
	return i
		
print(subtract(21,-3))	
print(multiply(21,-3))
print(divide(21,-3))
	


