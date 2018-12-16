import unittest

def find_indices(nums, target):
	if not nums:
		return [-1, -1]
	min_index=left_bias_binary_search(nums, target, 0, len(nums)-1) #O(logN)
	max_index=right_bias_binary_search(nums, target, min_index, len(nums)-1) #O(log(N-min_index))
	return [min_index, max_index]
	
def left_bias_binary_search(nums, target, start, end):
	min_index=-1
	while start<=end:
		
		mid=(start+end)//2
		if nums[mid]==target:
			min_index=mid
			end=mid-1
		elif nums[mid]>target:
			end=mid-1
		else:
			start=mid+1
	return min_index
	
def right_bias_binary_search(nums, target, start, end):
	max_index=-1
	while start<=end:
		
		mid=(start+end)//2
		if nums[mid]==target:
			max_index=mid
			start=mid+1
		elif nums[mid]>target:
			end=mid-1
		else:
			start=mid+1
	return max_index	

class Test(unittest.TestCase):
	def test_left_bias_binary_search(self):
		self.assertEqual(left_bias_binary_search([],8, 0,-1),-1)	
		self.assertEqual(left_bias_binary_search([8],8, 0, 0),0)			
		self.assertEqual(left_bias_binary_search([1,2,8,8,8,8,10],8, 0, 6),2)
		self.assertEqual(left_bias_binary_search([8,8,8,8,8,8,10],8, 0, 6),0)	
		self.assertEqual(left_bias_binary_search([1,2,3,4,5,6,10],8, 0, 6),-1)		
		self.assertEqual(left_bias_binary_search([1,2,3,4,5,6,10],1, 0, 6),0)	
		self.assertEqual(left_bias_binary_search([1,2,3,4,5,6,10],10, 0, 6),6)		
		
	def test_right_bias_binary_search(self):
		self.assertEqual(right_bias_binary_search([],8, 0, -1),-1)
		self.assertEqual(right_bias_binary_search([8],8, 0, 0),0)					
		self.assertEqual(right_bias_binary_search([1,2,8,8,8,8,10],8, 0, 6),5)
		self.assertEqual(right_bias_binary_search([8,8,8,8,8,8,10],8, 0, 6),5)	
		self.assertEqual(right_bias_binary_search([1,2,3,4,5,6,10],8, 0, 6),-1)		
		self.assertEqual(right_bias_binary_search([1,2,3,4,5,6,10],10, 0, 6),6)		
		
	def test_find_indices(self):
		self.assertEqual(find_indices([],8),[-1,-1])
		self.assertEqual(find_indices([8],8),[0,0])					
		self.assertEqual(find_indices([1,2,8,8,8,8,10],8),[2,5])
		self.assertEqual(find_indices([8,8,8,8,8,8,10],8),[0,5])	
		self.assertEqual(find_indices([1,2,3,4,5,6,10],8),[-1,-1])		
		self.assertEqual(find_indices([1,2,3,4,5,6,10],10),[6,6])							
		
if __name__=="__main__":
	unittest.main()
	
