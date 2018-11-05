class SetOfStacks():
	def __init__(self, stack_height):
		self.stack=[[]]
		self.stack_height=stack_height
		self.height=0
		self.stack_number=0
		
	def push(self, value):
		if self.height<self.stack_height:
			
			self.stack[self.stack_number].append(value)
			self.height+=1
		else:
			self.stack.append([value])
			self.stack_number+=1
			self.height=1
		print(self.stack)
			
	def pop(self):
		if self.is_empty():
			return None
		else:
			self.height-=1	
			top=self.stack[-1].pop()		
			if self.height==0 and self.stack_number>0:
				self.stack.pop()
				self.height=len(self.stack[-1])
				self.stack_number-=1
				
			return top			
		
	def popAt(self, i):
		if i<self.stack_number:
			return self.stack[i].pop()		
		else:
			return "Stack does not exist"		
			
	def is_empty(self):
		return len(self.stack[0])==0 and len(self.stack)==1	
			
if __name__=="__main__":
	ss=SetOfStacks(3)
	for i in range(0,15):
		ss.push(i)
	print("Popped ", ss.popAt(3))
	
	while not ss.is_empty():
		print(ss.pop())
	
	
