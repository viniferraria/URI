def reverse(array):
  for i in range(int(len(array)/2)):
    array[i], array[len(array) - 1 - i] = array[len(array) - 1 - i], array[i]
  return array

array  = [int(input()) for i in range(20)]
reversed_array = reverse(array)

for i in range(len(reversed_array)):
  print("N[{0}] = {1}".format(i,reversed_array[i]))
