
while True:
    m,n = map(int,input().split())
    if m <=0 or n <=0:
        break
    elif m>n:
        m,n = n,m
    lista = list(range(m,n+1))
    print(*lista, end =" ")
    print("Sum=%d" %sum(lista))
