def _even_():
    return list(range(2,102,2))
    
def _prt_(x):
    for i in x:
        print("%d" %i)
        
_prt_(_even_())
    