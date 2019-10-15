def _tri_():
    tria = list(map(float,input().strip().split()))[:3]
    tria.sort(reverse = True)
    ladoa = tria[0]
    ladob = tria[1]
    ladoc = tria[2]
    if ladoa>=(ladob+ladoc):
        print("NAO FORMA TRIANGULO")
    else:
        if ladoa**2 == ladob**2 + ladoc**2:
            print("TRIANGULO RETANGULO")
        if (ladoa**2)>(ladob**2+ ladoc**2):
            print("TRIANGULO OBTUSANGULO")
        if (ladoa**2)<(ladob**2)+(ladoc**2):
            print("TRIANGULO ACUTANGULO")
        if ladoa == ladob==ladoc:
            print("TRIANGULO EQUILATERO")
        if ladoa==ladob and ladoa!=ladoc or ladob==ladoc and ladob != ladoa or ladoa==ladoc and ladoa!=ladob:
            print("TRIANGULO ISOSCELES")
           
_tri_()
