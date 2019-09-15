aumento = [1.15, 1.12, 1.10, 1.07, 1.04]

def check(x):
    taxa = 0
    if x>0 and x<400.01:
        taxa = aumento[0]
    elif x>400.00 and x<=800.00:
        taxa = aumento[1]
    elif x>800.00 and x<=1200.00:
        taxa = aumento[2]
    elif x>1200.00 and x<=2000.00:
        taxa = aumento[3]
    elif x>2000.00:
        taxa = aumento[4]
    return taxa

def salario(x):
    x*= check(x)
    return x
        
before = float(input())
after = salario(before)

print("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: %.f"%(after,after-before,(check(before)-1)*100)+" %") 

