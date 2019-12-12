def weather():
	x,y,z = map(int, input().split())
	if y < x:
		if z >= y:
			return ":)"
		if (z-y) < (y-x):
			return ":)"
		if (z-y) >= (y-x):
			return ":("	

	if y > x:
		if z <= y:
			return ":("
		if z > y: 
			if z - y < y - x:
				return ":("
			if (z - y) >= (y - x):
				return ":)"
	if z < y:
		return ":("
	
	return ":)"


print(weather())
