def _quadrante_(x,y):
    if x>0 and y>0:
        return "primeiro"
    elif x>0 and  y<0:
        return "quarto"
    elif x<0 and y>0:
        return "segundo"
    elif x<0 and y<0:
        return "terceiro"

def main():
    while True:
        x,y = map(int,input().split())
        if x == 0 or y == 0:
            break
        else:
            print(_quadrante_(x,y))

main()