def _seq_():
    #x = quantidade numeros em uma linha
    #y = numero final da sequencia
    x,y = map(int,input().split())
    restante = y%x
    linhas = y//x
    
    #lista = sequencia de numeros
    lista = [list(range(x*i+1, x*i+x+1)) for i in range(linhas)]
    
    if restante !=0:
        linhas += 1    
        falta = list(range(linhas*x+1,x*linhas))
        lista.append(falta)    
        
    for i in range(linhas):
        print(*lista[i])
_seq_()