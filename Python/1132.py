def _not13_(x,y):
    lista = [i for i in range(x,y+1) if i%13 != 0 ]
    return sum(lista)

def main():
    x = int(input())
    y = int(input())
    if x>y:
        x,y = y,x
    print(_not13_(x,y))
    
main()