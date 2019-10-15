x = 0
impar = 0
par = 0
positivo = 0
negativo = 0

for i in range(5):
    y = int(input())
    if y%2 == 0:
        par+=1
    elif y%2 !=0:
        impar+=1
    
    if y>0:
        positivo+=1
    elif y<0:
        negativo+=1
        

print("%d valor(es) par(es)\n%d valor(es) impar(es)\n%d valor(es) positivo(s)\n%d valor(es) negativo(s)" %(par,impar,positivo,negativo))
    