import unittest

def smallest_difference(A,B): #O(NM)
	if not A and not B:
		return 0
	elif not A:
		return min(B)
	elif not B:
		return min(A)
	min_diff=float('inf')
	for a in A:
		for b in B:	
			if abs(a-b)<min_diff:
				min_diff=abs(a-b)
	return min_diff
	
def smallest_difference_fast(A,B): #O(NlogN+MlogM)
	#print(A)
	if not A and not B:
		return 0
	elif not A:
		
		return min(B)
	elif not B:
		A.sort()
		return min(A)
	A.sort()
	B.sort()
	
	min_diff=float('inf')
	i=j=0
	na, nb=len(A), len(B)
	while i<na and j<nb:		
		if abs(A[i]-B[j])<min_diff:
			min_diff=abs(A[i]-B[j])
		if A[i]<B[j]:
			i+=1
		else:
			j+=1
	return min_diff	
	
	
class Test(unittest.TestCase):
	def test_smallest_difference(self):
		self.assertEqual(smallest_difference([],[]),0)
		self.assertEqual(smallest_difference([],[9,1,7]),1)
		self.assertEqual(smallest_difference([15],[]),15)				
		self.assertEqual(smallest_difference([1,3,15,11,2],[23,127,235,19,8]), 3)
	
	def test_smallest_difference_fast(self):
		self.assertEqual(smallest_difference_fast([],[]),0)
		self.assertEqual(smallest_difference_fast([],[9,1,7]),1)
		self.assertEqual(smallest_difference_fast([15],[]),15)	
		self.assertEqual(smallest_difference_fast([1,3,15,11,18],[23,127,235,19,8]), 1)
		self.assertEqual(smallest_difference_fast([128],[23,127,235,19,8]), 1)
		self.assertEqual(smallest_difference_fast([1,3],[23,127,235,19,3,1]), 0)				
		
	
if __name__=="__main__":
	unittest.main()

	
	
