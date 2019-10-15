def _cube_(x):
    lista = [[row**i for i in range(1,4)] for row in range(1,x+1)]
    return lista

def show(lista,loop):
    for i in range(loop):
        for j in range(3):
            if j == 2:
                print("%d" %lista[i][j], end = "\n")
            else:
                print("%d" %lista[i][j], end = " ")

def main():
    x = int(input())
    show(_cube_(x),x)
    
main()

x = int(input())
for i in range(1,x+1):
    print("%d %d %d" %(i,i**2,i**3))
    