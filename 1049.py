def tax(x):
    after = 0
    if x>0 and x<=2000.00:
        return ("Isento")
    elif x>2000.00 and x<=3000.00:
        x-=2000
        after += x*0.08
        print(after)
    elif x>3000.0 and x<=4500.00:
        x-=3000
        after+= x*0.18 + 80
    elif x>4500.00:
        x-=4500
        after+= x*0.28 + 350
        
    return("R$ %.2f" %(after))

x = float(input())
print(tax(x))
            