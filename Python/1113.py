while True:
    a,b = map(int,input().split())
    if a>b:
        print("Decrescente")
    elif a<b:
        print("Crescente")
    else:
        break