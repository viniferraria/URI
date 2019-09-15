def _date_():
    try:
        di = input().split()
        hi,mi,si = map(int,input().strip().split(":"))
        df = input().split()
        hf,mf,sf = map(int,input().strip().split(":"))
    
        df = int(df[1]) - int(di[1]) 
        
        hf = hf - hi
        if hf<0:
            hf += 24
            df -= 1
        
        mf = mf - mi
        if mf<0:
            mf += 60
            hf -= 1
            
        sf  = sf - si
        if sf<0:
            sf += 60
            mf -= 1
            
        if df<=0:
            df = 0
            
        print("%d dia(s)" %df)
        print("%d hora(s)" %hf)
        print("%d minuto(s)" %mf)
        print("%d segundo(s)" %sf)
    except:
        print("0 dia(s)\n0 hora(s)\n0 minuto(s)\n0 segundo(s)\n")
        

_date_()