from graph import BinaryNode
from SLL import SLL
from node import Node
from queue import Queue

def list_of_depths(binary_node): #O(N)
	list_of_SLL=list()
	current_sll=SLL()
	current_sll.insert_binary_node(binary_node)
	
	while current_sll.size()>0:
		list_of_SLL.append(current_sll)
		parents=current_sll
		current_sll=SLL()
		c=parents.head	
		
		while c!=None:
			if c.left!=None:
				current_sll.insert_binary_node(c.left)
			if c.right!=None:
				current_sll.insert_binary_node(c.right)
			print(c.value)
			c=c.get_pointer()
		
	for sll in list_of_SLL:
		print("Linked list")
		print(sll.display())

			
if __name__=="__main__":
	root=BinaryNode(1)
	root.left=BinaryNode(2)
	root.right=BinaryNode(3)
	root.left.left=BinaryNode(4)
	root.left.right=BinaryNode(5)
	root.right.right=BinaryNode(20)
	root.right.left=BinaryNode(12)
	#root.right.right.right=BinaryNode(31)
	list_of_depths(root)
