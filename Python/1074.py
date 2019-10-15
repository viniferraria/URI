lista = []
x = int(input())

for i in range(x):
    y = int(input())
    if y>0 and y%2 != 0:
        lista.append("ODD POSITIVE")
    elif y<0 and  y%2 != 0:
        lista.append("ODD NEGATIVE")
    elif y>0 and y%2 == 0:
        lista.append("EVEN POSITIVE")
    elif y<0 and y%2 ==0:
        lista.append("EVEN NEGATIVE")
    else:
        lista.append("NULL")

for i in lista:
    print(i)