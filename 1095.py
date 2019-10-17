def _seq_():
    i = list(range(1,60,3))
    j = list(range(60,-1,-5))
    for p in range(len(j)):
        print("I=%d J=%d" %(i[p],j[p]))
    
_seq_()