import cv2

#load image from file
img = cv2.imread('test.png')
print(image.shape)

#resize
img = cv2.resize(img,(y2,x2))

#pixel visit
(b,g,r) = img[x,y]

#contour to bounding box
cv2.boundingRect(seg)
#countour to area
cv2.contourArea (seg)

#draw image
cv2.puText(img, "blabla", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (r,g,b), 2)
