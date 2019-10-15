def _media_(a):
    return sum(a)/len(a)

def _notas_():
    lista = []
    for i in range(2):
        grade = float(input())
        while grade < 0.0 or grade > 10.0:
            grade = float(input("nota invalida\n"))
        lista.append(grade)
    return _media_(lista)

def _main_():
    print("media = %.2f" %_notas_())
    while True:
        op = float(input("novo calculo (1-sim 2-nao)\n"))
        while op<1 or op>2:
            op = float(input("novo calculo (1-sim 2-nao)\n"))
        if op == 1:
            print("media = %.2f" %_notas_())
        else:
            break

_main_()
