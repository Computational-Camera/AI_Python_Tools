import numpy as np

np.zeros((10,4))
#check data type and dimmision
print(data.dtype, data.dim, data.shape)

#find max or min
result = np.where(data == np.amax(data)) #amin
