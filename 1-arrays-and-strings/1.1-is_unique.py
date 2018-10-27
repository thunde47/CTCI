#Additional data structure is not allowed
#Time complexity O(n^2)
def is_unique_1(s):
	for i in range(0, len(s)-1):
		for j in range(i+1, len(s)):
			if s[i]==s[j]: return False
	return True

#Additional data structure is allowed
#Time complexity O(n)
def is_unique_2(s):
	d=dict()
	for c in s: #O(n)
		if c in d: #O(1)
			return False
		d[c]=1
	return True

print(is_unique_1("adwaith"))
print(is_unique_2("gupta"))
