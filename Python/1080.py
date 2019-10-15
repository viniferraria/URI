lista = []*100
for i in range(100):
    x = int(input())
    lista.append(x)
print(max(lista))
print(lista.index(max(lista))+1)
