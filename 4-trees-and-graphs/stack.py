class Stack:
	stack=None
	def __init__(self):
		self.stack=list()
		
	def pop(self):
		return None if self.is_empty() else self.stack.pop()
	
	def push(self, value):
		self.stack.append(value)
		
	def peek(self):
		return None if self.is_empty() else self.stack[-1]
		
	def size(self):
		return len(self.stack)
		
	def is_empty(self):
		return self.size()==0
	
	#Find minima in an existing stack	
	def stack_min(self):
		minima=self.peek()		
		while self.peek()!=None: #O(N) worst case
			if self.peek()<minima:
				minima=self.peek()
			self.pop()
		return minima		
		
if __name__=="__main__":
	s=Stack()
	s.push(1)
	s.push(12)
	print(s.size())
	print(s.peek())
	print(s.pop())
	print(s.pop())
