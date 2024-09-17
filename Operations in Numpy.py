import numpy as np 

a = np.zeros((3,3), dtype = np.int32)
a[:] = 2
a.fill(8) #fill the matrix with 8
a += 3 #same as abow but more detailed
#print(a)

b = np.arange(1,10).reshape((3,3))
#print(b)
#arithamatic Methodes
array_sum = a.sum()
array_sum = a.sum(axis = 0) #get the sum of each columes
array_sum = b.sum(axis = 1) #get the sum of rows
print(array_sum)

#product

array_product = a.prod()
print(array_product)