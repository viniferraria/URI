def fill():
  array = [0] * 100
  array[0] =  float(input())
  #filled_array = [array[i-1]/2 for i in range(1,100)]
  filled_array = list(map(lambda x: x/2, array[1:]))
  return filled_array

print(fill())
