class Queue:
	queue=None
	def __init__(self):
		self.queue=list()
		
	def add(self, value):
		self.queue.insert(0,value)
	
	def remove(self):
		return None if self.is_empty() else self.queue.pop()
	
	def peek(self):
		return None if self.is_empty() else self.queue[-1]
	
	def is_empty(self):
		return self.size() == 0
	
	def size(self):
		return len(self.queue)	
		
if __name__=="__main__":
	q=Queue()
	q.add(1)
	q.add(3)
	q.add(9)
	#print(q.size())
	#print(q.peek())
	print(q.remove())
	print(q.remove())
	print(q.remove())		
	print(q.remove())	
