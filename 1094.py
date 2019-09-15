x = int(input())
C = 0
R = 0
S = 0

for i in range(x):
    a,b = input().split(" ")
    a = int(a)
    b = b.upper()
    if b == "C":
        C+=a
    elif b == "R":
        R+=a
    elif b == "S":
        S+=a

total = C+R+S

print("Total: %d cobaias" %total)
print("Total de coelhos: %d" %C)
print("Total de ratos: %d" %R)
print("Total de sapos: %d" %S)
print("Percentual de coelhos: %.2f " %(C/total*100)+"%")
print("Percentual de ratos: %.2f " %(R/total*100)+"%")
print("Percentual de sapos: %.2f " %(S/total*100)+"%")