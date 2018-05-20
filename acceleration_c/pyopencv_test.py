import ctypes
import cv2
import numpy as np
import numpy.ctypeslib as npct
import time
import random

ushortPtr = npct.ndpointer(dtype=np.uint16, ndim=1,  flags='CONTIGUOUS')
ucharPtr  = npct.ndpointer(dtype=np.uint8,  ndim=1,  flags='CONTIGUOUS')
libc = ctypes.CDLL("c/libpyopencv.so.1")
png2label = libc.png2label
png2label.argtypes = [ushortPtr, ucharPtr, ctypes.c_int, ctypes.c_int]#
png2box = libc.png2box
png2box.argtypes = [ushortPtr, ushortPtr, ushortPtr, ctypes.c_int, ushortPtr, ctypes.c_int, ctypes.c_int]#

hist = np.zeros(256,np.uint8)
t0 = time.time()
ana    = cv2.imread('./data/170927_070150200.png',-1)#16bit gray image
img    = cv2.imread('./data/170927_070150200.jpg') 
png2label(np.asarray(ana,np.uint16).ravel(), hist, ana.shape[0], ana.shape[1]) #np.array(ana).ravel()

label_list = []
label_idx  = []
for j in range(0, 255):
    if (hist[j]>0):
        label_list.append(j)

for j in range (0, len(label_list)):
    label_idx.append(hist[label_list[j]])
for j in range (1, len(label_list)):
    label_idx[j] = label_idx[j] + label_idx[j-1]

box_coordinate = np.zeros(int(np.sum(hist)*4),np.uint16)
for j in range(0,np.sum(hist)):
    box_coordinate[4*j]   = ana.shape[1]
    box_coordinate[4*j+2] = ana.shape[0]
png2box(np.asarray(ana,np.uint16).ravel(), box_coordinate, np.asarray(label_list, np.uint16), \
        len(label_list), np.asarray(label_idx, np.uint16), ana.shape[0], ana.shape[1]) 

t1 = time.time()
total = t1-t0

for j in range(0,np.sum(hist)):
    r = int(random.uniform(0, 1)*255)
    g = int(random.uniform(0, 1)*255)
    b = int(random.uniform(0, 1)*255)
    cv2.rectangle(img,(box_coordinate[4*j],box_coordinate[4*j+2]),(box_coordinate[4*j+1],box_coordinate[4*j+3]),(b,g,r),2)

#print(hist, total, ana.shape)
print(total, ana.shape, int(np.sum(hist)*4))
cv2.imwrite('test.png',img)

