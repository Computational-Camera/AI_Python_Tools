import numpy as np

np.zeros((10,4))
#check data type
print(data.dtype)

#find max or min
result = np.where(data == np.amax(data)) #amin
