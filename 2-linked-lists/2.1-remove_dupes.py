from node import Node
from SLL import SLL

if __name__=="__main__":
	A=[1,33,43,121,33,15,1]
	L=SLL()
	for a in A:
		L.insert(a)
	L.display()
	L.remove_dupes()
	L.display()

