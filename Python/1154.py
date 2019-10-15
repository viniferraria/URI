def _media_(lista):
    return sum(lista)/(len(lista))

lista = [int(input())]

while True:
    x = int(input()) 
    if x<0:
        print("%.2f" %_media_(lista))
        break
    else:
        lista.append(x)