def _pum_(loop):
    matriz = [[ value if row == 0 else value+(4*row) for value in range(1,4)] for row in range(loop)]
    return matriz

def show(matriz,loop):
    for i in range(loop):
        for j in range(3):
            print(matriz[i][j], end =" ")
        print("PUM",end ="\n")
            
def main():
    x = int(input())
    matriz = _pum_(x)     
    show(matriz,x)
main()

