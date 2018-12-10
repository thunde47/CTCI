import unittest

def longest(A): #O(N)
	diff=list()
	nums=0
	for a in A: #O(N)
		nums+=1 if a.isdigit() else -1
		diff.append(nums)
		
	d=dict()
	d[0]=-1
	start=end=0
	for i in range(0, len(diff)): #O(N)
		if diff[i] not in d:
			d[diff[i]]=i
		else:
			distance=i-d[diff[i]] #current index - previous index with same value
			max_distance=end-start
			if distance>max_distance:
				max_distance=distance
				start=d[diff[i]]
				end=i
		
	return A[start+1:end+1]
	
class Test(unittest.TestCase):
	def test_longest(self):
		self.assertEqual(longest('1abcdefg25b'), 'fg25')
		self.assertEqual(longest('15abcd70ea98zc7'), '15abcd70ea98')
		self.assertEqual(longest(''), '')
		
				
if __name__=="__main__":
	unittest.main()		
