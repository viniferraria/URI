def _seq_():
    x = int(input())  
    lista = [[i,i**2,i*i**2,i,i**2+1,i*i**2+1] for i in range(1,x+1)]
    for i in range(x):
        print(*lista[i][:3])
        print(*lista[i][3:])
_seq_()