def _media_(a):
    return sum(a)/len(a)

def _main_():
    lista= []
    while len(lista)!=2:
        x = float(input())
        if x<0.0 or x>10.0:
          print("nota invalida")
        else:
          lista.append(x)
    print("media = %.2f" %_media_(lista))

_main_()