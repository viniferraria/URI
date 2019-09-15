x = int(input())
if x%2 != 0:
    x+=1
x = [i for i in range(x+1,x+12,2)]
for i in x:
    print(i)