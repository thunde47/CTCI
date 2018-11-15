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
		return True		
		
	def traversal(self, order="in"):
		pass
		
if __name__=="__main__":
	graph={"a":["b","c"]}
	g=Graph(graph)
	g.add_node("b",["d","e"])
	g.add_node("c",["f"])
	print(g.is_tree())
	g.show()
