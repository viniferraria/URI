def _divisao_(x,y):
    try:
        return x/y
    except:
        return "divisao impossivel"

def _main_():
    x = int(input())
    for i in range(x):
        x,y = map(int,input().split())
        print(_divisao_(x,y))
    
_main_()