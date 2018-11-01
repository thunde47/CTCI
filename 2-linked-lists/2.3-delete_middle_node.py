from SLL import SLL
from node import Node

if __name__=="__main__":
	A=[1,33,43,121,19,15,10]
	L=SLL()
	for a in A:
		L.insert(a)
	L.display()
	del_node=L.head.get_pointer().get_pointer() #pointer to 19
	L.delete_node(del_node) #delete node with 19
	L.display()
