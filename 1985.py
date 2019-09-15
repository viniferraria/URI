
def _order_(loop):
    dict = {}
    for i in range(loop):
        cod,qtd = map(int,input().split())
        dict[cod] = qtd
    return dict

def _price_(dict):
    prices = {1001: 1.50, 1002: 2.50, 1003: 3.50, 1004: 4.50, 1005: 5.50}
    total = 0
    for i in prices:
        if i in dict:
            total += dict[i]*prices[i] 
    return total

def main():
    loop = int(input())
    order = _order_(loop)
    print("%.2f" %_price_(order))


main()
