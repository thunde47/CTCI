from SLL import SLL
from node import Node

if __name__=="__main__":
	A=[12,1,2,10,5,0,9,3,13,7,7]
	L=SLL()
	for a in A:
		L.insert(a)
	L.display()
	L.partition(10)
	L.display()
