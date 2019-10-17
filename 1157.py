def _div_():
    num = int(input())
    return [divisor for divisor in range(1,num+1) if num%divisor ==0]

def prnt(lista):
    for i in lista:
        print(i)
        
x = _div_()
prnt(x)