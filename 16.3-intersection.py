def intersection(a_point_1, a_point_2, b_point_1, b_point_2):
	a_x_1, a_y_1 = a_point_1[0], a_point_1[1]
	a_x_2, a_y_2 = a_point_2[0], a_point_2[1]
	b_x_1, b_y_1 = b_point_1[0], b_point_1[1]
	b_x_2, b_y_2 = b_point_2[0], b_point_2[1]
	
	try:
		a_m=(a_y_2-a_y_1)/(a_x_2-a_x_1)
	except:
		a_m="INF"
		
	try:
		b_m=(b_y_2-b_y_1)/(b_x_2-b_x_1)
	except:
		b_m="INF"
	print(a_m, b_m)
	
	if a_m==b_m:
		return "No intersection"
	
	if a_m=="INF":
		return (a_x_1, b_m*(a_x_1-b_x_1)+b_y_1)
	
	if b_m=="INF":
		return (b_x_1, a_m*(b_x_1-a_x_1)+a_y_1)
		
	xi=(b_y_1-a_y_1+a_m*a_x_1-b_m*b_x_1)/(a_m-b_m)
	yi=a_m*(xi-a_x_1)+a_y_1
	return (xi,yi)
	
if __name__=="__main__":
	print(intersection((0,1),(2,2),(0,2),(2,0)))
		
