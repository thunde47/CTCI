from stack import Stack

class MyQueue:
	def __init__(self):
		self.add_stack=Stack()
		self.pop_stack=Stack()
		
		
	def add(self, value): #O(1)
		self.add_stack.push(value)
		
	def remove(self): #Worst O(N)
		if self.pop_stack.is_empty():
			while not self.add_stack.is_empty():
				self.pop_stack.push(self.add_stack.pop())
		return self.pop_stack.pop()
		
if __name__=="__main__":
	Q=MyQueue()
	Q.add(1)
	Q.add(2)
	Q.add(10)
	Q.add(13)
	print(Q.remove())
	print(Q.remove())
	print(Q.remove())
	Q.add(21)
	print(Q.remove())
	print(Q.remove())
