#!/usr/bin/env python3

def calculate(x, y, total_area):
  area = x*y
  if total_area != 100:
    landSize = (area*100/total_area)**0.5
    return landSize
  else:
    return area ** 0.5


def main():
  x, y, total_area = map(int, input().split())
  landSize = calculate(x,y,total_area)
  print("%d" %landSize)
  while(x != 0):
    x, y, total_area = map(int, input().split())
    landSize = calculate(x,y,total_area)
    print("%d" %landSize)

try:
  main()
except ValueError:
  exit

