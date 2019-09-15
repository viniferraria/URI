def _fuel_(entrada,x = 0, y = 0, z = 0):
    alcool = x
    gas = y
    diesel = z
    if entrada == 1:
        alcool += 1
    elif entrada ==2:
        gas += 1
    elif entrada == 3:
        diesel += 1
    return alcool, gas, diesel
        
def main():    
    x = int(input())
    alcool,gas,diesel = _fuel_(x)
    while x != 4:
       x = int(input())
       alcool, gas, diesel = _fuel_(x,alcool,gas,diesel)
       if x == 4:
           print("MUITO OBRIGADO\nAlcool: %d\nGasolina: %d\nDiesel: %d" %(alcool,gas,diesel))
           break


main()