lista = []
def _positive_(x):
    cont = 0
    for i in lista: 
        if i>0:
            cont+=1
    return "%d valores positivos" %cont

for x in range (6):
    x = float(input())
    lista.append(x)
        
print(_positive_(lista))
