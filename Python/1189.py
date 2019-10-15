#!/usr/bin/env python3

def createMatrix():
  matrix = [[ float(input()) for column in range(12)] for row in range(12)]
  return matrix


def leftArea(matrix):
  soma = 0
  qtd = 0
  left = [matrix[each][0: each] if each < 6 else matrix[each][0: 11 - each] for each in range(1, 11)]
  for i in range(10):
    soma += sum(left[i])
    qtd += len(left[i])
  return soma, qtd
    

def main():
  opt = input()
  matriz = createMatrix()
  soma, qtd = leftArea(matriz)
  if opt.upper() == 'S':
    print('%.1f' %soma)
  elif opt.upper() == 'M':
    media = soma/qtd
    print('%.1f' %media)


main()
