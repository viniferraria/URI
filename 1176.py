def fib(num):
  resultados = [0,1] + [0]*(num-1)
  for i in range(2,num+1):
    resultados[i] = resultados[i-1] + resultados[i-2]
  return "Fib({0}) = {1}".format(num, resultados[num])

testes = int(input())
for i in range(testes):
  num = int(input())
  print(fib(num))


