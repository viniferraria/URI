def _fill_():
    elem = int(input())
    if elem <=0:
        return 1

def show(vetor):
    for i in range(len(vetor)):
        print("X[%d] = %d" %(i,vetor[i]))

def main():
    arr = []
    for i in range(10):
        arr[i] = _fill_()
    show(arr)

main()