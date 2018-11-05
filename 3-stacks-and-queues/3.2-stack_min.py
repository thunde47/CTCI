class Stack_Min():
	stack=None
	def __init__(self):
		self.stack=list()
		
	def push(self, value):
		#Store value alongwith minima upto that point as a tuple
		if self.is_empty():
			self.stack.append((value,value))
		else:
			if value<self.peek()[1]:
				self.stack.append((value,value))
			else:
				self.stack.append((value, self.peek()[1]))
				
	def min(self): #Second element of tuple contains minima upto that point
		return None if self.is_empty() else self.stack[-1][1]	
				
	def pop(self): #First element of tuple contains actual value
		return None if self.is_empty() else	self.stack.pop()[0]		
	
	def is_empty(self):
		return len(self.stack)==0	
		
	def peek(self):
		return None if self.is_empty() else self.stack[-1]	
				
				
if __name__=="__main__":
	s=Stack_Min()
	s.push(8)
	s.push(4)
	s.push(1)
	s.push(9)
	s.push(12)
	s.push(0.5)
	s.push(24)

	s.pop()	
	s.pop()
	print(s.min())		
	while s.peek():
		print(s.pop())
	
	
