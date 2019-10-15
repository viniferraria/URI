#!/usr/bin/env python3

winks_values = {"*--": 4, "-*-": 2, "--*": 1}

for i in range(3):
    result = 0
    while True: 
        crow = input().strip()
        if crow in winks_values:
            result += winks_values[crow]
        elif crow[0] == "c":
            break
    print(result)
