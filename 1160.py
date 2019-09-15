def population(cidade_a, cidade_b, crescimento_a, crescimento_b):
  cidade_a, cidade_b, crescimento_a, crescimento_b = int(cidade_a), int(cidade_b), float(crescimento_a), float(crescimento_b)
  anos = 0
 
  while cidade_a <= cidade_b:
    cidade_a += int(cidade_a * crescimento_a/100)
    cidade_b += int(cidade_b * crescimento_b/100)
    anos += 1

    if anos > 100:
      return "Mais de 1 seculo."

  return "{} anos.".format(anos)

qtd_testes = int(input())
for testes in range(qtd_testes):
  cidade_a, cidade_b, crescimento_a, crescimento_b = map(str, input().strip().split())
  print(population(cidade_a, cidade_b, crescimento_a, crescimento_b))

