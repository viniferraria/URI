def _div_(x,y):
    lista = [i for i in range(x+1,y) if i%5 == 2 or i%5 == 3]
    return lista
            
def main():
    x = int(input())
    y = int(input())
    if x>y:
        x,y = y,x
    for i in _div_(x,y):
        print(i)
        
main()