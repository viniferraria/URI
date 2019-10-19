#!/usr/bin/env python3 --

def createMatrix():
  matrix = [[ float(input()) for column in range(12)] for row in range(12)]
  return matrix


def belowSecundary(matrix):
  total = 0
  soma = 0
  for each in range(1, 12):
    total += len(matrix[each])
    soma += sum(matrix[each][12: 12 - each:-1])
  return soma, total


def main():
  opt = input()
  matriz = createMatrix()
  soma, total = belowSecundary(matriz)
  if opt.upper() == "S":
    return "%.1f".format(soma)
  elif opt.upper() == "M":
    media = soma/total
    return "%.1f".format(media)


main()

