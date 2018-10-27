#Check if s1 is a permutation of s2
#O(n)
def check_permutations(s1,s2):
	if not len(s1)==len(s2):
		return False
	d=dict()
	for c in s2: #Generate frequence dictionary of s2
		if c in d:
			d[c]+=1
		else:
			d[c]=1

	for c in s1:
		if c in d and d[c]>0:
			d[c]-=1
			continue
		else:
			return False

	return True

print(check_permutations("bootkaar", "kabootar"))
	
