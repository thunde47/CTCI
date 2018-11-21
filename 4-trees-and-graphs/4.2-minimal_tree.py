from graph import BinaryNode
from graph import in_order_traversal

def BST_insert(root, node):
	if root is None:
		root=node
	if root.value>=node.value:
		if root.left is None:
			root.left=node
		else:
			BST_insert(root.left, node)
	else:
		if root.right is None:
			root.right=node
		else:
			BST_insert(root.right, node)
			
if __name__=="__main__":
	A=[1,2,3,5,6,7, 12]
	root=BinaryNode(4)
	for a in A:
		BST_insert(root, BinaryNode(a))
	in_order_traversal(root)
