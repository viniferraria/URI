def odds(x,y):
    lista = [num for num in range(x,x+(y*2)) if num%2 != 0]
    return sum(lista)


def main():
    x = int(input())
    for i in range(x):
        a,b = map(int,input().split())
        print(odds(a,b))
        
main()