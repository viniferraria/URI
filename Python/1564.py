#!/usr/bin/env python3

def teraCopa(number):
    if number >= 1:
        return 'vai ter duas!'
    elif number == 0: 
        return 'vai ter copa!'


while True:
    try:
        test = int(input())
        print(teraCopa(test))
    except:
        break

