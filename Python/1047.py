def _main_(a,b,c,d):
    #hora inicial =a , minuto inicial = b, horafinal = c, minutofinal = d
    c = c-a
    d = d-b
    if c == 0 and d==0:
        c = 24
    elif c == 0 and d>0:
        c = 0
    elif c==0:
        c = 24
    elif c<0:
        c+=24 
        
    if d<0:
        d+=60
        c-=1
    
    elif d>60:
        c+=1
        d-= 60
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(c,d))
  

a,b,c,d = map(int,input().split())

_main_(a,b,c,d)

