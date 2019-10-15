x = int(input())
lista = [x*i for i in range(1,11)]
vezes = 1
for i in lista:
    print("%d x %d = %d" %(vezes,x,i))
    vezes+=1