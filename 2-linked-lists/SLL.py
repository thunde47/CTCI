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
