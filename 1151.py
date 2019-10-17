cache = {}

def fibonacci(n):
    if n in cache:
        return cache[n]

    if n == 1 or n == 2:
        return 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        cache[n] = result
        return result    

a = int(input())
b = fibonacci(a-1)
print("0 1 1", end=' ')
a = [cache[i] for i in cache]
print(*a)
