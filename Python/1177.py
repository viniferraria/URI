def array(x):
    lista =[0]*1000
    count = 0 
    for j in range(1000):
        if count <x:
            lista[j] = count
            count+=1
            if count == x:
                count = 0
    for i in range(1000):
        print("N[%d] = %d" %(i,lista[i]))

x = int(input())
array(x)