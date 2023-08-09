import numpy as np

# var1=np.array([2,3,4])
# print(var1)
# print(var1.size)
# print(var1.itemsize)
# print(var1.dtype)
# print(var1.ndim)
# print(var1.max())
# print(var1.sum())

# var1=np.array([(2,3,4), (3,4,5)])
# var2=np.array([(2,3,4), (3,4,5)])
# print(var1+var2)

# var3=np.array([(2,3,4), (3,4,5)])
# print(var3)
# print(var3.shape)
# var3=var3.reshape(3,2)
# print(var3)
# print(var3.shape)

# var5=np.linspace(10, 50, 35)
# print(var5)

# slicing 
var4=np.array([(2,3,4), (3,4,5)])
print(var4[0,1])
print(var4[0:, 1])


var6=np.array([(2,3,4), (3,4,5)])
print(var6.ravel())
print(var6.sum(axis=0))  # 0 for column
print(var6.sum(axis=1))  # 1 for row
print(np.sqrt(var6))     # square root of all elements
print(np.std(var6))      # standard deviation


#functions
var7=np.array([(2,3,4), (3,4,5)])
print(np.exp(var7))
print(np.log(var7))