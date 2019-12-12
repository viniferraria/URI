#!/usr/bin/env python3 -i

def preface(a, b):
	r = a%b
	q = (a - r)/b
	print(q)
	print(r)


while True: 
	x, y = map(int, input().split())
	preface(x,y)
