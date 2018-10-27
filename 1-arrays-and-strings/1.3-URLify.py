#Can be done in one loop if two strings are used
#The following code is in-place update, well, not quite because strings
#are immutable in Python and had to be turned to an array of chars or, list
def URLify(s, L):
	s=list(s)
	whitespaces=0
	for i in range(0,L-1): #Counting white spaces O(n)
		if s[i]==" ": 
			whitespaces+=1
	index=L+whitespaces*2-1


	for i in range(L-1,0,-1): #O(n)
		if s[i]==" ":
			s[index]="0"
			s[index-1]="2"
			s[index-2]="%"
			index-=3
		else:
			s[index]=s[i]
			index-=1
	return ''.join(s)

print(URLify("Mr John Smith    ", 13))
print(URLify("Adwaith Gupta  ", 13))
