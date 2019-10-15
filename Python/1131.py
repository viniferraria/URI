def _grenal_(vitoria_i = 0, vitoria_g = 0, tie = 0):
    score_inter, score_gremio = map(int,input().split())
    
    vit_inter = vitoria_i
    vit_gremio = vitoria_g
    empate = tie
    
    if score_inter > score_gremio:
        vit_inter += 1
    elif score_inter==score_gremio:
        empate += 1
    else:
        vit_gremio += 1

    return vit_inter,vit_gremio,empate

def main():
    count = 1
    inter,gremio,empate = _grenal_()
    
    while True:
        op = int(input("Novo grenal (1-sim 2-nao)\n"))

        if op == 1:
            count+=1
            inter,gremio,empate = _grenal_(inter,gremio,empate)
            
        else:
            print("%d grenais\nInter:%d\nGremio:%d\nEmpates:%d" %(count,inter,gremio,empate))
            
            if inter>gremio:
                print("Inter venceu mais")
                
            elif inter == gremio:
                print("Nao houve vencedor")

            else:
                print("Gremio venceu mais")
            break
            
main()