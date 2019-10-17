def _sum2_():
   s = 1
   pot = 1
   for i in range(3,40,2):
       s+= i/2**pot
       pot+=1
   return s
   
print("%.2f" %_sum2_())
    