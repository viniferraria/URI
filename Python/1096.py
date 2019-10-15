def _seq_():
    i = 1
    j = [7,6,5]
    while i<10:
        for a in j:
            print("I=%d J=%d" %(i,a))
        i+=2
        
_seq_()