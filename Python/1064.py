x = 0
cont = 0

for i in range(6):
    y = float(input())
    if y>0:
        cont+=1
        x+=y

x/=cont

print("%d valores positivos\n%.1f" %(cont,x))
    