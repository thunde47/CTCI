from stack import Stack
from queue import Queue

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
		
if __name__=="__main__":
	g=Graph()
	g.add_node(8,[4,10])
	g.add_node(4,[2,6])
	g.add_node(10,[12, 20])
	print(g.is_tree())
	print(g.is_binary_tree())
	g.pre_order_traversal(8)
	g.show()
