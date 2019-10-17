def _double_(x): 
    lista = [0]*10
    lista[0] = x
    print("N[0] = %d" %x)
    for i in range(1,10):
        lista[i] = lista[i-1]*2
        print("N[%d] = %d" %(i,lista[i]))
    
X = int(input())
_double_(X)
