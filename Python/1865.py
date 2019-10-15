def _mjolnir():
    name, force = map(input().split())
    if name == "Thor":
        return "Y"
    else: 
        return "N"
    
def main():
    cases = int(input())
    for i in range(cases):
        print(_mjolnir())

main()