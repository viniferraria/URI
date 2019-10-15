x = int(input())
lista = [i for i in range(10000) if i%x==2]
for i in lista:
    print(i)