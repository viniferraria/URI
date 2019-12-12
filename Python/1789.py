#!/usr/bin/env python3

def slugs():
  while True:
    try:
      qnt_slugs = int(input())
      slugs_speeds = list(map(int,input().split()))[:qnt_slugs]
      level = max(slugs_speeds)
      if level < 10:
        print(1)
      elif level < 20:
        print(2)
      else:
        print(3)
    except:
      break

slugs()
