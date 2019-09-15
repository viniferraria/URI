def _lista_(x,y):
    if x>y:
        x,y = y,x 
    lista = [a for b in range(x,y) if b%2 != 0 and b!=x]
    return sum(lista)

def _show_(x):
    for i in x:
        print(i)

x = int(input())
resultados = []
for i in range(x):
    try:
        a,b = map(int,input().strip().split())
        resultados.append(_lista_(a,b))
    except:
        pass
        
_show_(resultados)
