def _greater_(x,z):
    count = 1
    soma = x
    for i in range(x+1,z+1):
        soma += i
        if soma>z:
            count+=1
            return count
        else:
            count+=1
def main():
    x = int(input())
    y = int(input())
    while y<=x:
        y = int(input())
    print(_greater_(x,y))
    
main()