from graph import Graph	

if __name__=="__main__":
	
	graph={1:[2,3,6], 2:[1,5],5:[3,4],6:[7]}
	g=Graph(graph)
	print(g.is_route(1,7))
