import cv2

#init an array
img = np.zeros((height,width,3), np.uint8)

#load image from file
img = cv2.imread('test.png')# add additional flag 0:for mono import, -1: 16bit
height = img.shape[0]
width  = img.shape[1]
# or  height, width, channel = image.shape
print(image.shape)

#write image
cv2.imwrite('img.png', img)

#resize
img = cv2.resize(img,(w2,h2))

#pixel visit
(b,g,r) = img[x,y]

#contour to bounding box
cv2.boundingRect(seg)  # [x,y,w,h]
#countour to area
cv2.contourArea (seg)

#draw image
cv2.putText(img, "blabla", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (r,g,b), 2)
cv2.rectangle(img, (x1,y1), (x2,y2), (0, 0, 255), 3)#, -1 solid

#color coding
img2 = cv2.applyColorMap(img, cv2.COLORMAP_JET)


