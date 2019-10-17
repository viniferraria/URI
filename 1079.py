lista = []
x = int(input())

for i in range(x):
    a,b,c = map(float,input().strip().split())
    lista.append((a*2+b*3+c*5)/10)

for i in lista:
    print("%.1f" %i)