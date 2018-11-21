from node import Node

class SLL(object):
  head=None
  def __init__(self, head=None):
    self.head=head

  def insert(self, value): #O(1)
    new_node=Node(value)
    new_node.set_pointer(self.head)
    self.head=new_node

  def size(self): #O(n)
    count=0
    current=self.head
    while current:
      count+=1
      current=current.get_pointer()
    return count

  def search(self, search_value): #O(n)
    current=self.head
    while current:
      if current.get_value()==search_value:
        return True
      else:
        current=current.get_pointer()
    return False

  def delete(self, delete_value): #O(n)
    if self.head.get_value()==delete_value:
      self.head=self.head.get_pointer()
      return "Head re-assigned"
    previous=None
    current=self.head
    while current:
      if current.get_value()==delete_value:
        previous.set_pointer(current.get_pointer())
        current.set_pointer(None)
        return "Found and deleted"
      else:
        previous=current
        current=current.get_pointer()
    return "Not found" 

  def display(self): #O(n)
    current=self.head
    while current:
      print(current.get_value())
      current=current.get_pointer()

  def remove_dupes(self):
    print("Deleting duplicates")
    current=self.head
    d={current.get_value():1}
    while current.get_pointer(): #O(n)

      if current.get_pointer().get_value() in d: #O(1)
        current.set_pointer(current.get_pointer().get_pointer()) #O(1)

      else:
        d[current.get_pointer().get_value()]=1
        current=current.get_pointer()

  def k_to_last(self,k):
    print("Printing from kth position to the last position")
    current=self.head
    i=0
    while current: #O(n)
      if i>=k:
        print(current.get_value())
      i+=1  
      current=current.get_pointer()  

  def delete_node(self, node):
    print("Deleting a middle node")
    node.set_value(node.get_pointer().get_value())
    node.set_pointer(node.get_pointer().get_pointer())
    
  def partition(self, x): #O(N)
  	print("Partitioning around ", x)
  	current=self.head
  	left_side=SLL()
  	right_side=SLL()
  	while current: #O(N)
  		
  		if current.get_value()>=x:
  			right_side.insert(current.get_value()) #Insertion at end O(1)
  			
  		else:
  			left_side.insert(current.get_value())	#Insertion at end O(1)
  		current=current.get_pointer()
 
  	current=left_side.head
  	if current==None:
  		self.head=right_side.head
  	else:
	  	while current.get_pointer(): #Worst O(N)
	  		current=current.get_pointer()
	  	current.set_pointer(right_side.head)
	  	self.head=left_side.head #O(1) because only pointer is re-directed
  		
  		
  			
	
  			
  			
  			
  			
  			
  			
  			
  			
	  
