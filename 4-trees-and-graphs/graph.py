class Graph:
	def __init__(self, graph=dict()):
		self.graph=graph
		
	def add_node(self, node, connections):
		self.graph[node]=connections
		
	def show(self):
		print(self.graph)	
		
	def traversal(self, order="in"):
		pass
		
if __name__=="__main__":
	graph={"a":["b","c"]}
	g=Graph(graph)
	g.add_node("b",["d","e"])
	g.add_node("c",["f"])
	g.show()
