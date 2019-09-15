def _seq_():
    i = 0.0
    j = [1.0,2.0,3.0]
    while i<=2.00:
        for a in j:
            if str(i)[2] == '0':
                print("I=%d J=%d" %(i, a))
            else:
                print("I=%.1f J=%.1f" %(i, a))
        j = [round(a+0.2,2) for a in j]
        i = round(i+0.2,2)

_seq_()
