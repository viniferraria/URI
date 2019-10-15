lista = []

x = int(input())
for i in range(x):
    y = int(input())
    if y>=10 and y<=20:
        lista.append(y)

print(len(lista),"in")
print(x-len(lista),"out")