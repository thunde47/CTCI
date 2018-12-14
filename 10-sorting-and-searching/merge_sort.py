#Runtime is O(NlogN) in worst and average case both
def merge_sort(A, left, right):
	if len(A)==1: return A
	
	if left<right:
		middle=int((left+right)/2)
		merge_sort(A, left, middle)
		merge_sort(A, middle+1, right)
		return merge(A,left,middle,right)

def merge(A, left, middle, right):
	left_array=A[left:middle+1]
	right_array=A[middle+1: right+1]
	k=left
	while len(left_array)!=0 and len(right_array)!=0:
		if left_array[0]<right_array[0]:
			
			A[k]=left_array[0]
			del left_array[0]
		else:

			A[k]=right_array[0]
			del right_array[0]
		k=k+1

	while len(left_array)!=0:
		
		A[k]=left_array[0]
		del left_array[0]
		k=k+1
	while len(right_array)!=0: 
		
		A[k]=right_array[0]
		del right_array[0]
		k=k+1
	return A


def main():
	A=[1,7,23,13,35,68]
	merge_sort(A, 0, len(A)-1)
	print(A)


if __name__=="__main__":
	main()
