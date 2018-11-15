from stack import Stack
from queue import Queue

class BinaryNode:
	def __init__(self, value):
		self.value=value
		self.right=None
		self.left=None
				
class Graph:
	def __init__(self, graph=dict()):
		self.graph=graph
		
	def add_node(self, node, connections):
		self.graph[node]=connections
		
	def show(self):
		print(self.graph)
		
	def is_tree(self):
		visited=list()
		for node, connections in self.graph.items():
			visited.append(node)
			for connection in connections:
				if connection in visited:
					return False
		return "Graph is a tree (no cycles)"		
		
	def is_binary_tree(self):
		visited=list()
		for node, connections in self.graph.items():
			visited.append(node)
			if len(connections)<=2:
				for connection in connections:
					if connection in visited:
						return False
			else: return False			
		return "Graph is a binary tree (at most two child nodes)"
	
	def generate_binary_tree(self):
		for key, connections in self.graph.items():
			
			node=BinaryNode(key)
			try: 
				node.left=BinaryNode(connections[0])
				node.right=BinaryNode(connections[1])
			except:pass
			print(node.value, node.left.value, node.right.value)
			
			
	def is_binary_search_tree(self):
		pass
		
	#Root-->Left-->Right	
	def pre_order_traversal(self, root):		
		print(root)
		try:
			left=self.pre_order_traversal(self.graph[root][0])
			if left!=None: print(left)
			right=self.pre_order_traversal(self.graph[root][1])
			if right!=None: print(right)
		except:
			pass	
			
def pre_order_traversal(node):
	print(node.value)	
	if node.left!=None:
		pre_order_traversal(node.left)
	if node.right!=None:
		pre_order_traversal(node.right)
		

if __name__=="__main__":
	g=Graph()
	g.add_node(8,[4,10])
	g.add_node(4,[2,6])
	g.add_node(10,[20])
	print(g.is_tree())
	print(g.is_binary_tree())
	
	root=BinaryNode(8)
	root.left=BinaryNode(4)
	root.right=BinaryNode(10)
	root.left.left=BinaryNode(2)
	root.left.right=BinaryNode(6)
	root.right.right=BinaryNode(20)

	pre_order_traversal(root)
	
	
