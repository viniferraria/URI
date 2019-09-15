def array_selection(array):
  for i in range(len(array)):
    if array[i] <= 10:
      print("A[{0}] = {1}".format(i, array[i]))

x = [float(input()) for i in range(100)]
array_selection(x)

