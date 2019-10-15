#!/usr/bin/env python3 --

def createMatrix():
  matrix = [[ float(input()) for column in range(12)] for row in range(12)]
  return matrix


def belowSecundary(matrix):
  soma = 0
  total = 0
  for each in range(1, 12):
    temp = matrix[each][11: 11 - each:-1]
    total += len(temp)
    soma += sum(temp)
  return soma, total


def main():
  opt = input()
  matriz = createMatrix()
  soma, total = belowSecundary(matriz)
  if opt.upper() == "S":
    print("%.1f" %soma)
  elif opt.upper() == "M":
    media = soma/total
    print("%.1f" %media)


main()

