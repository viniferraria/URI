def _seq_():
    #x = quantidade numeros em uma linha
    #y = sequencia de numeros
    x,y = map(int, input().split())
    y = list(range(1,y+1))
    restante = len(y)%x
    linhas = len(y)//x
    
    if restante != 0:
        linhas += 1
        
    for i in range(linhas):
        print(*y[:x])
        for i in range(x):
            if len(y)>0:
                y.pop(0)    
_seq_()