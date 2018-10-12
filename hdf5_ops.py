import numpy as np
import h5py

data_to_write = np.random.random(size=(100,20))

#=========Write========
hf = h5py.File('name-of-file.h5', 'w')
hf.create_dataset("name-of-dataset",  data=data_to_write) #must have data=, may also add type="uint16"
  
#=========Read=========
with h5py.File('name-of-file.h5', 'r') as hf:
    data = hf['name-of-dataset'][:]
