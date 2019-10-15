def _soma_(x,y):
    lista = list(range(x,x+y))
    return sum(lista)

def main():
    lista = list(map(int,input().split()))
    x = lista[0]
    lista = lista[1:]
    for i in lista:
        if i>0:
            y = i
        
    print(_soma_(x,y))
    
main()