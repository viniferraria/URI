def theons():
	num_people = int(input())
	t = list(map(int, input().split()))
	awnser = t.index(min(t)) + 1
	return awnser

print(theons())

