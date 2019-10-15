#!/usr/bin/env python3 

def create_matrix():
     matrix = [[float(input()) for column in range(12)] for row in range(12)]
     return matrix


def aboveDiagonal(matriz):
     soma = [matriz[each][0 : each] for each in range(1 ,12)]
     total = 0
     qtd = 0
     for i in range(11):
          qtd += len(soma[i])
          total += sum(soma[i])
     return total, qtd


def main():
     option = input()
     matriz = create_matrix()
     soma, qtd = aboveDiagonal(matriz)
     if option.lower() == 'm':
          print("%.1f" %(soma/qtd))
     elif option.lower() == 's':
          print("%.1f" %soma)


main()

