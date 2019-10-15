'''def filter_array(array):
  par = list(filter(lambda x: x%2 == 0, array))
  impar = list(filter(lambda x: x%2 != 0, array))
  return par, impar
'''

def show_par(array):
  for i in range(len(array)):
    print("par[{0}] = {1}".format(i, array[i]))

def show_impar(array):
  for i in range(len(array)):
    print("impar[{0}] = {1}".format(i, array[i]))

def fill_IV(array):
  impar = []
  par = []
  for i in range(len(array)):
    if array[i]%2 != 0:
      if len(impar) == 5:
        show_impar(impar)
        impar = []
      impar.append(array[i])
    else:
      if len(par) == 5:
        show_par(par)
        par = []
      par.append(array[i])
  return impar, par

array = [0] * 15
for i in range(len(array)):
  array[i] = int(input())

impar, par = fill_IV(array)
show_impar(impar)
show_par(par)




