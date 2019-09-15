x = int(input())
x = [i for i in range(2,x+1,2)]

for i in x:
    print("%d^2 = %d" %(i,i**2))