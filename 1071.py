x = int(input())
y = int(input())

if x>y:
    x,y = y,x

x+=1
      
soma = sum(i for i in range(x,y) if i%2 != 0)

print(soma)
