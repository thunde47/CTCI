from stack import Stack
from queue import Queue

visited=list()
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
	
	def is_route(self, start, end):
		node=start
		while node:
			print(node, self.graph)	
			if len(self.graph[start])==0:
				return False
			if node==end:
				return True
			node_t=self.graph[node][0]
			if node_t==end:
				return True
			if node_t==start:
				del self.graph[node][0]
				node_t=start

			if node_t in self.graph:
				node=node_t
			else:
				del self.graph[node][0]	
				
			if len(self.graph[node])==0:
				self.graph.pop(node)
				node=start					
							
		
			
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

#Root->Left->Right			
def pre_order_traversal(node):
	
	print(node.value)	
	if node.left!=None:
		pre_order_traversal(node.left)
	if node.right!=None:
		pre_order_traversal(node.right)

#Left->Right->Root
def post_order_traversal(node):
	
	if node.left!=None:
		post_order_traversal(node.left)
	if node.right!=None:
		post_order_traversal(node.right)
	print(node.value)

#Left->Root->Right
def in_order_traversal(node):
	
	if node.left!=None:
		in_order_traversal(node.left)
	print(node.value)
	if node.right!=None:
		in_order_traversal(node.right)		
		

if __name__=="__main__":
	g=Graph()
	g.add_node(8,[4,10])
	g.add_node(4,[2,6])
	g.add_node(10,[20])
	print(g.is_tree())
	print(g.is_binary_tree())
	
	root=BinaryNode(1)
	root.left=BinaryNode(2)
	root.right=BinaryNode(3)
	root.left.left=BinaryNode(4)
	root.left.right=BinaryNode(5)
	root.right.right=BinaryNode(20)

	print("Pre order traversal")
	pre_order_traversal(root)
	print("Post order traversal")
	post_order_traversal(root)
	print("In order traversal")
	in_order_traversal(root)
	
	
