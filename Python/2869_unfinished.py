import time
cache = [6, 1024]
        

def _menor_(qtd_de_divisores):
    start = time.time()
    count = 0
    x = 1
    while True:
        divisores = list(range(1,x+1))
        for b in divisores:                 
            if x%b == 0:
                count +=1
                
        if count == qtd_de_divisores:
            return ("%d time main2: %.8f" %(x,time.time()-start))
        count = 0      
        x+=1


def menor(qtd_de_divisores, x=1):
    start = time.time()
    count = 0
    print("x =",x)
    while True:
        divisores = list(range(1, x+1))
        for b in divisores:
            if x % b == 0:
                count += 1

        if count == qtd_de_divisores:
            return ("%d time main3: %.8f" % (x, time.time()-start))
        count = 0
        x += 1


def main2():
    #tentativas = int(input())
    #for i in range(tentativas):
    lista = [1,2,3,4,5,6,7,8,9,10,11]
    for i in lista:
        #qtd_divisores = int(input())
        #print(_menor_(qtd_divisores))
        print(_menor_(i))


def main3():
    #tentativas = int(input())
    #for i in range(tentativas):
    lista = [1, 4, 11, 100]
    for i in lista:
        if i == 11:
            print(menor(i,cache[0]))

        elif i == 100:
            print(menor(i,cache[1]))
            #qtd_divisores = int(input())
            #print(_menor_(qtd_divisores))
        else:
            print(menor(i))

main2()
main3()
