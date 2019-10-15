line = int(input())
option = input()

array = [ [ float(input()) for i in range(12) ] for i in range(12) ]

if option.upper() == "S":
  soma = sum(array[line])
  print(soma)

elif option.upper() == "M":
  media =  sum(array[line])/len(array[line])
  print(media)

