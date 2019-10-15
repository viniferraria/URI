def even(x):
    lista = [num for num in range(x,x+10) if num%2 == 0]
    print(*lista)
    return sum(lista)

def main():
    x = int(input())
    if x == 0:
        exit
    else:
        print(even(x))
        main()

main()