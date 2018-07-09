#check the current device being used cpu or gpu
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

#Memory usage, by default, the GPU memory will be all occpupied
from keras.backend.tensorflow_backend import set_session
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
set_session(tf.Session(config=config))
