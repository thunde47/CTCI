class Node:
  pointer=None  
  value=None
  def __init__(self, value, pointer=None, left=None, right=None):
    self.value=value
    self.pointer=pointer
    self.left=left
    self.right=right

  def get_value(self):
    return self.value

  def set_value(self, new_value):
    self.value=new_value

  def get_pointer(self):
    return self.pointer

  def set_pointer(self, new_pointer):
    self.pointer=new_pointer

