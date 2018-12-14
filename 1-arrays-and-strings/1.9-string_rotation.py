#Check if s2 is a rotation of s1
def rotation(s1, s2):
	return isSubstring(s1+s2, s2)
